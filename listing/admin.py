from django.contrib import admin

from .models import PropertyType, RoomType, Property


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'property_type', 'room_type',
        'accomodation_count', 'bedroom_count', 'bed_count',
        'bathroom_count', 'is_published']
