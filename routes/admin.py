from django.contrib import admin
from routes.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("image", "title", "desc", "publish", "author")
    search_fields = ["image", "title"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created', 'status')
#    list_filter = ('active', 'created', 'updated')
#    search_fields = ('name', 'body')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)