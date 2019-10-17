from django.shortcuts import render
from utils.SomeSetting import MyPagination
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .models import  Article,ArticleUpDown,Comment
from .serializers import ArticleSerializer,AdminArticleSerializer
from .serializers import UpDownSerializer,AdminUpDownSerializer
from .serializers import CommentSerializer,AdminCommentSerializer
from .filters import ArticleFilter
from utils.SomeSetting import MyPagination
from django.db.models import Q
from .filters import CommentFilter
from rest_framework.decorators import parser_classes

from django.views.decorators.csrf import csrf_exempt#不进行csrf验证

# Create your views here.


class ArticleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
               返回所有文章 过滤,排序
               list:
                   获取所有文章
                retrieve:
                    文章详情
               """
    queryset = Article.objects.all().filter(Q(is_disabled=False) & Q(State=1) )
    serializer_class = ArticleSerializer
    pagination_class = MyPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ArticleFilter

    search_fields = ('title', 'desc')
    ordering_fields = ('browse', 'ThumbsUp','CommentCount','create_time')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.browse += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class AdminArticleViewSet(viewsets.ModelViewSet):
    """
    管理文章
    list:
        获取所有文章
    retrieve:
        文章详情
    create:
           添加文章
    update:
           更新文章
    delete:
           删除文章
    """

    pagination_class = MyPagination
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve" or self.action == 'list':
            return ArticleSerializer

        elif self.action == "create" or self.action == "update":
            return AdminArticleSerializer

        return ArticleSerializer




class ArticleUpDownViewSet():
    """
    目前不设计查看所有的点赞人
    """
    pass


class AdminArticleUpDownViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.DestroyModelMixin,
                                mixins.CreateModelMixin,
                                viewsets.GenericViewSet):
    """
    点赞
    create:
        给文章点赞
    update:
        更新点赞(是不是还点赞)
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    serializer_class = AdminUpDownSerializer
    lookup_field = 'article'
    def get_queryset(self):
        return ArticleUpDown.objects.filter(user=self.request.user)




class CommentViewSet(mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet,
                   mixins.ListModelMixin,):
    """
    评论

    """
    queryset = Comment.objects.all().filter(layer=1)
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = CommentFilter




class AdminCommentViewSet(mixins.CreateModelMixin,
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
    serializer_class = AdminCommentSerializer
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)






from rest_framework.decorators import api_view,authentication_classes,permission_classes
import os
from django.http import JsonResponse
import datetime


@api_view(['POST','GET'])
@authentication_classes((JSONWebTokenAuthentication, authentication.SessionAuthentication))
@permission_classes((IsAuthenticated,))
@csrf_exempt
def upload_file(request):
    # 中文不能上传.
    myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
    if not myFile:
        return Response("no files for upload!")
    hou = myFile.name[-4:]
    myFile.name = myFile.name + datetime.datetime.now().strftime(
        '%Y-%m-%d-%H:%M:%S'
    )+hou
    destination = open(os.path.join("./media/", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作

    for chunk in myFile.chunks():  # 分块写入文件
        destination.write(chunk)

    destination.close()

    ret = {
        "code":200,
        "data":{
            "url":"http://127.0.0.1:8000/media/"+myFile.name,
        },
        "info": "请求成功"
    }

    return JsonResponse(ret)

