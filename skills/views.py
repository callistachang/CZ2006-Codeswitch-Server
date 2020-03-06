from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action

import re

from utils import get_or_none

from .models import Skill
from .serializers import SkillSerializer

class SkillViewSet(viewsets.ModelViewSet):
    """API endpoints pertaining to skills.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer