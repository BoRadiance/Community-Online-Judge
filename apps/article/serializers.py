from .models import Article
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import ArticleUpDown,Comment
from user.serializers import TagSerializer,UserDetailSerializer




class ArticleSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    tags = TagSerializer(many=True)
    user = UserDetailSerializer()
    class Meta:
        model = Article
        fields = '__all__'



class AdminArticleSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Article
        fields = ('user','tags','is_disabled','title','content',)



class UpDownSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleUpDown
        fields = '__all__'


class AdminUpDownSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = ArticleUpDown
        fields = ('user','article',)


class CommentSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    sub_comm = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    touser = UserDetailSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

    def get_sub_comm(self,obj):
        if obj.sub_comm:
            return CommentSerializer(obj.sub_comm,many=True).data
        else:
            return None


class AdminCommentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Comment
        fields = '__all__'

