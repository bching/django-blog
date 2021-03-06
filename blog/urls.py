from django.conf.urls import url, include
from . import views
# from django.urls import include

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^about/$', views.about_me, name='about_me'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url('', include('contact.urls')),
]
