from django.conf.urls.defaults import patterns, include, url
from ephestrus.blog.models import Post
from django.views.generic.date_based import *

info_dict = {
	'queryset': Post.objects.filter(published=True),
	'date_field': 'pub_date',
}

urlpatterns = patterns('',
	url(r'^$', archive_index, dict(info_dict, template_name='blog/list.html')),
)
