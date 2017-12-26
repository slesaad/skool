from django.db import models
from teacher.models import Teacher
from classroom.models import Classroom, ClassGroup


class Routine(models.Model):
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return 'Routine for {}'.format(self.classroom)


class Period(models.Model):

    DAYS = (
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    )

    subject = models.CharField(max_length=200)
    teachers = models.ManyToManyField(Teacher, blank=True)
    groups = models.ManyToManyField(ClassGroup, blank=True)
    day = models.CharField(max_length=10, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '{}, {}'.format(
            self.day,
            self.subject,
        )
