from .models import Job, UserJob
from skills.models import Skill
from interests.models import Interest
from courses.models import Course
from users.models import ModifiedUser

from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    recommended_courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    required_skills = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Skill.objects.all())
    interest_fields = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Interest.objects.all())

    class Meta:
        model = Job
        fields = '__all__'

class UserJobSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=ModifiedUser.objects.all())
    job = serializers.PrimaryKeyRelatedField(queryset=Job.objects.all())

    class Meta:
        model = UserJob
        fields = '__all__'