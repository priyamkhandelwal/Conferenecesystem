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
	if not request.user.is_authenticated():
		flag1 = False
		flag2 = False
		cid = request.GET.get('cid')
		conference = Conference.objects.get(c_id=cid)
		editors = conference.editors.all()
		papers = Papers.objects.filter(conference=conference)
		pages = Page.objects.filter(conference=conference)
		return render(request,'conference/conferenc.html',{'conference':conference,'editors':editors,'papers':papers,'pages':pages,'flag1':flag1,'flag2':flag2})
	else:
		cid = request.GET.get('cid')
		conference = Conference.objects.get(c_id=cid)
		editors = conference.editors.all()
		papers = Papers.objects.filter(conference=conference)
		pages = Page.objects.filter(conference=conference)
		user = request.user
		u = UserProfile.objects.get(user=user)
		flag1 = False
		flag2 = False
		regconf = u.regconf.all()
		for r in regconf:
			if r.c_id == int(cid):
				flag1=True
		print flag1
		if request.user.is_authenticated():
			flag2=True
		print flag2
		# print conference.confpapers
		return render(request,'conference/conferenc.html',{'conference':conference,'editors':editors,'papers':papers,'pages':pages,'flag1':flag1,'flag2':flag2})

def conferencepage(request):
	pn = request.GET.get('pn')
	page = Page.objects.get(pagename=pn)
	return render(request,'conference/dynamicpage.html',{'title':page.pagename,'content':page.content,'template':page.template})

def allconf(request):
	confs = Conference.objects.all()
	return render(request,'conference/frontpage.html',{'conferences':confs})

def register(request):
	cid = request.GET.get('cid')
	conference = Conference.objects.get(c_id=cid)
	user = request.user
	u = UserProfile.objects.get(user=user)
	u.regconf.add(conference)
	u.save()
	confs = Conference.objects.all()
	return render(request,'conference/mainpage.html',{'conferences':confs})