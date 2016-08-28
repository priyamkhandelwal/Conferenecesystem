from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from conference.models import Conference

# Create your models here.

class ProfilePic(models.Model):
	picFile = models.FileField(upload_to='documents',default=None,null=True)

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	usertype = models.CharField(max_length=50,blank=True)
	contactNo = models.CharField(max_length=20)
	pic = models.OneToOneField(ProfilePic,null=True,blank=True)
	regconf = models.ManyToManyField(Conference,blank=True)

	def __str__(self):
		return self.user.first_name
		
