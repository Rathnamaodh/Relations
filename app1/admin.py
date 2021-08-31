from django.contrib import admin
from app1.models import Menu,Item

# Register your models here.

class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','age']

class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['id','menu','name','description']

admin.site.register(Menu,MenuModelAdmin)
admin.site.register(Item,ItemModelAdmin)

