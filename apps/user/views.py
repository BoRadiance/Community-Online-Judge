from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import User,UserInfoImg
from .models import Tag as UserTag
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from .serializers import UserDetailSerializer,UserRegSerializer
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.hashers import make_password
from .serializers import TagSerializer,UserInfoImgSerializer,UpdateUserDetailSerializer
from .filters import TagFilter
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from utils.permissions import IsOwnerOrReadOnly

from itsdangerous import TimedJSONWebSignatureSerializer as Serializers
from itsdangerous import SignatureExpired
from django.conf import settings
from rest_framework.views import APIView

import re
from celery_tasks.tasks import send_register_active_email

from .serializers import AdminUserInfoImgSerializer,AdminTagSerializer


class UserViewset(CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    用户
    """
    serializer_class = UserRegSerializer
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserRegSerializer

        return UpdateUserDetailSerializer

    # permission_classes = (permissions.IsAuthenticated, )
    def get_permissions(self):
        if self.action == "retrieve": # 如果是返回某个用户就要权限
            return [permissions.IsAuthenticated()]
        elif self.action == "create":# 如果是注册就没有要求
            return []

        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        user = self.perform_create(serializer)
        ret = re.match("\w{4,20}@(163|126|qq)\.com", serializer.validated_data['MyEmail'])
        if not ret:
            res = {}
            res['message'] = '邮箱格式不正确'
            user.delete()
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


        #print(serializer.validated_data)
        #return
        user.password=make_password(serializer.validated_data['password'])


        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username
        # print('--------------------')
        # print(user.password)

        user.save()
        newinfoimg = UserInfoImg.objects.create(user=user)

        # print('--------------------')






        headers = self.get_success_headers(serializer.data)
        # # 发送激活邮件
        # # 加密用户的身份信息，生成激活token
        # serializer = Serializers(settings.SECRET_KEY, 3600)
        # info = {'confirm': user.id}
        # token = serializer.dumps(info)  # bytes
        # token = token.decode()
        #
        # send_register_active_email.delay(user.MyEmail, user.username, token)

        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def get_object(self):
        return self.request.user

    def perform_create(self, serializer):
        return serializer.save()


class ActiveView(APIView):
    def get(self, request,token):
        '''进行用户激活'''
        print(token)
        # 进行解密，获取要激活的用户信息
        serializer = Serializers(settings.SECRET_KEY, 3600)
        try:
            info = serializer.loads(token)
            # 获取待激活用户的id
            user_id = info['confirm']

            # 根据id获取用户信息
            user = User.objects.get(id=user_id)
            user.Check = True
            user.save()

            return HttpResponse('恭喜成功激活!')
        except SignatureExpired as e:
            # 激活链接已过期
            return HttpResponse('激活链接已过期!')



class ShowUserViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):


    queryset = User.objects.all().order_by('id')
    serializer_class = UserDetailSerializer

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    ordering_fields =('create_time',)





class TagViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
           返回所有标签
           list:
               获取所有标签
           """

    queryset = UserTag.objects.all().filter(is_disabled=False)
    serializer_class = TagSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_class = TagFilter




class AdminTagViewSet(viewsets.ModelViewSet):
    """
       标签管理
       list:
           获取所有标签
       create:
           添加标签
       update:
           更新标签
       delete:
           删除标签
       """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)



    def get_queryset(self):
        return  UserTag.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list" or self.action=="retrieve":
            return TagSerializer
        elif self.action == "create":
            return AdminTagSerializer

        return AdminTagSerializer


class UserInfoImgViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    头像和封面图
    list:
        获取
    update:
        更新
    """
    queryset = UserInfoImg.objects.all().order_by('id')
    serializer_class = UserInfoImgSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    ordering_fields =('create_time',)





class AdminUserInfoImgViewSet(viewsets.GenericViewSet,mixins.ListModelMixin, mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    serializer_class = AdminUserInfoImgSerializer

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def get_queryset(self):
        return UserInfoImg.objects.filter(user=self.request.user)



