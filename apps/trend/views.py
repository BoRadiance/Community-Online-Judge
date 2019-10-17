from django.shortcuts import render
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .models import TrendClass,TrendComment,Trend,TrendUpDown,TrendPhoto
from .serializers import TrendClassSerializer,TrendSerializer,AdminTrendSerializer
from .serializers import TrendUpDownSerializer,AdminTrendUpDownSerializer,TrendPhotoSerializer
from .serializers import TrendCommentSerializer,AdminTrendCommentSerializer
from django.db.models import Q
from utils.SomeSetting import MyPagination
from .filters import TrendPhotoFilter,TrendCommentFilter,TrendFilter


# Create your views here.
class TrendClassViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    获取所有动态类
    """
    queryset = TrendClass.objects.all().filter(is_disabled=False)
    serializer_class = TrendClassSerializer


class TrendViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    返回动态列表:
    list:
        获取所有动态
    retrieve:
        动态详情
    filter:
        过滤动态
    """
    queryset = Trend.objects.all().filter(State=1)
    serializer_class = TrendSerializer
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = TrendFilter

    ordering_fields = ('browse', 'ThumbsUp', 'CommentCount', 'create_time')

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        instance.browse += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class AdminTrendViewSet(viewsets.ModelViewSet
                        ):
    """
    管理动态:
     list:
        获取所有
    retrieve:
        详情
    update:
        更新
    create:
        添加
    delete:
        删除
    """

    pagination_class = MyPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)

    def get_queryset(self):
        return Trend.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == 'list':
            return TrendSerializer

        elif self.action == "create" or self.action == "update":
            return AdminTrendSerializer

        return TrendSerializer


class TrendPhotoViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    动态图片

    """
    queryset = TrendPhoto.objects.all()
    serializer_class = TrendPhotoSerializer
    lookup_field = 'artile'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = TrendPhotoFilter


class AdminTrendPhotoViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin):
    """
    动态图片管理:
            list:
               获取所有照片
           create:
               添加照片
           delete:
               删除相册
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    serializer_class = TrendPhotoSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = TrendPhotoFilter

    def get_queryset(self):
        return TrendPhoto.objects.filter(user=self.request.user)


class AdminTrendUpDownViewSet(mixins.ListModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    点赞
    create:
        给动态点赞
    destory:
        取消点赞
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    serializer_class = AdminTrendUpDownSerializer
    lookup_field = 'article'
    def get_queryset(self):
        return TrendUpDown.objects.filter(user=self.request.user)






class TrendCommentViewSet(mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet,
                   mixins.ListModelMixin,):
    """
    评论
    """
    queryset = TrendComment.objects.all().filter(layer=1)
    serializer_class = TrendCommentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = TrendCommentFilter



class AdminTrendCommentViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,):
    """
    评论管理
    list:
        查看所有的评论
    create:
        添加评论
    delete:
        删除评论

    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    serializer_class = AdminTrendCommentSerializer
    def get_queryset(self):
        return TrendComment.objects.filter(user=self.request.user)


