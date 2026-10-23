from django.test import TestCase

from todo.models import Todo


class TodoModelTest(TestCase):
    def test_todo_creation(self):
        todo = Todo.objects.create(
            title="Test Todo", description="Test Description", completed=False
        )
        self.assertEqual(todo.title, "Test Todo")
        self.assertFalse(todo.completed)
