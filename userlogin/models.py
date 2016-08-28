from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfilePic(models.Model):
	picFile = models.FileField(upload_to='documents',default=None,null=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	usertype = models.CharField(max_length=50)
	contactNo = models.CharField(max_length=20)
	pic = models.OneToOneField(ProfilePic,null=True)

	def __str__(self):
		return self.user.first_name
		
