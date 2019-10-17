from .models import Video
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from user.serializers import  UserDetailSerializer

class VideoSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = Video
        fields = "__all__"


class AdminVideoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Video
        fields = "__all__"