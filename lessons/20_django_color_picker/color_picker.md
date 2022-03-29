# Django challenge: Color Picker

In this challenge, you'll create a new django project called 'Color Picker'.

# 1. Get set up for Django

* First, go to your `django-projects` directory
- Create a new folder called `color-picker-container` and `cd` into it
- Run `python3 -m venv venv` (or whichever version of this your computer uses) to create a new virtual environment (it's common practice to name your virtual environment 'venv')
- Run `source django-env/bin/activate` on Unix/MacOS or `django-env\Scripts\activate.bat` on Windows to activate the virtual environment
- Run `pip install django` to install Django
- Run `pip freeze > requirements.txt` (take a look at the new requirements file that popped up!)


# 2. Initialize your git instance

In your terminal, initialize a new instance of git with

```
$ git init
```

Be sure to `add` and `commit` your progress as you go!

# 3. Start a new Django project

Create the project
```
$ django-admin startproject colorpicker
$ ls
colorpicker/
```

Then navigate into the project folder you created

```
$ cd colorpicker
$ ls
manage.py*  colorpicker/
```

# 4. Run Django server

Use the `manage.py` file to run the server! Don't worry about the "unapplied migrations" yet for now

```
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 17, 2019 - 16:09:28
Django version 2.2.1, using settings 'colorpicker.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Go to `localhost:8000` and you should see the Django welcome screen!

<img width="1680" alt="Screen Shot 2021-09-21 at 6 09 09 PM" src="https://user-images.githubusercontent.com/7483633/134254378-9faa393e-ef95-4168-9464-980e604d1ba4.png">


# 5. Create your app

Use the `manage.py` file to start up your new app! Then inspect the files that are created

```
$ python manage.py startapp paintapp
$ ls
db.sqlite3  manage.py*  paintapp/  colorpicker/
```

# 6. Register `paintapp` app with the `colorpicker` project

Edit `colorpicker/settings.py`

```python
INSTALLED_APPS = [
    'paintapp.apps.PaintappConfig',
    ... # Leave all the other INSTALLED_APPS
]
```

Now, your `paintapp` app should be connected with the larger `colorpicker` project

# 7. Migrate the database

We'll talk more about what migrations are later, but for now run this to get the initial database set up for your project. We won't use it in this project, but it'll get rid of the annoying red instruction to migrate them.

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

# 8. Create a URL for the "color picker" app

In your `paintapp` directory, create a file called `urls.py` as below:

```python
from django.urls import path

from paintapp.views import PaintView

urlpatterns = [
    # paintapp/
    path('', PaintView.as_view(), name='paint'),
]
```

# 9. Create the view

Open `paintapp/views.py`. It will initially look like this:

```python
from django.shortcuts import render

# Create your views here.
```

Let's add some code to render the view that we referenced above!

```python
from django.shortcuts import render
from django.views import View

# Create your views here.
class PaintView(View):
    def get(self, request):
        return render(request=request, template_name='hello_world.html')
```

# 10. Create a template

-   In `paintapp` directory create a new directory called `templates`.
-   Inside `templates` create a file called `hello_world.html`.
-   Add the code below in `hello_world.html`:

```html
<h1>Hello World!</h1>
```

# 11. Add `paintapp` urls to `colorpicker` project

Update `urlpatterns` in `colorpicker/urls.py`

```python
"""colorpicker URL Configuration

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
    path('hello/', include('paintapp.urls')), # add this line of code
]
```

Go to `localhost:8000/hello`

# 12. Make the app dynamic!

Add a new a URL that takes a string parameter called `name`. The goal is to have the new page say hello to a different person, depending on the url

### In `paintapp/urls.py`

```python
from django.urls import path

from paintapp.views import HelloWorldView, HelloView

urlpatterns = [
    # paintapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
]
```

### In `paintapp/views.py`

Let's pass this `name` parameter down to the view, then render as a dictionary for the `context` argument

```python
class HelloView(View):
    def get(self, request, name):
        context = {'name': name}
        return render(
            request=request, template_name='hello_name.html', context=context,
        )
```



### In `paintapp/templates/hello_name.html`

Finally, create a new template that will dynamically render the `name` parameter. Remember that this is using a Django template to take in `{{ name }}`, not just regular HTML!

```html
<h1>Hello {{ name }}!</h1>
```

### Check out `localhost:8000/hello/ash` instead!

# 13. Add a `filter` to the template

This will make the name always show up using the django template for 'title' -- first letter caps

```html
<h1>Hello {{ name|title }}</h1>
```

### Try some more examples and see what happens

-   `localhost:8000/paintapp/paul`
-   `localhost:8000/paintapp/serena`
-   `localhost:8000/paintapp/alanna`
-   `localhost:8000/paintapp/yusuf`

# 14. Give a default person to greet

Go to `localhost:8000/hello` and notice that it creates an error...

-   The error `hello() missing 1 required positional argument: 'name'` still requires we provide a value for the `name` parameter. Let's set a default value:

```python
class HelloView(View):
    def get(self, request, name='world'):
        context = {'name': name}
        return render(
            request=request, template_name='hello_name.html', context=context,
        )
```

Go to `localhost:8000/hello` again and make sure it works!

# 15. Make a "goodbye" page

We've given very specific code instructions for the previous steps, but this last one is a little more open-ended. However, you can use what you've learned so far to do this!

- Make an additional "goodbye" page that says "see you later" based on the url, such that going to `localhost:8000/hello/goodbye/django` results in a page as below:
- Don't worry about setting a 'default' person to say 'see you later' to here.

<img src='images/goodbye_page.png'>


# 16. Wrap-up!

- Create a new GitHub repo on GitHub
- Connect your local folder to that repo (rewatch the videos or class video on how to do this, or google it!)
- Add your pod TA as a collaborator to your GitHub repo so that they can check your work (google how!)

**Congrats!!** You've just finished your first Django app of the class!
