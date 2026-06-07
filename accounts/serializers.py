from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    company_name = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):

        user = User.objects.create_user(
            username = validated_data["username"],
            password = validated_data["password"],
            email = validated_data["email"]
        )

#Signal Company create kar chuka hoga

        user.company.company_name = validated_data["company_name"]
        user.company.save()

        return user


