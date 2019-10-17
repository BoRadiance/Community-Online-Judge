from .models import User,Tag,UserInfoImg
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator




class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfoImg
        fields = ('UserBackgroundImage','UserAvatar',)


class LessUserSerializer(serializers.ModelSerializer):
    image = UserImgSerializer()
    class Meta:
        model = User
        fields = ("id", "username",
                  "AboutMe",
                  "NickName",
                  'image',
                  "SumbitNumber","AcNumber",
                  "Point",
                  )

class UpdateUserDetailSerializer(serializers.ModelSerializer):
    """
       用户详情序列化类
       """

    class Meta:
        model = User
        fields = ("id", "last_login", "username", "first_name",
                  "last_name", "email", "is_active", "is_disabled",
                  "AboutMe", "Motto", "BirthPlace", "BirthDay",
                  "LivesIn", "Gender", "Status", "MyEmail", "QQ",
                  "WeChat", "Hobbies", "FavouriteTvShows", "FavouriteMovies",
                  "FavouriteGames", "FavouriteMusic", "FavouriteBooks",
                  "NickName", "OtherInterests", "OthersAboutMe",
                  "UserState",  "LearnId",
                  )


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化类
    """
    image = UserImgSerializer()
    class Meta:

        model = User
        fields = ("id","last_login","username","first_name",
                  "last_name","email","is_active","is_disabled",
                  "AboutMe","Motto","BirthPlace","BirthDay",
                  "LivesIn","Gender","Status","MyEmail","QQ",
                  "WeChat","Hobbies","FavouriteTvShows","FavouriteMovies",
                  "FavouriteGames","FavouriteMusic","FavouriteBooks",
                  "NickName","OtherInterests","OthersAboutMe",
                  "UserState","Check", "LearnId","SumbitNumber","AcNumber",
                  "Point",
                  "image",)


class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'},required=True,allow_blank=False,help_text="密码", label="密码", write_only=True,
    )



    MyEmail = serializers.CharField(label='邮箱',help_text='请输入有效邮箱,以便用户认证',required=True,
                                    allow_blank=False, validators=[UniqueValidator(queryset=User.objects.filter(Check=True), message="该邮箱已被激活使用")]
                                    )

    class Meta:
        model = User
        fields = ("username", "password","MyEmail")



class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        validators = [
            UniqueTogetherValidator(
                queryset=Tag.objects.all(),
                fields=('user', 'title'),
                message="已存在"
            )
        ]
        fields = ('id','user','title','is_disabled')



class AdminTagSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Tag
        validators = [
            UniqueTogetherValidator(
                queryset=Tag.objects.all(),
                fields=('user', 'title'),
                message="已存在"
            )
        ]
        fields = ('id','user','title','is_disabled')





class UserInfoImgSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    class Meta:
        model = UserInfoImg
        fields = "__all__"


class AdminUserInfoImgSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserInfoImg
        fields = "__all__"
