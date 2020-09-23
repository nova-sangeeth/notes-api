from django.conf.urls import url
from django.urls import path, include
from .views import notes_viewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r"api", viewset=notes_viewset)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]