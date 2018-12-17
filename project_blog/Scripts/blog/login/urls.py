from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    url(r'^auth/register', views.register, name='register'),
    url(r'^auth/login$', views.enter, name='enter'),
    url(r'^auth/logout$', views.logout, name='logout'),
]