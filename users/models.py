from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICE = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUARE_KOREAN = "kr"
    LANGUAGE_ENGLISH = "eng"
    LANGUAGE_CHOICES = (
        (LANGUARE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    )

    CURRENCY_KRW = "krw"
    CURRENCY_USD = "usd"
    CURRENCY_CHOICES = ((CURRENCY_KRW, "KRW"), (CURRENCY_USD, "USD"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICE, max_length=80, null=True, blank=True
    )
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=80, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=80, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)
