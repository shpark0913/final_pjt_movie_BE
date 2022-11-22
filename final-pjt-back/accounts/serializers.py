from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    # genres = serializers.TextField(source='')
    class Meta:
        model = User
        fields = ('id', 'username',)