from rest_framework import viewsets
from student.models import Student
from student.serializers import StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
