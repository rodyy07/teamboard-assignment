from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from accounts.models import Company

class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self,request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            raise AuthenticationFailed("API key is required")

        try:
            company = Company.objects.get(api_key=api_key)
        except Company.DoesNotExist:

            raise AuthenticationFailed("Invalid API key")

        return (company.user, None)