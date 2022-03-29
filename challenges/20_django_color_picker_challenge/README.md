# Django challenge: Color Picker

In this challenge, you'll create a new django project called 'Color Picker'.

# 1. Get set up for Django

* First, go to your `django-projects` directory
- Create a new folder called `color-picker-container` and `cd` into it
- Run `python3 -m venv venv` (or whichever version of this your computer uses) to create a new virtual environment (it's common practice to name your virtual environment 'venv')
- Run `source django-env/bin/activate` on Unix/MacOS or `django-env\Scripts\activate.bat` on Windows to activate the virtual environment (or whichever instruction works for you!)
- Run `pip install django` to install Django
- Run `pip freeze > requirements.txt` (take a look at the new requirements file that popped up!)


# 2. Initialize your git instance and .gitignore file

In your terminal, initialize a new instance of git with

```
$ git init
```

Without changing what directory you're in, create a new file called `.gitignore` (note the `.` at the start of the file name). Any files or folders that you specify in your `.gitignore` file will be completely ignored by git, meaning you won't be able to add, commit, or push them. This helps us keep our git repos clean from files that are local to our computers. Particularly, things like our `venv` folders, our `db.sqlite3` files, and more, we do NOT want to push to GitHub. So we can add them to our `.gitignore` file and never have to worry about them again.

By simply googling `gitignore python`, you can find a commonly used `.gitignore` file that has everything we'll need (and more). Feel free to copy-paste directly from [this file](https://github.com/github/gitignore/blob/main/Python.gitignore) into your `.gitignore` (this is what open source is for!). Now you can keep committing your code without worrying about cluttering up your GitHub repo.

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

# 8. Create your Django form

This time around, we'll need a 4th element to make our website do what we want: a django `form`. In our `paintapp` directory, create a new file called `forms.py`. Create your form here:

```python
from django import forms


class ColorPickerForm(forms.Form):
    red_amount = forms.IntegerField(label='Red Value', min_value=0, max_value=255, required=True)
    green_amount = forms.IntegerField(label='Green Value', min_value=0, max_value=255, required=True)
    blue_amount = forms.IntegerField(label='Blue Value', min_value=0, max_value=255, required=True)
```

# 9. Create the view

Open `paintapp/views.py`. It will initially look like this:

```python
from django.shortcuts import render

# Create your views here.
```

Let's add some code to pull in our django form and send it to our html template

```python
from django.shortcuts import render
from django.views import View

from color_maker.forms import ColorPickerForm


# Create your views here.
class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'color_picker.html', context=context)
```

We're sending the form, as well as our default numbers for the color of our page. rgb(255, 255, 255) is white!

# 10. Create a template

-   In the `paintapp` directory, create a new directory called `templates`.
-   Inside `templates`, create a file called `paint.html`.
-   Add the code below in `paint.html`:

Let's add some more of our standard html this time around--

```html
<html>
<head>
    <title>Color Picker</title>
</head>
<body></body>
</html>
```

Now let's use the variables we have in our `context` to fill this out a bit more.

We can change the color of our page to anything we want by adding a CSS style to our body tag and using the rgb function to pick a color.

```html
<html>
<head>
    <title>Color Picker</title>
</head>
<body style="background-color: rgb(40, 100, 100);"></body>
</html>
```

Let's finish up adding our url to see if this works as expected.

# 11. Create a URL for the "color picker" app

In your `paintapp` directory, create a file called `urls.py` as below:

```python
from django.urls import path

from paintapp.views import PaintView

urlpatterns = [
    # paintapp/
    path('', PaintView.as_view(), name='paint'),
]
```

It's best practice for each app to have its own url file, that we connect to the overarching site's url file as one unit.

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
from django.urls import include, path  # add `include` to import it from this library

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paint/', include('paintapp.urls')),  # add this line of code
]
```

Go to `localhost:8000/paint`

Is our page a different color?? Change the numbers in your CSS and reload the web page to see it change.


# 12. Use our context variables

Now that we have our page showing up, we can actually use the context we sent to our html template. Let's update the CSS to use whatever colors we send it from the View.

```html
<html>
<head>
    <title>Color Picker</title>
