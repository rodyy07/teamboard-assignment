from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer
class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(data = request.data)

        serializer.is_valid(raise_exception = True)

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "access" : str(refresh.access_token),
                "refresh": str(refresh),
                "api_key" : user.company.api_key
            },

            status = status.HTTP_201_CREATED
        )

class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"]
        )

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "company_name": user.company.company_name,
            "api_key": user.company.api_key
        })


# Create your views here.
