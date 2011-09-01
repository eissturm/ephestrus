from django.conf.urls.defaults import patterns, include, url
from ephestrus.blog.models import Post
from django.views.generic.date_based import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


life_dict = {
	'queryset': Post.objects.filter(section='life',published=True),
	'date_field': 'pub_date',
	'extra_context': {'recent': Post.objects.filter(published=True)}
}
web_dict = {
	'queryset': Post.objects.filter(section='web',published=True),
	'date_field': 'pub_date',
	'extra_context': {'recent': Post.objects.filter(published=True)}
}
tech_dict = {
	'queryset': Post.objects.filter(section='tech',published=True),
	'date_field': 'pub_date',
	'extra_context': {'recent': Post.objects.filter(published=True)}
}
info_dict = {
	'queryset': Post.objects.filter(published=True),
	'date_field': 'pub_date',
	'extra_context': {
		'recent': Post.objects.filter(published=True),
	}
}

urlpatterns = patterns('',
    # Examples:
    url(r'^$', archive_index, dict(info_dict, template_object_name='object_list', template_name='blog/list.html')),
    # url(r'^ephestrus/', include('ephestrus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^web/$', archive_index, dict(web_dict, template_object_name='object_list', template_name='blog/list.html')),
	url(r'^web/(?P<year>\d{4})/$', archive_year, dict(web_dict, make_object_list=True, template_name='blog/list.html')),
	url(r'^web/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', archive_month, dict(web_dict, template_name='blog/list.html')),
	url(r'^web/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/$', archive_day, dict(web_dict, template_name='blog/list.html')),
	url(r'^web/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, dict(web_dict, template_name='blog/detail.html')),
	url(r'^tech/$', archive_index, dict(tech_dict, template_object_name='object_list', template_name='blog/list.html')),
	url(r'^tech/(?P<year>\d{4})/$', archive_year, dict(tech_dict, make_object_list=True, template_name='blog/list.html')),
	url(r'^tech/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', archive_month, dict(tech_dict, template_name='blog/list.html')),
	url(r'^tech/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/$', archive_day, dict(tech_dict, template_name='blog/list.html')),
	url(r'^tech/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, dict(tech_dict, template_name='blog/detail.html')),
	url(r'^life/$', archive_index, dict(life_dict, template_object_name='object_list', template_name='blog/list.html')),
	url(r'^life/(?P<year>\d{4})/$', archive_year, dict(life_dict, make_object_list=True, template_name='blog/list.html')),
	url(r'^life/(?P<year>\d{4})/(?P<month>[a-z]{3})/$', archive_month, dict(life_dict, template_name='blog/list.html')),
	url(r'^life/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/$', archive_day, dict(life_dict, template_name='blog/list.html')),
	url(r'^life/(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, dict(life_dict, template_name='blog/detail.html')),
)
