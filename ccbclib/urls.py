from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ccbclib import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$',views.about, name='about'),
        )

urlpatterns += staticfiles_urlpatterns()