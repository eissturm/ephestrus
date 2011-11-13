from django.contrib import admin
from ephestrus.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'published')
	search_field = ['title', 'entry']
	list_filter = ('pub_date', 'published')
	prepopulated_fields = {"slug": ("title",)}
	class Media:
			js = (
				'/js/tiny_mce/tiny_mce.js',
				'/js/admin_pages.js'
			)
	
admin.site.register(Post, PostAdmin)
