from django.db import transaction
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

class PersonRegisterSerializer(RegisterSerializer):
    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.save()
        return user