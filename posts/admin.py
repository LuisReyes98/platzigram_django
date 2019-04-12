from django.contrib import admin

# Register your models here.
from posts.models import Post

admin.site.register(Post)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):

