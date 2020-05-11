from django.contrib import admin
from . import models


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'price')
    list_per_page = 25

admin.site.register(models.Listing, ListingAdmin)