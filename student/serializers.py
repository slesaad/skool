from rest_framework import serializers
from student.models import Student
from user.serializers import ProfileSerializer
from user.models import Profile


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__' 
