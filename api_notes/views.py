from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializer import notes_serializer
from .models import notes_api_model


class notes_viewset(viewsets.ModelViewSet):
    queryset = notes_api_model.objects.all()
    serializer_class = notes_serializer