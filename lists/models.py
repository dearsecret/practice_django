from django.db import models
from core import models as core_model

# Create your models here.


class List(core_model.TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", blank=True)
