from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^blog/$', views.index, name='index'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.article, name='article'),
    url(r'^blog/article/(?P<article_id>\d+)/addcomment$', views.addcomment, name='addcomment'),
    url(r'^blog/article/(?P<article_id>\d+)/changecomment/(?P<comment_id>\d+)$', views.changecomment, name='changecomment'),
    url(r'^blog/article/(?P<article_id>\d+)/deletecomment/(?P<comment_id>\d+)$', views.deletecomment, name='deletecomment'),
    url(r'^blog/article/addlike/(?P<article_id>\d+)$', views.addlike, name='addlike'),
    url(r'^page/(\d+)/$', views.index, name='page'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)