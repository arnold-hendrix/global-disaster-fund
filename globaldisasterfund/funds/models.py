from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Organization(models.Model):
    representative = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    contact = models.EmailField(max_length=254)
    license_verification = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Donations(models.Model):
    donor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    donation_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return self.donation_amount
