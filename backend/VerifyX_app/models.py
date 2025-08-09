from django.db import models
from _applib.model_utils import OTP_Status


class OTP_Model(models.Model):
    otp_for = models.CharField(max_length=40)
    identifier = models.CharField(max_length=200)
    reason = models.CharField(max_length=100)
    otp_message = models.CharField(max_length=300, null=True, blank= True)
    otp_code = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices= OTP_Status.choices, default=OTP_Status.INITIALIZE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    verfied_at = models.DateTimeField(null=True,blank = True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.otp_for
    
    
    class Meta:
        verbose_name = "OTP"
        verbose_name_plural = "Otps"
        db_table = "otp_db"