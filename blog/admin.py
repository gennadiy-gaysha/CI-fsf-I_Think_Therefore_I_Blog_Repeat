from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    def publish_post(self, request, queryset):
        queryset.update(status=1)
    publish_post.short_description = 'Publish Me!'

    summernote_fields = ('content')
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    actions = [publish_post]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    def approve_comments(self, request, queryset):
        queryset.update(status=True)
    approve_comments.short_description = "Approve me please!"

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    # We inform our ModelAdmin of the action:
    actions=[approve_comments]

