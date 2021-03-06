from django.conf.urls.defaults import patterns, include, url
from django.views.generic.date_based import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ephestrus.views.home'),
    url(r'^search/', 'ephestrus.views.search'),
    url(r'^contact/', 'ephestrus.views.contact'),
    # url(r'^ephestrus/', include('ephestrus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^blog/', include('ephestrus.blog.urls')),
)
