from django.urls import include, path
from rest_framework import routers
from . import viewsets

router = routers.DefaultRouter()
router.register(r"owners", viewsets.OwnerViewSet)
router.register(r"species", viewsets.SpeciesViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
