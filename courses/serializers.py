from rest_framework import serializers

from .models import Course
from skills.models import Skill

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    skills_taught = serializers.SlugRelatedField(many=True, slug_field="name", queryset=Skill.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'title', 'organizer', 'description', 'price', 'date_posted', 'course_src', 'picture_src', 'skills_taught', 'url']
