from .views import ModifiedUser
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ModifiedUser
        fields = ['id', 'email', 'password', 'url']
