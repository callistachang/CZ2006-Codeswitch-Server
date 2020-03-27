from .models import Job, UserJob
from skills.models import Skill
from interests.models import Interest
from courses.models import Course
from users.models import ModifiedUser

from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    required_skills = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Skill.objects.all())

    class Meta:
        model = Job
        fields = '__all__'

class UserJobSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=ModifiedUser.objects.all())

    class Meta:
        model = UserJob
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(UserJobSerializer, self).to_representation(instance)
        representation['job'] = JobSerializer(instance.job).data
        return representation