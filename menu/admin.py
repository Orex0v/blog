from django.contrib import admin
from .models import Menu, MenuItem
from mptt.admin import MPTTModelAdmin

@admin.register(Menu)
class  MenuAdmin(admin.ModelAdmin):
    '''Меню'''
    list_display = ('name', 'status', 'published')
    list_filter = ('published',)
    
@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    '''Пунты меню'''
    list_display = ('title', 'name', 'parent', 'menu', 'sort', 'id', 'published', 'object_id')
    list_filter = ('menu', 'parent', 'published')    
    search_fields = ('name', 'parent__name', 'menu__name')
    save_as = True
    list_editable = ('sort', )
    mptt_level_indent = 20
    
