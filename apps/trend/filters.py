from rest_framework import filters
import django_filters
from .models import Trend,TrendComment,TrendPhoto

class TrendFilter(django_filters.rest_framework.FilterSet):
    """
    动态过滤
    """
    user = django_filters.NumberFilter(method='belong_user_filter')
    tags = django_filters.NumberFilter(method='belong_tag_filter')
    is_disabled = django_filters.NumberFilter(method='belong_disable_filter')

    def belong_disable_filter(self, queryset, name, value):
        return queryset.filter(is_disabled = value)


    def belong_user_filter(self, queryset, name, value):
        return queryset.filter(user_id=value)

    def belong_tag_filter(self, queryset, name, value):
        return queryset.filter(tags=value)

    class Meta:
        model = Trend
        fields = ('user', 'tags')

class TrendPhotoFilter(django_filters.rest_framework.FilterSet):
    """
    动态图片过滤
    """
    article = django_filters.NumberFilter(method='belong_articlea_filter')

    def belong_articlea_filter(self,queryset,name,value):
        return queryset.filter(article_id=value)

    class Meta:
        model = TrendPhoto
        fields = ('article',)



class TrendCommentFilter(django_filters.rest_framework.FilterSet):
    """
    评论过滤
    """
    article = django_filters.NumberFilter(method='belong_article_filter')

    def belong_article_filter(self, queryset, name, value):
        return queryset.filter(article_id=value)

    class Meta:
        model = TrendComment
        fields = ('article',)