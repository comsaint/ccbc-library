from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ccbclib import views

urlpatterns = patterns('',
        #url(r'^$', views.index, name='index'),
        url(r'^about/$',views.about, name='about'),
        url(r'^home/$',views.home, name='home'),
        url(r'^borrow/$',views.bookborrow,name='borrow'),
        url(r'^return/$',views.bookreturn,name='return'),
        url(r'^renew/$',views.bookrenew,name='renew'),
        url(r'^success/$',views.success,name='success'),
        url(r'^infotable/(?P<dataToDisplay>\w+)/$',views.infotable,name='infotable'),
        #url(r'^book/add/$', views.BookCreate.as_view(),name='book_add'),
        #url(r'book/(?P<pk>[0-9]+)/$', views.BookUpdate.as_view(),name='book_update'),
        #url(r'book/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(),name='book_delete'),
        url(r'^borrower/$', views.BorrowerListView.as_view(),name='borrower_list'),
        url(r'^borrower/add/$', views.BorrowerCreate.as_view(),name='borrower_add'),
        url(r'^borrower/(?P<pk>[0-9]+)/$', views.BorrowerUpdate.as_view(),name='borrower_update'),
        )

urlpatterns += staticfiles_urlpatterns()