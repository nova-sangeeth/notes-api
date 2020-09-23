from rest_framework import serializers

from .models import notes_api_model


class notes_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = notes_api_model
        fields = "__all__"
