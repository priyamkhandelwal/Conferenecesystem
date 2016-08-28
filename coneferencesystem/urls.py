from django.conf.urls import include,url
from django.conf import settings
from django.contrib import admin
from conference import views
admin.autodiscover()

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^login/',include('userlogin.urls',namespace='userlogin')),
    url(r'^admin/', admin.site.urls),
    url(r'^conference/',include('conference.urls',namespace='conference')),
]
