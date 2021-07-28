from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/v1/user/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/v1/comment/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/v1/user/(?P<pk>[0-9]+)/comment/$', views.tutorial_detail),
    url(r'^api/v1/user/(?P<pk>[0-9]+)/comment$', views.tutorial_detail),
    url(r'^api/v1/user/([0-9])/comment/([0-9])$', views.tutorial_detail)

]