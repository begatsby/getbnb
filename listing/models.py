from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class PropertyType(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name


class RoomType(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.name


class Property(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='properties'
    )

    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)

    property_type = models.ForeignKey(
        'listing.PropertyType',
        on_delete=models.PROTECT,
        related_name='+'
    )
    room_type = models.ForeignKey(
        'listing.RoomType',
        on_delete=models.PROTECT,
        related_name='+'
    )
    accomodation_count = models.SmallIntegerField(blank=False)
    bedroom_count = models.SmallIntegerField(blank=False)
    bed_count = models.SmallIntegerField(blank=False)
    bathroom_count = models.SmallIntegerField(blank=False)

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'properties'


class Location(models.Model):
    property = models.OneToOneField(
        'listing.Property',
        on_delete=models.CASCADE
    )
    address_1 = models.CharField(max_length=120)
    address_2 = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=60)
    zip_code = models.CharField(max_length=12)
    country = CountryField()

    def __str__(self):
        return self.address_1


class Photo(models.Model):
    property = models.ForeignKey(
        'listing.Property',
        on_delete=models.CASCADE,
        related_name='photos'
    )
    title = models.CharField(max_length=60, blank=True, null=True)
    file = models.ImageField(upload_to='photos', blank=True, null=True)
    thumb_small = ImageSpecField(
        source='file',
        processors=[ResizeToFill(350, 250)],
        options={'quality': 85}
    )

    def __str__(self):
        return self.url


class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'amenities'


class PropertyAmenity(models.Model):
    property = models.ForeignKey(
        'listing.Property',
        on_delete=models.CASCADE,
        related_name='amenities'
    )
    amenity = models.ForeignKey(
        'listing.Amenity',
        on_delete=models.CASCADE,
        related_name='+'
    )

    def __str__(self):
        return self.amenity.name

    class Meta:
        verbose_name_plural = 'amenity'
