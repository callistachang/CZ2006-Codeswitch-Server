from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .models import ModifiedUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = ModifiedUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer