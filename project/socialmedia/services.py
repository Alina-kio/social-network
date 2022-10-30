from .models import *
from django.contrib.auth.models import User


def get_userprofile():
    return UserProfile.objects.all()


def get_user():
    return User.objects.all()


def get_post():
    return Post.objects.all()



