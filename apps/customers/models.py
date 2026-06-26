from django.db import models

import uuid

from config import settings



# Create your models here.
class Customer(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='customer'
    )

    phone_number = models.CharField(
        max_length=255,
        blank=True
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    def __str__(self):
        return self.user.username