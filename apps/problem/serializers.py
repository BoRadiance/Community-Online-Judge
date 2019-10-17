from rest_framework import serializers
from .models import ProblemTages,OtherProblem,CodingProlemInfo
from user.serializers import LessUserSerializer
class ProblemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProblemTages
        fields = '__all__'


class CodingProblemSerializer(serializers.ModelSerializer):
    tags = ProblemTagSerializer(many=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    user = LessUserSerializer()
    class Meta:
        model = CodingProlemInfo
        fields = '__all__'


class AdminCodingProblemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = CodingProlemInfo
        fields = ('id','user','title','pro_desc','source','pro_input','pro_output',
                  'sample_input','sample_output','tags','hit','time_limit','spj','memory_limit','degree',
                  'is_disabled')


