from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^account/logout', 'profiles.views.logoutUser'),
    url(r'^account', 'profiles.views.account'),
    url(r'^register/$', 'profiles.views.register', name='register'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<slug>\w+)/$', 'profiles.views.profile' ),
#    url(r'^login','profiles.views.login', name='logout'),
    # url(r'^ProfileApplication/', include('ProfileApplication.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
