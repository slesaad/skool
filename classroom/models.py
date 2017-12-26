from django.db import models
from student.models import Student


class Classroom(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class ClassGroup(models.Model):
    title = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True,
                                      through='GroupMembership')

    def __str__(self):
        return self.title


class GroupMembership(models.Model):
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    roll_no = models.IntegerField()

    def __str__(self):
        return '{} @ {} ({})'.format(
            self.student,
            self.class_group.classroom,
            self.class_group,
        )
