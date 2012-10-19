from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', direct_to_template, {"template": "homepage.html"}),

    (r'^accounts/signin/$', 'django.contrib.auth.views.login', {'template_name': 'signin.html'}, 'signin'),
    (r'^accounts/signout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/accounts/signin/?signout=True'}, 'signout'),

    (r'^events/', include('events.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
