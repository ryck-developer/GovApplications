from app.models import AllCookies
from rest_framework import serializers




class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllCookies
        fields = [
            "cookie",
        ]

