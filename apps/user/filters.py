from rest_framework import filters
import django_filters
from .models import User,Tag
from django.db.models import Q
class TagFilter(django_filters.rest_framework.FilterSet):
    """
    用户标签过滤类
    """
    user = django_filters.NumberFilter(method='belong_user_filter')


    def belong_user_filter(self, queryset, name, value):
        return queryset.filter(Q(user_id=value))

    class Meta:
        model = Tag
        fields = ('user',)



