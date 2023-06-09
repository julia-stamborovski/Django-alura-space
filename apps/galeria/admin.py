from django.contrib import admin
from apps.galeria.models import Photography

class ListingPhotography(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "published")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category", "user",)
    list_per_page = 10
    list_editable = ("published",)

admin.site.register(Photography, ListingPhotography)