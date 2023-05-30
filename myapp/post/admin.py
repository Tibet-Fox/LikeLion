from django.contrib import admin
from .models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description','date_created','date_modified','writer')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content_text','content_img','content_file','date_created','date_updated','writer','hits' )
    # search_fields=('title','content_text','content_img','content_file','date_created','date_updated','writer','hits')

class CommentAdmin(admin.ModelAdmin):
   list_display = ('comment','date_created','date_updated','post','writer')

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user','post','date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category','blog')

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('user','neighbor','date_added')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Neighbor, NeighborAdmin)