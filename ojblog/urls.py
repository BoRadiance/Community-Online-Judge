"""ojblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include,re_path
import xadmin
# 为了后台可以访问到meida里面的图片
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from .settings import MEDIA_ROOT,STATIC_ROOT
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from user.views import UserViewset,ShowUserViewSet,TagViewSet,AdminTagViewSet
from user.views import AdminUserInfoImgViewSet,UserInfoImgViewSet
from photo.views import PhotosViewSet,AdminPhotosViewSet
from photo.views import PhotoDetailViewSet,AdminPhotoDetailViewSet
from video.views import VideoViewSet,AdminViedoViewSet
from article.views import ArticleViewSet,AdminArticleViewSet
from article.views import CommentViewSet,AdminCommentViewSet
from article.views import ArticleUpDownViewSet,AdminArticleUpDownViewSet
from article.views import upload_file
from user.views import  ActiveView
from announcement.views import DaySen




router = DefaultRouter()
"""
社区路由
"""
router.register(r'users',UserViewset,base_name='users')
router.register(r'visitor',ShowUserViewSet,base_name='visitor')
router.register(r'tags',TagViewSet,base_name='tags')
router.register(r'admintags',AdminTagViewSet,base_name='admintags')
router.register(r'userinfoimg',UserInfoImgViewSet,base_name='userinfoimg')
router.register(r'adminuserinfoimg',AdminUserInfoImgViewSet,base_name='adminuserinfoimg')
router.register(r'photos',PhotosViewSet,base_name='photos')
router.register(r'adminphotos',AdminPhotosViewSet,base_name='adminphotos')
router.register(r'photodetail',PhotoDetailViewSet,base_name='photodetail')
router.register(r'adminphotodetail',AdminPhotoDetailViewSet,base_name='adminphotodetail')
router.register(r'video',VideoViewSet,base_name='video')
router.register(r'adminvideo',AdminViedoViewSet,base_name='adminvideo')
router.register(r'article',ArticleViewSet,base_name='article')
router.register(r'adminarticle',AdminArticleViewSet,base_name='adminarticle')
router.register(r'adminupdown',AdminArticleUpDownViewSet,base_name='adminupdown')
router.register(r'comment',CommentViewSet,base_name='comment')
router.register(r'admincomment',AdminCommentViewSet,base_name='admincomment')

from trend.views import TrendClassViewSet,TrendViewSet,AdminTrendViewSet
from trend.views import TrendPhotoViewSet,AdminTrendPhotoViewSet
from trend.views import AdminTrendUpDownViewSet,TrendCommentViewSet,AdminTrendCommentViewSet


router.register(r'trendtag',TrendClassViewSet,base_name='trendtag')
router.register(r'trend',TrendViewSet,base_name='trend')
router.register(r'admintrend',AdminTrendViewSet,base_name='admintrend')
router.register(r'admintrendphoto',AdminTrendPhotoViewSet,base_name='admintrendphoto')
router.register(r'admintrendupdown',AdminTrendUpDownViewSet,base_name='admintrendupdown')
router.register(r'trendcomment',TrendCommentViewSet,base_name='trendcomment')
router.register(r'admintrendcomment',AdminTrendCommentViewSet,base_name='admintrendcomment')





"""
OJ 路由
"""
from announcement.views import AnnViewSet,OJCarViewSet,BlogCarViewSet
router.register(r'announcement',AnnViewSet,base_name='announcement')
router.register(r'ojcarousel',OJCarViewSet,base_name='ojcarousel')
router.register(r'blogcarousel',BlogCarViewSet,base_name='blogcarousel')

from problem.views import ProblemTagViewSet,CodingProblemViewSet, AdminCodingProblemViewSet
router.register(r'problemtag',ProblemTagViewSet,base_name='problemtag')
router.register(r'codingproblem',CodingProblemViewSet,base_name='codingproblem')
router.register(r'admincodingproblem',AdminCodingProblemViewSet,base_name='admincodingproblem')






urlpatterns = [
    path('xadmin/',xadmin.site.urls),

    # restframe登录的路由
    path('api-auth/', include('rest_framework.urls')),

    path('ueditor/', include('DjangoUeditor.urls')),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$',serve,{'document_root': STATIC_ROOT}),

    path('docs/', include_docs_urls(title="南理社区api")),

    # jwt 的token 认证接口
    path('login/', obtain_jwt_token),

    path('uploadfile/',upload_file),

    # 邮箱验证接口
    re_path('activeuser/(?P<token>.*)',ActiveView.as_view(),name='activeuser'),

    path('',include(router.urls)),

    # 每日一句
    path('daysen/',DaySen.as_view(),name='daysen'),


]
