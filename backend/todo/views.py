from django.shortcuts import render
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoView(viewsets.ModelViewSet):
    """Main view for Todo app."""

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
