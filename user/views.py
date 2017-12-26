from rest_framework import viewsets

from user.serializers import ProfileSerializer
from user.models import Profile


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
