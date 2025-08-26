from django.contrib import admin

# Register your models here.
from .models import Menu,MenuCategory,Dietary,Item,Order

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Item)
admin.site.register(Dietary)
admin.site.register(Order)