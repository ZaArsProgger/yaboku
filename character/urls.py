from django.conf.urls import url
from . import views


appname='character'
urlpatterns = [
#    url(r'^$', views.index, name='index'),
    url(r'^(?P<character_id>[0-9])+/$', views.detail, name='detail'),
]
