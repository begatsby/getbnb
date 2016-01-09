from django.db import models
from django.conf import settings


class Profile(models.Model):
    GENDER_MALE = 'm'
    GENDER_FEMALE = 'f'
    GENDER_OTHER = 'o'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=False)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    current_location = models.CharField(max_length=60, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
