from django.db import models
from django.conf import settings


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='+')

    text = models.CharField(max_length=500)
    sent_at = models.DateTimeField()
    read_at = models.DateTimeField(null=True)

    is_deleted = models.BooleanField(default=False)
