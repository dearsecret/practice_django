from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class Room(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )
    search_fields = ("=city", "^host__username")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
