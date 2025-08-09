from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otp/', include('VerifyX_app.urls')) # =>>>>>>>> http://127.0.0.1:8001/otp/send/ <<<<<<<<=
]
