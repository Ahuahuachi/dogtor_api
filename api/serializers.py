"""API Serializers"""

from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserModelSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class OwnerModelSerializer(serializers.ModelSerializer):
    """Owner model serializer"""

    class Meta:
        model = models.Owner
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
        )


class SpeciesModelSerializer(serializers.ModelSerializer):
    """Species model serializer"""

    class Meta:
        model = models.Species
        fields = ("id", "name")


class PetModelSerializer(serializers.ModelSerializer):
    """Pet model serializer"""

    class Meta:
        model = models.Pet
        fields = ("id", "name", "owner", "age", "species", "created_at")
        read_only_fields = ("created_at",)


class RecordModelSerializer(serializers.ModelSerializer):
    """Record model serializer"""

    class Meta:
        model = models.Record
        fields = ("id", "category", "procedure", "pet", "date")
