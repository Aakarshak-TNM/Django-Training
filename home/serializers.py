from rest_framework import serializers
from .models import Student, Standard


class StudentModelSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class StudentModelSerializer(serializers.ModelSerializer):
    standard_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def get_standard_name(self, obj):
        if obj.standard_name:
            return obj.standard_name.standard_name
        return None


class StandardModelSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Standard
        fields = '__all__'