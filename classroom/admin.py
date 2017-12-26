from django.contrib import admin
from classroom.models import Classroom, ClassGroup, GroupMembership


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassGroup)
class ClassGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(GroupMembership)
class GroupMembershipAdmin(admin.ModelAdmin):
    pass
