from django.contrib import admin
from django.db import models
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'labor_name', 'project_name', 'price','pay_complete','created_at')

    search_fields = ('labor_name',)

    list_filter = ('labor_name', 'project_name','labor_Phone')

    list_per_page = 20

    fieldsets = (
        ['領款人資料',{
            'fields':('labor_name','labor_ID','labor_email','labor_Phone',('labor_ResidentAddress',),
                        ('labor_bank','labor_bankname','labor_bankaccount','bank_cover',),
                        ('category_choice','member_choice',)
                    ),
        }],
        ['專案名稱',{    
            'fields': ('project_name','price',),
        }],
        ['身分證',{    
            'fields': ('ID_front','ID_back','labor_signature',),
        }],
        ['付款狀態',{    
            'fields': ('pay_complete',),
        }],

        
    )
   
# Register your models here.
admin.site.register(Post, PostAdmin)