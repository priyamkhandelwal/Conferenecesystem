from django.conf.urls import url
from . import views

app_name='userlogin'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signin/$',views.signin,name='signin'),
    url(r'^signout/$',views.signout,name='signout'),
]
