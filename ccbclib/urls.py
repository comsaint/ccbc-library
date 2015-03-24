from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ccbclib import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$',views.about, name='about'),
        url(r'^home/$',views.home, name='home'),
        url(r'^borrow/$',views.bookborrow,name='borrow'),
        url(r'^return/$',views.bookreturn,name='return'),
        url(r'^renew/$',views.bookrenew,name='renew'),
        url(r'^success/$',views.success,name='success'),
        url(r'^infotable/(?P<dataToDisplay>\w+)/$',views.infotable,name='infotable'),
        #url(r'^return/(?P<idTransaction>\d+)/$',views.bookreturn,name='return'),
        )

urlpatterns += staticfiles_urlpatterns()