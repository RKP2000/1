from django.contrib import admin
from . models import Country



@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'government_type',  'important_sports', 'products' )