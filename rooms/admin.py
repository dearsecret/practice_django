from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class Room(admin.ModelAdmin):
    pass
