from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'labor_name', 'project_name', 'price')

# Register your models here.
admin.site.register(Post, PostAdmin)