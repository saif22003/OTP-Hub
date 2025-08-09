from rest_framework.views import APIView
from .models import OTP_Model
from _applib.utils_logic import otp_generator
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from datetime import datetime, timedelta


class OTP_View(APIView):
    def post(self,request):
        otp_for = request.data.get("otp_for")
        identifier = request.data.get("identifier")
        reason = request.data.get("reason")
        otp_code = otp_generator()
        otp_message = f"Your OTP is {otp_code}"
        
        current_time = datetime.now()
        after_two_minutes = timedelta(minutes=2)
        expires_at = current_time + after_two_minutes


        OTP_Model.objects.create(
            otp_for  = otp_for  ,
            identifier =  identifier,
            reason = reason,
            otp_message = otp_message,
            otp_code = otp_code ,
            expires_at =expires_at 
        )

        return Response({
            "msg" : "Success",
            "data" : "OTP Successfully Send",
        }
        )