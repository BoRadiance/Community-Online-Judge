from rest_framework import filters
import django_filters

from .models import Photos,PhotoDetail

from django.db.models import Q

class PhotosFilter(django_filters.rest_framework.FilterSet):
    """
    相册过滤类
    """
    user = django_filters.NumberFilter(method='belong_user_filter')

    def belong_user_filter(self, queryset, name, value):
        return queryset.filter(Q(user_id=value))

    class Meta:
        model = Photos
        fields = ('user',)

class PhotoDetailFilter(django_filters.rest_framework.FilterSet):
    """
    照片过滤类
    """
    belong = django_filters.NumberFilter(method='belong_photo_filter')

    def belong_photo_filter(self,queryset,name,value):
        return queryset.filter(Belong_id=value)

    class Meta:
        model = PhotoDetail
        fields=('belong',)
