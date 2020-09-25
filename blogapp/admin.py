from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','status','created_at')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    
    
admin.site.register(Blog, BlogAdmin)
