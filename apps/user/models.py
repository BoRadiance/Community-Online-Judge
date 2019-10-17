from django.db import models
from base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from utils.SomeSetting import LiterDocStorage


class User(AbstractUser,BaseModel):
    """
    用户
    """

    # 社区相关

    AboutMe = models.TextField(max_length=1024,null=True,blank=True,
                               verbose_name='关于我',default='这个人很懒,什么都没有写')

    Motto = models.TextField(max_length=1024,null=True,blank=True,
                               verbose_name='座右铭',default='没有座右铭')

    BirthPlace = models.CharField(max_length=526,null=True,blank=True,
                                  verbose_name='出生地',default='江西')
    BirthDay =models.CharField(max_length=256,null=True,blank=True,verbose_name='生日',default='1998.4.2')


    LivesIn = models.CharField(max_length=526,null=True,blank=True,
                               verbose_name='居住地',default='xx栋')

    Gender = models.CharField(max_length=526,null=True,blank=True,
                              verbose_name='性别',default='保密')

    Status = models.CharField(max_length=526,null=True,blank=True,
                              verbose_name='状态',default='单身')

    MyEmail = models.CharField(max_length=526,null=True,blank=True,
                              verbose_name='邮箱',default='xx@163.com')

    QQ =  models.CharField(max_length=526,null=True,blank=True,
                              verbose_name='QQ',default='189219902')

    WeChat =  models.CharField(max_length=526,null=True,blank=True,
                              verbose_name='微信',default='Youyixin9842')


    Hobbies =  models.TextField(max_length=1024,null=True,blank=True,
                               verbose_name='爱好',default='打羽毛球,编程')

    FavouriteTvShows = models.TextField(max_length=1024, null=True, blank=True,
                               verbose_name='最喜欢的网剧', default='法医秦明,心理罪,无罪之证')

    FavouriteMovies = models.TextField(max_length=1024, null=True, blank=True,
                                        verbose_name='最喜欢的电影', default='心理罪之城市之光')

    FavouriteGames = models.TextField(max_length=1024, null=True, blank=True,
                                       verbose_name='最喜欢的游戏', default='王者荣耀,英雄联盟')

    FavouriteMusic =  models.TextField(max_length=1024, null=True, blank=True,
                                       verbose_name='最喜欢的歌曲', default='画,我会很诚实')

    FavouriteBooks = models.TextField(max_length=1024, null=True, blank=True,
                                      verbose_name='最喜欢的书籍', default='围城,皮囊,活着')

    NickName = models.TextField(max_length=256, null=True, blank=True,
                                      verbose_name='昵称', default='该用户没有设置昵称')

    OtherInterests = models.TextField(max_length=1024, null=True, blank=True,
                                      verbose_name='其他爱好', default='...')

    OthersAboutMe = models.TextField(max_length=1024, null=True, blank=True,
                                      verbose_name='其他关于我的信息', default='巴拉巴拉巴拉...')

    ChannelsName = models.TextField(max_length=1024,null=True,blank=True,verbose_name='最新的channels通道名')

    User_State = (
        (1,'在线'),
        (2,'离线(勿扰)'),
    )


    UserState = models.IntegerField(choices=User_State,default=2,
                                    verbose_name='在线状态',null=True)

    Check = models.BooleanField(default=False,verbose_name='验证通过',null=True,blank=True)


    # oj相关
    LearnId = models.CharField(default='1601020301', verbose_name='学号',max_length=100)
    SumbitNumber = models.IntegerField(default=0, verbose_name='提交数')
    AcNumber = models.IntegerField(default=0,verbose_name='AC数')

    Point = models.IntegerField(default=0,verbose_name='贡献分')



    def AcAdd(self):
        self.AcNumber = self.AcNumber+1

    def SumbitAdd(self):
        self.SumbitNumber = self.SumbitNumber+ 1

    def PointAdd(self):
        self.Point = self.Point+ 1

    def GetChannelsName(self):
        return self.ChannelsName

    def __str__(self):
        return  self.username

    class Meta:
        verbose_name='用户'
        verbose_name_plural = verbose_name



class UserInfoImg(BaseModel):
    """
    用户的头像和封面图
    """
    UserBackgroundImage = models.ImageField(upload_to="user/", null=True,
                                            blank=True, verbose_name="个人背景图",
                                            default='user/defaultback.jpg')

    UserAvatar = models.ImageField(upload_to="user/", null=True,
                                   blank=True, verbose_name="头像",
                                   default='user/defaultavatar.jpg',storage=LiterDocStorage())

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='image')


    class Meta:
        verbose_name = '用户头像和封面图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user)



class Tag(BaseModel):
    """
    标签
    """
    title =  models.CharField(max_length=100)  # 标签名
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)+self.title


    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name
        unique_together = ("user", "title")

