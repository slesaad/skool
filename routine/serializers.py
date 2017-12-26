from rest_framework import serializers
from routine.models import Routine, Period


class RoutineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routine
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Period
        fields = '__all__'
