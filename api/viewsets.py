"""REST API viewsets"""

from rest_framework import viewsets
from . import models, serializers


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner viewset"""

    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerModelSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
    """Species viewset"""

    queryset = models.Species.objects.all()
    serializer_class = serializers.SpeciesModelSerializer


class PetViewSet(viewsets.ModelViewSet):
    """Pet viewset"""

    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetModelSerializer


class RecordViewSet(viewsets.ModelViewSet):
    """Record viewset"""

    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordModelSerializer
