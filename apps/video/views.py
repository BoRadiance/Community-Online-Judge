from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Video
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .serializers import VideoSerializer,AdminVideoSerializer
from .filters import VideoFilter


# Create your views here.

class VideoViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
           返回所有视频
           list:
               获取所有视频
           """
    queryset = Video.objects.all().filter(is_disabled=False)
    serializer_class = VideoSerializer

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    filter_class = VideoFilter


class AdminViedoViewSet(viewsets.ModelViewSet):
    """
    视频管理
    list:
        获取所有视频
    create:
        添加视频
    update:
        更新视频
    delete:
        删除视频

    """
    serializer_class = AdminVideoSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    def get_queryset(self):
        return Video.objects.filter(user=self.request.user)


