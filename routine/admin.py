from django.contrib import admin
from routine.models import Routine, Period


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    pass


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    pass
