from django.db import models


class OTP_Status(models.TextChoices):
    INITIALIZE = "INITIALIZE "
    VERIFIED = "VERIFIED"
    EXPIRED = "EXPIRED"