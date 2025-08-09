from django.contrib import admin
from .models import OTP_Model

@admin.register(OTP_Model)


class OTP_Admin(admin.ModelAdmin):
    list_display = (
        "otp_for",
        "identifier",
        "reason",
        "status",
        "expires_at",
    )

    ordering = ["-id"]
