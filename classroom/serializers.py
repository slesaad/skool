from classroom.models import Classroom, ClassGroup, GroupMembership
from rest_framework import serializers


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = '__all__'


class ClassGrouupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassGroup
        fields = '__all__'


class GroupMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupMembership
        fields = '__all__'
