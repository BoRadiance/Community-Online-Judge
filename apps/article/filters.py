from rest_framework import filters
import django_filters

from .models import Article,Comment

from django.db.models import Q

class ArticleFilter(django_filters.rest_framework.FilterSet):
    """
    文章过滤
    """
    user = django_filters.NumberFilter(method='belong_user_filter')
    tags = django_filters.NumberFilter(method='belong_tag_filter')

    def belong_user_filter(self, queryset, name, value):
        return queryset.filter(Q(user_id=value))

    def belong_tag_filter(self,queryset, name, value):
        return queryset.filter(tags = value)


    class Meta:
        model = Article
        fields = ('user','tags')


class CommentFilter(django_filters.rest_framework.FilterSet):
    """
    评论过滤
    """
    article = django_filters.NumberFilter(method='belong_article_filter')

    def belong_article_filter(self, queryset, name, value):
        return queryset.filter(Q(article_id=value))



    class Meta:
        model = Comment
        fields = ('article',)




