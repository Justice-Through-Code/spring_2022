# Before Class

Make sure students have: 
- Watched 'How the web works' 
- Followed the instructions to setup virtual environment and install dependencies

It is not important to code along in this lecture but to listen and take notes. 
Students will have a chance to build the app in this lesson during challenge.

# Outline

We're going to learn how to:
-   Create a simple website using the Django web framework
-   Demo the 'Hello' app, describe its URLs and change in content based on the URL

# Why Django?

-   Known as “the web framework for perfectionists with deadlines,” Django powers some of the biggest websites in the world like Instagram, Pinterest, National Geographic, Mozilla, Disqus
-   In the 'How the web works' video, we mentioned that the act of visiting a website boils down to the client making a request for a resource to the server and a server responding with that resource. By using Django we can build a server that can respond to client requests
<img width="827" alt="Screen Shot 2021-10-19 at 5 36 28 PM" src="https://user-images.githubusercontent.com/7483633/137994324-32e6a5f3-4713-4ca7-84da-4b9c4bb49a2a.png">
<img width="825" alt="Screen Shot 2021-10-19 at 5 36 35 PM" src="https://user-images.githubusercontent.com/7483633/137994333-e8906353-62ba-4d56-b782-827ca35e080f.png">


-   Explain how Django allows us to do full stack development
-   Share Django's [official documentation](https://docs.djangoproject.com/en/)

# Django architecture overview

<img width="983" alt="Screen Shot 2021-10-20 at 9 30 57 AM" src="https://user-images.githubusercontent.com/7483633/138102708-ffe085fe-26d7-4068-a991-2ca2c56b28b4.png">



-   Explain what the Django server does when a request is received from the user typing in a URL and pressing enter in their browser
-   Explain that in this lesson we will touch on everything in this architecture except for Model which will be covered in a future lesson

# Start a new Django project

```
$ django-admin startproject mysite
$ ls
mysite/
```

```
$ cd mysite
$ ls
manage.py*  mysite/
```

-   Explain use of `manage.py` to control a lot of the operations around building the Django app

# Run Django server

```
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 17, 2019 - 16:09:28
Django version 2.2.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Go to `localhost:8000` and you should see the Django welcome screen!

<img width="1680" alt="Screen Shot 2021-09-21 at 6 09 09 PM" src="https://user-images.githubusercontent.com/7483633/134254378-9faa393e-ef95-4168-9464-980e604d1ba4.png">

# Initial Setup

## Create app

-   Explain that _app_ here is not the same way we use "app" in conversation -- one single website/project can have many apps
-   Walk students through directory structure of `myapp/` and `mysite/`

```
$ python manage.py startapp myapp
$ ls
db.sqlite3  manage.py*  myapp/  mysite/
```

## Register `myapp` app with the `mysite` project

Edit `mysite/settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    ... # Leave all the other INSTALLED_APPS
]
```

## Migrate the database

Let's migrate those initial models!

-   Explain what a [migration](https://docs.djangoproject.com/en/3.2/topics/migrations/) is (updating any changes made to the models to be reflected in the database)
-   Explain when migrations need to be done

```
$ python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

## Create Super User

Let’s make ourselves the owners and administrators of this project so we can use Django's admin interface
to review the data in our database

```
$ python manage.py createsuperuser

Username (leave blank to use 'bennett'):
Email address: hello@bennettgarner.com
Password:
Password (again):
Superuser created successfully.
```

Let’s verify that it works. Start up the Django server:

```
$ python manage.py runserver
```

And then navigate to `localhost:8000/admin`

<img width="1680" alt="Screen Shot 2021-09-21 at 6 10 01 PM" src="https://user-images.githubusercontent.com/7483633/134254446-706496c6-883f-4cd7-9d36-91ab00e7b433.png">

Use the credentials you created when running the `createsuperuser` command to log into the Django admin interface.

<img width="1677" alt="Screen Shot 2021-09-21 at 6 13 57 PM" src="https://user-images.githubusercontent.com/7483633/134254824-d4d221b0-ed84-41b8-8f92-a0597d912916.png">

We are not going to explore the admin interface in this lesson, but it's good practice to create a super user after creating a Django project

# Hello app

## Create a URL

In `myapp` directory create a file called `urls.py`.

```python
from django.urls import path

from myapp.views import hello

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
]
```

## Create a view

Open `myapp/views.py`

```python
from django.shortcuts import render

# Create your views here.
```

Let's add some code:

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    if request.method == 'GET':
        return render(request, 'hello.html')
```

-   Explain Django views
-   Explain how `GET` relates to a `GET` request

## Create a template

-   In `myapp` directory create a new directory called `templates`.
-   Inside `templates` create a file called `hello.html`.
-   Add the code below in `hello.html`:

```html
<h1>Hello World</h1>
```

## Add `myapp` urls to `mysite` project

```python
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')), # add this line of code
]
```

Go to `localhost:8000/myapp`

# Let's make our app dynamic

We will add a new a URL that takes a string parameter called `name`

In `myapp/urls.py`

```python
from django.urls import path

from myapp.views import hello

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
    # myapp/<str:name>
    path('<str:name>', hello, name='hello_name'),
]
```

Explain what `<str:name>` does

In `myapp/views.py`

Let's pass this `name` parameter down to the view

```python
def hello(request, name):
    if request.method == 'GET':
        return render(request, 'hello.html', { 'name': name })
```

Explain what the third parameter in `render` function does

In `myapp/templates/hello.html`

Finally, let's update the template so it can dynamically render the `name` parameter

```html
<h1>Hello {{ name }}</h1>
```

-   Explain what the template syntax is doing
-   Distinguish between regular HTML and Django templates
-   Share the [template syntax documentation](https://docs.djangoproject.com/en/3.2/ref/templates/language/)

Let's try `localhost:8000/myapp/ash` instead!

Add a `filter` to the template

```html
<h1>Hello {{ name|title }}</h1>
```

-   Scroll to show what filters are in [template syntax documentation](https://docs.djangoproject.com/en/3.2/ref/templates/language/)

### Show more examples

-   `localhost:8000/myapp/paul`
-   `localhost:8000/myapp/serena`
-   `localhost:8000/myapp/alanna`
-   `localhost:8000/myapp/yusuf`

# Dealing with Django errors

Go to `localhost:8000/myapp`

Hmm, looks like it's not working...

-   Explain how to read Django errors
-   The error `hello() missing 1 required positional argument: 'name'` still requires we provide a value for the `name` parameter. Let's set a default value:

```python
def hello(request, name='world'):
    if request.method == 'GET':
        return render(request, 'hello.html', { 'name': name })
```

Let's go to `localhost:8000/myapp` again.

Awesome it works!

# Conclusion

We build our first Django website. This included:

-   Creating a Django's CLI to create project and app
-   Running a Django server
-   Running a migration
-   Creating a superuser for Django admin interface
-   Creating a URL, view and template in the Django app to serve a dynamic HTML page
