from rest_framework import serializers

from .models import ModifiedUser
from skills.serializers import SkillSerializer
from skills.models import Skill

class UserSerializer(serializers.HyperlinkedModelSerializer):
    skills = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Skill.objects.all())
    
    class Meta:
        model = ModifiedUser
        fields = ['id', 'email', 'password', 'skills', 'interests', 'location', 'url']
