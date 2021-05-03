from django.contrib import admin
from menu.models import menu

# from menu.models import Resturant_menu

# # Register your models here.

# class Resturant_menuAdmin(admin.ModelAdmin):
#     list_display=['number','name','price']


# admin.site.register(Resturant_menu,Resturant_menuAdmin)
admin.site.register(menu)