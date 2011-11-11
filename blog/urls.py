from django.conf.urls.defaults import patterns, include, url
from ephestrus.blog.models import Post
from ephestrus.blog.views import *
from django.views.generic.date_based import *

info_dict = {
	'queryset': Post.objects.filter(published=True),
	'date_field': 'pub_date',
	'extra_context': {'recent': Post.objects.filter(published=True)}
}

urlpatterns = patterns('',
	url(r'^$', home, dict(info_dict, template_name='blog/list.html')),
	url(r'^(?P<year>\d{4})/$', archive_year, dict(info_dict, make_object_list=True, template_name='blog/list.html')),
	url(r'^(?P<year>\d{4}/(?P<month>[a-z]{3}/$', archive_month, dict(info_dict, template_name="blog/list.html")),
	url(r'^(?P<year>\d{4}/(?P<month>[a-z]{3}/(?P<day>\d{2})/$', archive_day, dict(info_dict, template_name="blog/list.html")),
	url(r'^(?P<year>\d{4}/(?P<month>[a-z]{3}/(?<day>\d{2})/(?P<slug>[-\w]+)/$', object_detail, dict(info_dict, template_name='blog/detail.html')),
)
