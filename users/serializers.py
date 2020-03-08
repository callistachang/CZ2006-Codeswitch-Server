from .views import ModifiedUser
from rest_framework import serializers
from skills.serializers import SkillSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = ModifiedUser
        fields = ['id', 'email', 'password', 'url', 'skills']
