# Django challenge: make the helo world app!

In this challenge, to get started with Django, you'll remake the "Hello World" app from class and add a few extra features

# 1. Get set up for Django

* First, go to your personal folder in your pod repo and *on a new branch* make a `django-projects` directory there. You'll use this directory to store django apps you make in class
* In the `django-projects` folder:
- Run `python3 -m venv django-env` to create a new virtual environment
- Run `source django-env/bin/activate` on Unix/MacOS or `django-env\Scripts\activate.bat` on Windows to activate the virtual environment
- Run `pip install django` to install Django
- Run `pip freeze > requirements.txt`

# 2. Start a new Django project

Create the project
```
$ django-admin startproject mysite
$ ls
mysite/
```

Then navigate into the project folder you created

```
$ cd mysite
$ ls
manage.py*  mysite/
```

-   Explain use of `manage.py` to control a lot of the operations around building the Django app

# 3. Run Django server

Use the `manage.py` file to run the server! Don't worry about the "unapplied migrations" yet for now

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


# 4. Create your app

Use the `manage.py` file to start up your new app! Then inspect the files that are created

```
$ python manage.py startapp myapp
$ ls
db.sqlite3  manage.py*  myapp/  mysite/
```

# 5. Register `myapp` app with the `mysite` project

Edit `mysite/settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    ... # Leave all the other INSTALLED_APPS
]
```

Now, your `myapp` app should be connected with the larger `mysite` project

# 6. Migrate the database

We'll talk more about what migrations are later, but for now run this to get the initial database set up for your project. 

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

# 7. Create Super User

Make yourself a "superuser" so that you can use Django's admin interface to review the data in your database. Create your username and password!

Again this uses `manage.py`


```
$ python manage.py createsuperuser

Username (leave blank to use 'bennett'):
Email address: hello@bennettgarner.com
Password:
Password (again):
Superuser created successfully.
```

Now verify that it works. Start up the Django server:

```
$ python manage.py runserver
```

And then navigate to `localhost:8000/admin`

<img width="1680" alt="Screen Shot 2021-09-21 at 6 10 01 PM" src="https://user-images.githubusercontent.com/7483633/134254446-706496c6-883f-4cd7-9d36-91ab00e7b433.png">

Use the credentials you created when running the `createsuperuser` command to log into the Django admin interface.

<img width="1677" alt="Screen Shot 2021-09-21 at 6 13 57 PM" src="https://user-images.githubusercontent.com/7483633/134254824-d4d221b0-ed84-41b8-8f92-a0597d912916.png">

Not much data to explore yet, but now you can see that you're an 'admin' for your project! This will come in useful much more later once we start adding more to the database. 


# 8. Create a URL for the "hello world" app

In `myapp` directory create a file called `urls.py` as below:

```python
from django.urls import path
from myapp.views import hello

urlpatterns = [
    # myapp/
    path('', hello, name='hello'),
]
```

# 9. Create a view

Open `myapp/views.py`. It will initially look like this:

```python
from django.shortcuts import render

# Create your views here.
```

Let's add some code to render the first view!

```python
from django.shortcuts import render

# Create your views here.
def hello(request):
    if request.method == 'GET':
        return render(request, 'hello.html')
```

# 10. Create a template

-   In `myapp` directory create a new directory called `templates`.
-   Inside `templates` create a file called `hello.html`.
-   Add the code below in `hello.html`:

```html
<h1>Hello World</h1>
```

# 11. Add `myapp` urls to `mysite` project

Update `urlpatterns` in `mysite/urls.py`

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

# 12. Make the app dynamic!

Add a new a URL that takes a string parameter called `name`. The goal is to have the new page say hello to a different person, depending on the url

### In `myapp/urls.py`

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

### In `myapp/views.py`

Let's pass this `name` parameter down to the view, then render as a dictionary for the `context` argument

```python
def hello(request, name):
    if request.method == 'GET':
        return render(request, 'hello.html', context = { 'name': name })
```



### In `myapp/templates/hello.html`

Finally, update the template so it can dynamically render the `name` parameter. Remember that this is using a Django template to take in `{{ name }}`, not just regular HTML!

```html
<h1>Hello {{ name }}</h1>
```

### Check out `localhost:8000/myapp/ash` instead!

# 13. Add a `filter` to the template

This will make the name always show up using the django template for 'title' -- first letter caps

```html
<h1>Hello {{ name|title }}</h1>
```

### Try some more examples and see what happens

-   `localhost:8000/myapp/paul`
-   `localhost:8000/myapp/serena`
-   `localhost:8000/myapp/alanna`
-   `localhost:8000/myapp/yusuf`

# 14. Give a default person to greet

Go to `localhost:8000/myapp` and notice that it creates an error...

-   The error `hello() missing 1 required positional argument: 'name'` still requires we provide a value for the `name` parameter. Let's set a default value:

```python
def hello(request, name='world'):
    if request.method == 'GET':
        return render(request, 'hello.html', { 'name': name })
```

Go to `localhost:8000/myapp` again and make sure it works!

# 15. Make a "goodbye" page

We've given very specific code instructions for the previous steps, but this last one is a little more open-ended. However, you can use what you've learned so far to do this!

- Make an additional "goodbye" page that says "see you later" based on the url, such that going to `localhost:8000/myapp/goodbye/django` results in a page as below:
- Don't worry about setting a 'default' person to say 'see you later' to here. 

<img src='images/goodbye_page.png'>


# 16. Wrap-up! Commit and push your work, send a pull request to your TA

**Congrats!!** You've just finished your first Django app of the class!
