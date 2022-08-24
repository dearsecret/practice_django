from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        abstract = True
