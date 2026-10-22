from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    """Main view for Todo app."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
