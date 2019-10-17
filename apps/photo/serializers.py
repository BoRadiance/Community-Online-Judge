from .models import PhotoDetail,Photos
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from user.serializers import UserDetailSerializer


class UsePicSerialzier(serializers.ModelSerializer):
    class Meta:
        model = PhotoDetail
        fields = ("Img",)


class PhotosSerializer(serializers.ModelSerializer):
    pic = UsePicSerialzier(many=True)
    user = UserDetailSerializer()

    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Photos
        fields = "__all__"



class AdminPhotosSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Photos
        fields = "__all__"




class PhotoDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = PhotoDetail
        fields = "__all__"

    def create(self, validated_data):
        obj = PhotoDetail.objects.create(**validated_data)

        print(obj.Belong.user)
        print(obj.user)
        if obj.Belong.user!=obj.user:
            print('不是同一个人啊!')
            obj.delete()


        return obj






