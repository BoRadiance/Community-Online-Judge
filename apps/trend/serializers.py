from .models import TrendClass,TrendComment,Trend,TrendUpDown,TrendPhoto
from user.serializers import UserDetailSerializer
from rest_framework import serializers

class TrendClassSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    class Meta:
        model = TrendClass
        fields = '__all__'

class UseTrendPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendPhoto
        fields = ('Image',)


class UseTrendClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendClass
        fields =('title','id')


class TrendSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    photo = UseTrendPhotoSerializer(many=True)
    user  = UserDetailSerializer()
    tags = UseTrendClassSerializer()
    class Meta:
        model = Trend
        fields = '__all__'





class AdminTrendSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


    class Meta:
        model = Trend
        fields = ('user','tags','content','is_disabled')


class TrendPhotoSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = TrendPhoto
        fields = '__all__'

    def create(self, validated_data):
        obj = TrendPhoto.objects.create(**validated_data)

        print(obj.article.user)
        print(obj.user)
        if obj.article.user != obj.user:
            print('不是同一个人啊!')
            obj.delete()

        return obj




class TrendUpDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendUpDown
        fields = '__all__'


class AdminTrendUpDownSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = TrendUpDown
        fields = ('user','article',)


class TrendCommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    trendsub_comm = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    touser = UserDetailSerializer()

    class Meta:
        model = TrendComment
        fields = '__all__'

    def get_trendsub_comm(self, obj):
        if obj.trendsub_comm:
            return TrendCommentSerializer(obj.trendsub_comm, many=True).data
        else:
            return None


class AdminTrendCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = TrendComment
        fields = '__all__'
