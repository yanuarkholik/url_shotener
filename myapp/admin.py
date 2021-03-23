from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from .models import Profile, URLs
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  
    list_display = ('user','buat', 'id')
    ordering = ('-buat',)
    search_fields = []

@admin.register(URLs)
class DataURL(admin.ModelAdmin):  
    list_display = ('url', 'id')
    ordering = ('-id',)
    search_fields = []
