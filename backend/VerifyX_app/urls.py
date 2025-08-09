from django.urls import path
from .views import OTP_View

urlpatterns = [
    path(
        # =>>>>>>>> http://127.0.0.1:8001/otp/send/ <<<<<<<<=
        route = "send/",
        view = OTP_View.as_view(),
        name = "otp_send"
    )
]