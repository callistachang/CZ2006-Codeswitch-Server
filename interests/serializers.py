from rest_framework import serializers

from .models import Interest

class InterestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'name', 'url']
