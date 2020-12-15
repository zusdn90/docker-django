from django.conf import settings

from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField(read_only=True, required=False)
    email = serializers.EmailField(required=False, allow_null=True, allow_blank=True)    
    

    class Meta:
        model = User
        fields = ["id", "username", "email",]

class AuthSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    username = serializers.CharField(read_only=True, required=False)
    email = serializers.CharField(read_only=True, required=False)
    
    class Meta:
        model = User     
        fields = ["id", "username", "email",]
