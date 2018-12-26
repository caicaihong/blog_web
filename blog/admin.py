from django.contrib import admin
from .models import BlogArticles
# Register your models here.
admin.site.site_header = "Blog manager system"
admin.site.site_title = "Blog"
class BlogArticlesAdmin(admin.ModelAdmin):
	"""docstring for BlogArticlesAdmin"""
	list_display = ("title","author","publish","body")
	list_filter = ("publish","author")
	search_fields = ("title","body")
	raw_id_fields = ("author",)
	# date_hierarchy = "publish"
	ordering = ["publish","author"]
admin.site.register(BlogArticles,BlogArticlesAdmin)


		