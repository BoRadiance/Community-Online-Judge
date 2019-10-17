from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import authentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from utils.SomeSetting import MyPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets
from .models import ProblemTages,CodingProlemInfo,OtherProblem
from .serializers import ProblemTagSerializer,CodingProblemSerializer
from .serializers import AdminCodingProblemSerializer

from .filters import ProblemTagFilter,CodingProblemFilter

class ProblemTagViewSet(mixins.ListModelMixin,viewsets.GenericViewSet,mixins.RetrieveModelMixin):
    """
    问题标签
    list:
        所有的标签
    """

    queryset = ProblemTages.objects.all()
    serializer_class = ProblemTagSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ProblemTagFilter


class CodingProblemViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    编程题
    list:
        获取可用的编程题
    retrieve:
        获取具体编程题
    """


    pagination_class = MyPagination
    serializer_class = CodingProblemSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = CodingProblemFilter

    search_fields = ('title', )


    def get_queryset(self):
        return CodingProlemInfo.objects.filter(is_disabled=False)








class AdminCodingProblemViewSet(viewsets.ModelViewSet):
    """
    管理编程题
    list:
        获取编程题
    create:
        新建编程题
    update:
        更新编程题
    delete:
        删除编程题
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, authentication.SessionAuthentication)

    serializer_class = AdminCodingProblemSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = CodingProblemFilter

    def get_queryset(self):
        return CodingProlemInfo.objects.filter(user=self.request.user)






