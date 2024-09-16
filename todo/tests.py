from datetime import datetime
from django.test import TestCase

from todo.models import Todo, TodoList

# Create your tests here.
class TestTodoCase(TestCase):
    TEST_TODO_TITLE = 'Test ELement'
    def setUp(self): # creer une instance de TodoList() avant que les autres methodes ne commencent
        self.todo_list = TodoList() # l'instance de TodoList() sera utilise par l'instance de Todo() dans le test unitaire
        self.todo_list.name = 'courses'
        self.todo_list.save()

        self.todoTestELement = Todo()
        self.todoTestELement.title = self.TEST_TODO_TITLE
        self.todoTestELement.due_date = datetime.now()
        self.todoTestELement.completed = True
        self.todoTestELement.favourite = False
        self.todoTestELement.todo_list = self.todo_list
        self.todoTestELement.save()

    def test_create_todo(self):
        nb_todo_before = Todo.objects.count()

        TodoTest = Todo()
        TodoTest.title = 'Acheter du pain'
        TodoTest.due_date = datetime.today()
        TodoTest.completed = True
        TodoTest.favourite = False
        TodoTest.todo_list = self.todo_list # instance de TodoList()

        TodoTest.save()

        nb_todo_after = Todo.objects.count()
        self.assertTrue(nb_todo_after == nb_todo_before + 1)
    def test_update_todo(self):
        self.assertEqual(self.todoTestELement.title,self.TEST_TODO_TITLE)

        self.todoTestELement.title = 'Changed'
        #tsy adino ny mi-save
        self.todoTestELement.save()

        tempElement = Todo.objects.get(id=self.todoTestELement.id)

        self.assertEqual(tempElement.title,'Changed')
    def test_delete_todo(self):
        nb_todo_before = Todo.objects.count()

        self.todoTestELement.delete()

        nb_todo_after = Todo.objects.count()

        self.assertTrue(nb_todo_after == nb_todo_before - 1)