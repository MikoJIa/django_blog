from django.contrib import admin
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author',)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'post')