# Before class

-   Navigate to `mysite` project
-   Run virtual environment

# Outline

In this lesson, we're going to learn how to create a Todo app.

<img width="446" alt="Screen Shot 2021-10-17 at 5 06 45 PM" src="https://user-images.githubusercontent.com/7483633/137645162-bf24a2f2-fe1d-40e1-82c7-93627572c6e7.png">

-   Run a live demo of the Todo app
-   Describe the app by its views, content, URLs and its CRUD-like (Create, Read, Update, Delete) functionality
-   Explain that today we'll use databases, and in particular, *models* in django to create the CRUD functionality

# Run Django server

-   Navigate to `mysite` project
-   Make sure `manage.py` exists in the directory

```
$ ls
manage.py*  mysite/
```

Then run the server

```
$ python manage.py runserver
```

# Initial setup

Before we start building the app, we must do some initial setup:

## Create `todo` app

```

$ python manage.py startapp todo
$ ls
db.sqlite3 manage.py\* myapp/ mysite/ sandwich/ todo/

```

## Register `todo` app with the `mysite` project

Edit `mysite/settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'sandwich.apps.SandwichConfig',
    'todo.apps.TodoConfig',
    ... # Leave all the other INSTALLED_APPS
]
```

## Create `todo/urls.py`

`todo/urls.py`

```python
from django.urls import path

urlpatterns = []
```

## Add `todo` urls to `mysite` project

`mysite/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('sandwich/', include('sandwich.urls')),
    path('todo/', include('todo.urls')) # add this line of code
]
```

# Todo model

-   Revisit database design from previous lesson
-   A model translates to one table in the database
-   Tables are stored in a `sqlite` instance, a zero-configuration, lightweight database that is default in Django when you install it. You can configure other databases in its place.

## Designing a table

| task_id | task   |
| ------- | ------ |
| 1       | Item 1 |
| 2       | Item 2 |

## Create model

`todo/models.py`

```python
from django.db import models

# Create your models here.
class Todo(models.Model):
    task_id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=255)
```

## Run migrations

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

## Register model in admin site

-   Log into admin interface
-   We can see database tables here
-   Let's register the todo model to make it available in the admin site

`todo/admin.py`

```python
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Todo)
```

-   Refresh the admin site!
-   Show that you can use the admin site to create, read, update, delete entries in the todos table

## Exploring QuerySet API

Run the Django's python interactive shell:

```
$ python manage.py shell
```

Show that the `Todo.objects.all()` returns all the tasks in the todos table:

```python
In [1]: from todo.models import Todo
In [2]: Todo.objects.all()
<QuerySet []>
```

Exit the interactive shell:

```python
In [3]: exit()
```

