from django.contrib import admin
from django.db import models
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'labor_name', 'project_name', 'price')

    search_fields = ('labor_name',)

    list_filter = ('labor_name', 'project_name','labor_Phone')

    list_per_page = 20

    fieldsets = (
        ['領款人資料',{
            'fields':('labor_name','labor_ID','labor_Phone','labor_ResidentAddress','labor_CurrentAddress',
                        ('labor_bank','labor_bankname','labor_bankaccount',)),
        }],
        ['專案名稱',{    
            'fields': ('project_name','price',),
        }],
        ['身分證',{    
            'fields': ('ID_front','ID_back','bank_cover',),
        }]
    )
   
# Register your models here.
admin.site.register(Post, PostAdmin)