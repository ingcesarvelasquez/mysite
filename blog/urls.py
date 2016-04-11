from django.conf.urls import include, url
from blog import views
#https://docs.djangoproject.com/en/1.8/topics/http/urls/
urlpatterns = [
	url(r'^$', views.post_list),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
]