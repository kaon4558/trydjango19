from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostAdmin(admin.ModelAdmin):
	class Meta:
		model = Post
admin.site.register(Post, PostAdmin)

