from rest_framework import serializers
from .models import CustomUser
import re

class CreateUserSerializer(serializers.ModelSerializer):
    username_regex = r'^[a-zA-Z0-9_]+$'
    password_regex = r'^[a-zA-Z0-9_]+$'

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, username):
        if len(username) > 8 and re.match(self.username_regex, username):
            return username
        else:
            raise serializers.ValidationError('Username should contain at least 8 characters!')

    def validate_email(self, email):
        if '@' in email:
            return email
        else:
            raise serializers.ValidationError('Invalid email address!')

    def validate_password(self, password):
        if len(password) > 8 and re.match(self.password_regex, password):
            return password
        else:
            raise serializers.ValidationError({"password": "Invalid password!"})


    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





