from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from markupfield.fields import MarkupField

class Post(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField('Date published')
	author = models.ForeignKey(User)
	entry = MarkupField(default_markup_type='markdown')
	slug = models.SlugField(
		unique_for_date='pub_date',
		help_text='Automatically built from the Title'
	)
	tags = TaggableManager()
	published = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('-pub_date',)
		get_latest_by = 'pub_date'
		verbose_name_plural = 'posts'
		
	def __unicode__(self):
		return u'%s' % (self.title)
		
	def get_absolute_url(self):
		return "http://ephestr.us/blog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
