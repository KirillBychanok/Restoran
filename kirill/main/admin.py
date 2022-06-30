from django.contrib import admin
from .models import FeedBack, DishCategory, Dish, Portfolio

# Register your models here.

class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'price')
    ordering = ('cat', 'price')

admin.site.register(FeedBack)
admin.site.register(DishCategory, DishCategoryAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Portfolio)