from django.contrib import admin
from .models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('author', 'date_posted')
    extra = 0


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    list_display_links = ('title', 'author')
    search_fields = ('title', 'author',)
    readonly_fields = ('author', 'date_posted')
    list_per_page = 20
    
    inlines = [CommentInline]

admin.site.register(Post, PostsAdmin)
admin.site.register(Comment)
