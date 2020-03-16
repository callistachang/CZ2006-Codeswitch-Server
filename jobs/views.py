from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action

import re

from utils import get_or_none

from .models import Job, UserJob
from .serializers import JobSerializer, UserJobSerializer

class JobViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to jobs.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class UserJobViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to user-jobs.
    """
    queryset = UserJob.objects.all()
    serializer_class = UserJobSerializer