-   We will refer to the [QuerySet API](https://docs.djangoproject.com/en/3.2/ref/models/querysets/) throughout this lesson

# Todo home page

Before we get started, let's review the page:

-   This page is at `/todo`
-   This page has a heading - "Tasks"
-   This page has a text input and a "Create" button
-   This page has an unordered list of tasks

<img width="446" alt="Screen Shot 2021-10-17 at 5 06 45 PM" src="https://user-images.githubusercontent.com/7483633/137645162-bf24a2f2-fe1d-40e1-82c7-93627572c6e7.png">

## Create route

`todo/urls.py`

-   The `path` function takes two more arguments, the Django `view` which we will create next and a `name` for the URL

```python
from django.urls import path

urlpatterns = [
    # todo/
    path('')
]
```

## Create view

`todo/views.py`

```python
from django.shortcuts import render

def todo(request):
    if request.method == 'GET':
        return render(request, 'list.html')
```

Now that we've created a view, let's add it to our URL:

`todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # todo/
    path('', views.todo, name='todo')
]
```

Since we want the todo homepage to have hyperlinks to tasks, let's pull our tasks from the database:

```python
from django.shortcuts import render
from .models import Todo

def todo(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-task_id')
        return render(request, 'list.html', context={'tasks': tasks})
```

-   Explain that [all()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.all) lists all items in the database
-   Explain that [order_by()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by) lets us specify how we want to order these items
    -   Explain that `-` at the beginning of `'-task_id'` indicates descending order

## Create template

-   Create a directory called `templates` in `todo` directory
-   Create an HTML file `list.html` in `templates`

`todo/templates/list.html`

-   We can use built-in [for loop template tag](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for) to iterate over `tasks` list
-   We will set the `href` once we create the task view

```html
<h1>Tasks</h1>

<ul>
    {% for task in tasks %}
    <li><a href="">{{ task.task }}</a></li>
    {% endfor %}
</ul>
```

## Let's test it out!

-   Go to `http:localhost:8000/todo`

## Create form

Let's create the text input field and 'Create' button.

-   Django lets us handle complex flows around submitting forms to the server
-   We can use Django's form functionality to submit a task securely, validate it before creating an entry in our todos table

`todo/forms.py`

```python
from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(label='Add task', max_length=255)
```

`todo/templates/list.html`

```html
<h1>Tasks</h1>

<form action="{% url 'todo' %}" method="POST">
    {% csrf_token %} {{ form }}
    <input type="submit" name="create" value="Create" />
</form>

<ul>
    {% for task in tasks %}
    <li><a href="">{{ task.task }}</a></li>
    {% endfor %}
</ul>
```

-   Explain `action` and `method` attributes
-   Explain `csrf_token` is required to make a POST request to Django

`todo/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

def todo(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-task_id')
        form = TodoForm()
        return render(request, 'list.html', context={'form': form, 'tasks': tasks})

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            Todo.objects.create(task=task)
        return HttpResponseRedirect(reverse('todo'))
```

-   Explain how to work with `TodoForm()` instance
-   Explain `HTTPResponseRedirect()`
-   Explain `reverse()`

## Let's test it out!

-   Go to `http:localhost:8000/todo`
-   Use the text field and click 'Create' or press enter to add a new task

# Task page

Before we get started, let's review the page:

-   This page has a text input field pre-populated with the current task
-   This page has a 'Save' button
-   This page has a 'Delete' button

<img width="376" alt="Screen Shot 2021-10-17 at 5 04 58 PM" src="https://user-images.githubusercontent.com/7483633/137645175-b3f98959-9de2-43f1-812a-469587ca5eff.png">

## Create route

`todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # todo/
    path('', views.todo, name='todo'),
    # todo/<int:task_id>
    path('<int:task_id>')
]
```

## Create view

`todo/views.py`

```python
def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial={'task': todo.task })
        return render(request, 'detail.html', { 'form': form, 'task_id': task_id })
```

-   Explain that `get()` returns a dictionary instead of a QuerySet object
-   Explain that `initial` argument lets us pre-populate a form field

Now that we've created a view, let's add it to our URL:

`todo/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # todo/
    path('', views.todo, name='todo'),
    # todo/<int:task_id>
    path('<int:task_id>', views.task, name='task')
]
```

## Create template

-   Create an HTML file `detail.html` in `templates`

`todo/templates/detail.html`

```html
<form action="{% url 'task' task_id %}" method="POST">
    {% csrf_token %} {{ form }}
    <input type="submit" name="save" value="Save" />
    <input type="submit" name="delete" value="Delete" />
</form>
```

-   Explain `action` and `method` attributes
-   Explain `csrf_token` is required to make a POST request to Django

Let's see how we can handle a POST request in our view:

```python
def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial={'task': todo.task })
        return render(request, 'detail.html', { 'form': form, 'task_id': task_id })
    if request.method == 'POST':
        if 'save' in request.POST:
            pass
        elif 'delete' in request.POST:
            pass
        return HttpResponseRedirect(reverse('todo'))
```

-   Explain `save` and `delete` come from `name` attributes in the text fields

```python
def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial={'task': todo.task })
        return render(request, 'detail.html', { 'form': form, 'task_id': task_id })
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
             Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))
```

-   Explain that `TodoForm` instance can be used to validate the incoming POST request form data
-   Explain that `filter()` filters the entries in the table by finding a match for `task_id`
-   Explain that `update()` updates an existing entry in the table
-   Explain that `delete()` deletes an existing entry in the table

Let's update the list template to link to the detail template
`todo/templates/list.html`

```html
<h1>Tasks</h1>

<ul>
    {% for task in tasks %}
    <li><a href="{% url 'task' task.task_id %}">{{ task.task }}</a></li>
    {% endfor %}
</ul>
```

## Let's test it out!

-   Go to `http:localhost:8000/todo/1`

# Conclusion

In this lesson we covered more concepts in Django:

-   We created Django models to create tables in our database and added functionality to create, read, update and delete entries in the table
-   We created Django forms to dynamically create form elements and send form data to the server where it is validated
-   We handled both GET and POST requests to the server
