from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.test import APITestCase

from todo.models import Todo


class TodoAPITest(APITestCase):
    def setUp(self):
        """Set up tests."""
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client.force_authenticate(user=self.user)
        self.default_data: dict[str, str | bool] = {
            "title": "Test Todo",
            "description": "Test Description",
            "completed": False,
        }

    def create_default_todo(self) -> HttpResponse:
        """Create default todo, to help in tests."""
        response = self.client.post("/api/todos/", self.default_data)
        return response

    def test_create_todo(self):
        """Todo item is successfully created."""
        started_with: int = Todo.objects.count()
        response: HttpResponse = self.create_default_todo()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), started_with + 1)

    def test_delete_todo(self):
        """Todo item is successfully deleted."""
        create_response: HttpResponse = self.create_default_todo()
        item_id: int = create_response.data["id"]
        before_delete = Todo.objects.count()

        response = self.client.delete(f"/api/todos/{item_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), before_delete - 1)

    def test_edit_todo(self):
        """Todo item is successfully edited."""
        create_response: HttpResponse = self.create_default_todo()
        item_id: int = create_response.data["id"]

        edit: dict[str, str | bool] = {
            "title": "Test Todo - Edited",
            "description": "Test Description was edited",
            "completed": False,
        }
        response: HttpResponse = self.client.put(f"/api/todos/{item_id}/", edit)
        item = Todo.objects.get(id=item_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(item.title, edit["title"])
        self.assertEqual(item.description, edit["description"])

    def test_get_todos(self):
        """Todo items are successfully fetched."""
        Todo.objects.create(title="Test Todo", description="Test")
        response = self.client.get("/api/todos/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
