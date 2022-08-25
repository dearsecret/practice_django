from django.db import models
from core import models as core_model

# Create your models here.


class Reservation(core_model.TimeStampedModel):
    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCLED = "canceled"
    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCLED, "Canceled"),
    )

    status = models.CharField(
        max_length=80, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.TimeField()
    check_out = models.TimeField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
