from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'index', name="index"),
    url(r'^(?P<poll_id>\d+)/$', 'detail', name="detail"),
    url(r'^(?P<poll_id>\d+)/results/$', 'results', name="results"),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name="vote"),
)