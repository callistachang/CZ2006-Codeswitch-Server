from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action

import re

from utils import get_or_none

from .models import Course
from .serializers import CourseSerializer

# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to interests.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer