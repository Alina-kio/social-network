from .models import Post, UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class AuthValidateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=5, max_length=100)
    password = serializers.CharField(min_length=1)


class RegistrationValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('User already exists')
        return username


class UserListSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UserProfile
        fields = ['user', 'name']


class ProfileSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=UserProfile
        # fields = '__all__'
        fields = ['id', 'name', 'birthday', 'phone', 'lives_in', 'profile_image']



class PostSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = ['id', 'user', 'name', 'datetime', 'image', 'text', 'likes']


class SearchSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = User
        fields = ['id', 'user']

