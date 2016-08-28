from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conference(models.Model):
	c_id = models.IntegerField(primary_key=True)
	confname = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	startdate = models.DateField()
	enddate = models.DateField()
	manager = models.OneToOneField(User,on_delete=models.CASCADE)
	editors = models.ManyToManyField(User,related_name='+')
	# confimages = models.ManyToManyField(Images,null=True,blank=True)
	# confpapers = models.ManyToManyField(Papers,null=True,blank=True)

	def __str__(self):
		return self.confname

		
class Images(models.Model):
	imgfile = models.FileField(upload_to='documents',default=None,null=True)
	conference = models.ForeignKey(Conference,on_delete=models.CASCADE,null=True)

class Papers(models.Model):
	pname = models.CharField(max_length=50,default=None,primary_key=True)
	aprooved = models.BooleanField(default=False)
	conference = models.ForeignKey(Conference,on_delete=models.CASCADE,null=True)
	paperfile = models.FileField(upload_to='documents/papers',default=None,null=True)

	def __str__(self):
		return self.pname

class Page(models.Model):
	pagename = models.CharField(max_length=50)
	conference = models.ForeignKey(Conference,on_delete=models.CASCADE,null=True)
	url = models.CharField(max_length=200,blank=False)
	content = models.CharField(max_length=400)
	template = models.CharField(max_length=50,default='conference/base.html')
	ispublished = models.BooleanField(default=True)

	def __str__(self):
		return self.pagename

		
		