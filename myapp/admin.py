from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter

from .models import Profile, URLs, CustomURLs
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):  
    list_display = ('user','buat', 'id')
    ordering = ('-buat',)
    search_fields = []

@admin.register(URLs)
class DataURL(admin.ModelAdmin):  
    list_display = ('slug', 'id')
    ordering = ('-id',)
    search_fields = []


@admin.register(CustomURLs)
class DataURL(admin.ModelAdmin):  
    list_display = ('user', 'url', 'long_url', 'foll', 'id')
    ordering = ('-id',)
    search_fields = []