from django.contrib import admin
from .models import Category, Tag, Post, Comment
from pages.admin import ActionPublish

class CategoryAdmin(ActionPublish):
    '''Категории блога'''
    list_display = ('id', 'name', 'parent', 'slug', 'sort', 'paginated', 'published')
    actions = ['unpublish', 'publish']
    list_display_links = ('name',)
    list_filter = ('parent', )
    

class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1
    

class PostAdmin(ActionPublish):
    '''Посты блога'''
    inlines = [CommentsInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

admin.site.site_header = 'test'
admin.site.site_title = 'test'