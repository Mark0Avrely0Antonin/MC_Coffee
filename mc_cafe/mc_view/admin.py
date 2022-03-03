from django.contrib import admin
from .models import Category_Coffee, Category_Dilikates, MC_Coffee, MC_Dilikates
# Register your models here.

admin.site.register(MC_Coffee)
admin.site.register(Category_Coffee)
admin.site.register(MC_Dilikates)
admin.site.register(Category_Dilikates)
