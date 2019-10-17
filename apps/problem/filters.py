from rest_framework import filters
import django_filters

from .models import ProblemTages,CodingProlemInfo,OtherProblem

from django.db.models import Q

class ProblemTagFilter(django_filters.rest_framework.FilterSet):
    """
    问题标签过滤
    """
    is_hot = django_filters.NumberFilter(method='hot_filter')
    def hot_filter(self, queryset, name, value):
        return queryset.filter(is_hot = value)

    class Meta:
        model = ProblemTages
        fields = ('is_hot',)


class CodingProblemFilter(django_filters.rest_framework.FilterSet):
    """
    问题过滤
    """
    tags = django_filters.NumberFilter(method='belong_tag_filter')
    degree = django_filters.NumberFilter(method='belong_degree_filter')

    def belong_tag_filter(self, queryset, name, value):
        return queryset.filter(tags=value)

    def belong_degree_filter(self,queryset, name, value):
        return queryset.filter(degree=value)

    class Meta:
        model = CodingProlemInfo
        fields = ('tags',)