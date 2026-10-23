from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """Serializer Class."""

    class Meta:
        model = Todo
        fields = ("id", "title", "description", "completed")
