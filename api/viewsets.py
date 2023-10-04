"""REST API viewsets"""

from rest_framework import viewsets, response, decorators
from . import models, serializers


class UserViewSet(viewsets.ViewSet):
    """User sign up"""

    authentication_classes = []
    permission_classes = []
    serializer_class = serializers.UserModelSerializer

    def create(self, request):
        """Create new user action"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response(
            {"detail": f"user {user.username} created"}, status=201
        )


class OwnerViewSet(viewsets.ModelViewSet):
    """Owner viewset"""

    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerModelSerializer

    @decorators.action(detail=False, methods=["post"])
    def auth(self, request):
        # Logica para autenticar al usuario
        email = request.data.get("email")
        password = request.data.get("password")
        return response.Response({"token": "lkajshdlkfjhaslkdjhflkasjhdfklj"})


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