</head>
<body style="background-color: rgb({{ red }}, {{ green }}, {{ blue }});"></body>
</html>
```

This is taking our variables from our context dictionary and using Django templating language to insert them into our code, just like we did with `{{ name }}` last night.

Change the numbers in our _view_ this time around and reload the page to make sure it works.

Now let's use our `form`! There are many ways to do this, but let's follow this one for now:

```html
<html>
<head>
    <title>Color Picker</title>
</head>
<body style="background-color: rgb({{ red }}, {{ green }}, {{ blue }});">
    <div >
        <h2>Enter a number between 0 and 255 for each color below</h2>
        <form method="POST" action="{% url 'paint' %}">
            {% csrf_token %}
            <div>
                {{ form.red_amount.label_tag }}
                {{ form.red_amount }}

                {{ form.green_amount.label_tag }}
                {{ form.green_amount }}

                {{ form.blue_amount.label_tag }}
                {{ form.blue_amount }}
            </div>
            <div>
                <button type="submit">
                    Paint
                </button>
            </div>
        </form>
    </div>
</body>
</html>
```

A few things to note:
- `{% csrf_token %}` is a security thing that we need to add manually basically as an interim step until django developers fix it more directly. You can google what a csrf token is to learn more if you'd like!
- We are creating a `<form>` object here just like regular HTML code. When a user 'submits' this form (by pressing the 'Paint' button), we are going to make a POST call to the server, to send it the numbers that the user chose.
- We are using Django templating language to make the `action` send us to our url that we named 'paint'.
- Then in the form content itself, we're displaying the label and the field of each piece of our form. You can look back at your `form.py` file to see that `red_amount`, `green_amount`, and `blue_amount` are the names of our three fields. We access them here as part of the `form` variable that we have in our `context` dictionary.
- Then, we end our form with a button of type 'submit', that let's the code know that when we hit the button, we want to submit the data in the form, via the 'action' we set above.


Let's reload our page to see if it worked!

# 13. Actually taking in data

Our form shows up! But when we put data into it and hit submit, what happens? Nothing!

We haven't set up View logic to handle a POST request, just a GET. So we aren't sending our form data back to the server to update the page color with. Let's do that now.

### In `paintapp/views.py`

We don't need to create a new class, because we're going to be POSTing to the same url that we already have. Instead, let's add a post method to our existing view--

```python
class ColorPickerView(View):
    def get(self, request):
        """Present the color picker form and color the user"""
        form = ColorPickerForm()

        context = {
            'form': form,
            'red': 255,
            'green': 255,
            'blue': 255,
        }

        return render(request, 'color_picker.html', context=context)


    # This is the new content
    def post(self, request):
        """Display the user's chosen color"""
        form = ColorPickerForm(request.POST)

        red = int(request.POST['red_amount'])
        green = int(request.POST['green_amount'])
        blue = int(request.POST['blue_amount'])

        context = {
            'form': form,
            'red': red,
            'green': green,
            'blue': blue,
        }

        return render(request, 'color_picker.html', context=context)
```

This time, we're going to collect the POST data (sent to Django in the `request` object as `request.POST`), and send it to our form to update the numbers that show up in it. We are also going to take the data in the POST object and send them into our context for our CSS to use, to actually update the color of our page.

# 14. See it in action

We should now have all the pieces in place for our form to execute as expected. Let's try it out!


# 16. Wrap-up!

- Create a new GitHub repo on GitHub
- Connect your local folder to that repo (rewatch the videos or class video on how to do this, or google it!)
- Add your pod TA as a collaborator to your GitHub repo so that they can check your work (google how!)
- Add the link to your GitHub repo on Canvas like you did for the Tip Calculator

**Congrats!!**
