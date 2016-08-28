from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User,UserManager,AbstractBaseUser
from django.contrib.auth import authenticate,login,logout
from .models import Conference,Papers,Page
from userlogin.models import UserProfile

# Create your views here.

def index(request):
	confs = Conference.objects.all()
	return render(request,'conference/mainpage.html',{'conferences':confs})

def upload(request):
	# print request.FILES
	papername = request.POST['papername']
	file = request.FILES['paperfile']
	obj = Papers(pname=papername,paperfile=file)
	obj.save()
	confs = Conference.objects.all()
	return render(request,'conference/mainpage.html',{'conferences':confs})

def show(request):
	user = request.user
	u = UserProfile.objects.get(user=user)
	contact = u.contactNo
	return render(request,'conference/prac.html',{'user':user,'contact':contact})

def viewconference(request):
	cid = request.GET.get('cid')
	conference = Conference.objects.get(c_id=cid)
	editors = conference.editors.all()
	papers = Papers.objects.filter(conference=conference)
	pages = Page.objects.filter(conference=conference)
	# print conference.confpapers
	return render(request,'conference/conferenc.html',{'conference':conference,'editors':editors,'papers':papers,'pages':pages})

def conferencepage(request):
	pn = request.GET.get('pn')
	page = Page.objects.get(pagename=pn)
	return render(request,'conference/dynamicpage.html',{'title':page.pagename,'content':page.content,'template':page.template})
