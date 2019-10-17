from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from .models import Photos,PhotoDetail
from rest_framework import permissions
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from .filters import PhotosFilter,PhotoDetailFilter
from .serializers import PhotosSerializer,AdminPhotosSerializer,PhotoDetailSerializer
# Create your views here.


class PhotosViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
           返回所有相册
           list:
               获取所有相册
           """
    queryset = Photos.objects.all().filter(is_disabled=False)
    serializer_class = PhotosSerializer

    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter,)
    filter_class = PhotosFilter


class AdminPhotosViewSet(viewsets.ModelViewSet):
    """
           相册管理
           list:
               获取所有相册
           create:
               添加相册
           update:
               更新相册
           delete:
               删除相册
           """
    serializer_class = AdminPhotosSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    def get_queryset(self):
        return Photos.objects.filter(user=self.request.user)


class PhotoDetailViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    照片
    """
    queryset = PhotoDetail.objects.all()
    serializer_class = PhotoDetailSerializer
    lookup_field ='Belong'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = PhotoDetailFilter




class AdminPhotoDetailViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   ):
    """
     照片管理
           list:
               获取所有照片
           create:
               添加照片
           delete:
               删除相册
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)


    serializer_class = PhotoDetailSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = PhotoDetailFilter

    def get_queryset(self):
        return PhotoDetail.objects.filter(user=self.request.user)

