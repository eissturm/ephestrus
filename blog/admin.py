from django.contrib import admin
from ephestrus.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'published')
	search_field = ['title', 'entry']
	list_filter = ('pub_date', 'published')
	prepopulated_fields = {"slug": ("title",)}
	
admin.site.register(Post, PostAdmin)
