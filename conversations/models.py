from django.db import models
from core import models as core_model

# Create your models here.


class Conversation(core_model.TimeStampedModel):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return f"{self.created}"


class Message(core_model.TimeStampedModel):
    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    converation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says : {self:text}"
