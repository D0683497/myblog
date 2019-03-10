from django.contrib import admin

# Register your models here.
from .models import Post, Tag

class TagInline(admin.StackedInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_date') # 管理員看的
    fields  = ('title', 'text','published_date') # 管理員可修改的
    search_fields = ('title',) #搜尋列
    inlines = [TagInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)