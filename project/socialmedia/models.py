from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length = 20,
        choices = options,
        default = 'other',
        null=False,
        blank=False
        )
    birthday = models.DateField(null=True,blank=True,default=None)
    phone = models.CharField(max_length=20,null=True,blank=True)
    lives_in = models.CharField(max_length=200,null=True,blank=True)
    profile_image = models.ImageField(upload_to="profile_image",null=True,blank=True)


    def __str__(self):
        return self.user.username
    


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    text = models.CharField(max_length=1000, null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.user.username