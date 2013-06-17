from django.conf.urls import patterns, include, url
import v1
from v1 import urls
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os, sys

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^api/', include('api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/', include(v1.urls)),
)
