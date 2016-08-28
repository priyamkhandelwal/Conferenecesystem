from django.conf.urls import url
from . import views

app_name='conference'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^show/$',views.show,name='show'),
    url(r'^viewconference/$',views.viewconference,name='viewconference'),
    url(r'^conferencepage/$',views.conferencepage,name='conferencepage'),
]
