from .models import Announcement
from .models import OjCarouselImg
from .models import BlogCarouselImg
from user.serializers import UserDetailSerializer

from rest_framework import serializers
from django.db.models import Q

class AnnSerializer(serializers.ModelSerializer):
    Belong = UserDetailSerializer()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Announcement
        fields = "__all__"


class OjCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = OjCarouselImg
        fields = '__all__'

class BlogCarouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCarouselImg
        fields = '__all__'


