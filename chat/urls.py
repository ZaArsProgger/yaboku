from django.conf.urls import url
from . import views

app_name='chat'
urlpatterns = [
    url(r'^(?P<page>[0-9]+)/$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^send/', views.sendMessage, name='send'),
]
