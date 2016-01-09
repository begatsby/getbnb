from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


class PropertyType(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name


class Property(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)

    property_type = models.ForeignKey('listing.PropertyType')
    room_type = models.ForeignKey('listing.RoomType')
    accomodation_count = models.SmallIntegerField(blank=False)
    bedroom_count = models.SmallIntegerField(blank=False)
    bed_count = models.SmallIntegerField(blank=False)
    bathroom_count = models.SmallIntegerField(blank=False)

    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'properties'


class Location(models.Model):
    property = models.ForeignKey('listing.Property', on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=12)
    country = CountryField()

    def __str__(self):
        return self.address_1
