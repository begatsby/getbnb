from django.contrib import admin
from imagekit.admin import AdminThumbnail


from .models import (
    PropertyType, RoomType, Property, Amenity, PropertyAmenity,
    Photo
)

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class PropertyAmenityInline(admin.StackedInline):
    model = PropertyAmenity
    extra = 1


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'property_type', 'room_type',
        'accomodation_count', 'bedroom_count', 'bed_count',
        'bathroom_count', 'is_published']
    inlines = [PropertyAmenityInline, PhotoInline]
