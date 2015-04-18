from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the home page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/ccbclib/home/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ccbc_library.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ccbclib/',include('ccbclib.urls',namespace='ccbclib')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
)
