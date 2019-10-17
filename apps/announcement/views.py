from django.shortcuts import render
from .serializers import AnnSerializer,OjCarouselSerializer,BlogCarouseSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from utils.SomeSetting import MyPagination
from rest_framework import mixins
from rest_framework import viewsets
from .models import Announcement,OjCarouselImg,BlogCarouselImg
from django.http import HttpResponse,JsonResponse
class AnnViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnSerializer


    ordering_fields = ('create_time',)


class OJCarViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = OjCarouselImg.objects.filter(is_disabled=False)
    serializer_class = OjCarouselSerializer


class BlogCarViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    queryset = BlogCarouselImg.objects.filter(is_disabled=False)
    serializer_class = BlogCarouseSerializer

import json
import random

class DaySen(APIView):
    def get(self,request):
        data = open("../days.json",encoding='utf-8')
        strjson = json.load(data)
        length = len(strjson["list"])
        i = random.randint(0,length-1)
        ret = {
            "code":200,
            "sen":strjson["list"][i],
        }
        data.close()
        return JsonResponse(ret)
