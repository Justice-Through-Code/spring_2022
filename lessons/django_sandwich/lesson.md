# Outline

We're going to learn how to create a Sandwich Generator.

Describe the application by its three pages (home, ingredients list, sandwich generator) and their content, functionality and URLs.

# Run Django server

-   Navigate to `mysite` project we created in the previous lesson.
-   Make sure `manage.py` exists in the directory

```
$ ls
manage.py*  mysite/
```

Then run the server

```
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 05, 2021 - 21:15:29
Django version 3.2.4, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Initial setup

Before we start building the three pages, we must do some initial setup:

## Create `sandwich` app

```

$ python manage.py startapp sandwich
$ ls
db.sqlite3 manage.py\* myapp/ mysite/ sandwich/

```

## Register `sandwich` app with the `mysite` project

Edit `mysite/settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'sandwich.apps.SandwichConfig',
    ... # Leave all the other INSTALLED_APPS
]
```
* Show students that the `SandwichConfig` class has been automatically set up in `apps.py` in the `sandwich` app (and that it inherits `AppConfig` -- django is doing a lot to set up the app for you!)
## Create `sandwich/urls.py`

`sandwich/urls.py`

```python
from django.urls import path

urlpatterns = []
```

## Add `sandwich` urls to `mysite` project

`mysite/urls.py`

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
    path('myapp/', include('myapp.urls')),
    path('sandwich/', include('sandwich.urls')), # add this line of code
]
```

# Sandwich home page

Before we get started, let's review the page:

-   This page is at `/sandwich`
-   This page has a heading - "Sandwich home"
-   This page has a list of hyperlinks - meats, cheeses, toppings
-   This page has a button - "Make a sandwich!"

<img width="1678" alt="Screen Shot 2021-10-08 at 9 58 36 AM" src="https://user-images.githubusercontent.com/7483633/136570008-626c874a-0d54-404f-9b31-a92fe5b3698e.png">

## Create route

`sandwich/urls.py`

-   The `path` function takes two more arguments, the Django `view` which we will create next and a `name` for the URL

```python
from django.urls import path
from your_app_name.views import SandwichView, IngredientsView, SandwichGeneratorView

urlpatterns = [
    # sandwich/
    path('', SandwichView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
]
```

## Create view

`sandwich/views.py`

```python
from django.shortcuts import render
from django.http import Http404
from django.views import View
import random


class SandwichappView(View):
    def get(self, request):
        if request.method == 'GET':
            return render(
                request = request,
                template_name = 'sandwichapp.html',
                context = {'ingredients': ingredients.keys()}
            )

```

Now that we've created a view, let's add it to our URL:

`sandwich/urls.py`

```python
from django.urls import path
from <your_app_name>.views import SandwichappView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
]
```

Since we want the sandwich homepage to have hyperlinks to ingredients, let's create our ingredients data by creating our IngredientsView class in views.py:

```python

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type}')

            return render(
                request = request,
                template_name = 'ingredients_list.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type }
            )
```

## Create template

-   Create a directory called `templates` in `sandwich` directory
-   Create an HTML file `sandwich.html` in `templates`

`sandwich/templates/sandwich.html`

-   We can use built-in [for loop template tag](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#for) to iterate over `ingredients` list

```html
<h1>Sandwich Home</h1>

<h3>Ingredients</h3>

<ul>
    {% for ingredient in ingredients %}
    <li>
        <a href="/sandwich/ingredients/{{ ingredient }}">{{ ingredient }}</a>
    </li>
    {% endfor %}
</ul>

<p>Click the button if you are hungry!</p>

<form action="/sandwich/random">
    <input type="submit" value="Make a sandwich!" />
</form>
```

## Let's test it out!

-   Go to `http:localhost:8000/sandwich`
-   Clicking the hyperlinks don't take us anywhere, let's build the ingredients list page next.

# Ingredients list page

Before we get started, let's review the page:

-   This page is at `/sandwich/ingredients/meats`, `/sandwich/ingredients/cheeses`, `/sandwich/ingredients/toppings`.
    -   If we try a URL with a random string instead of `meats, cheeses or toppings`, we'll get a 404 error.
-   This page has a heading - "Meats", "Cheeses", "Toppings"
-   This page has a unordered list of all the ingredients
-   Although it may seem like it, these are not three different pages. We can avoid repeating ourselves by creating a template that can render a heading and an unordered list for us

<img width="1679" alt="Screen Shot 2021-10-08 at 9 56 17 AM" src="https://user-images.githubusercontent.com/7483633/136570085-a0c83105-fcd3-4e37-95b0-506f41a5909f.png">

## Create route

`sandwich/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # sandwich/
    path('', views.sandwich, name='sandwich'),
    # sandwich/ingredients/<str:ingredient_type>
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
]
```

## Create view

`sandwich/views.py`

-   Let's create a `ingredients` dictionary so that we can look up the `ingredient_type` on a `GET` request to the URL
-   Since we created key names `meats`, `cheeses`, `toppings` for `ingredients` dictionary, we can avoid redundancy in `sandwich` view and pass `ingredients.keys()` instead of the list we originally created as its context

```python
from django.shortcuts import render

ingredients = {
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'tomato', 'onions', 'peppers', 'pickles']
}


class SandwichappView(View):
    def get(self, request):
        if request.method == 'GET':
            return render(
                request = request,
                template_name = 'sandwichapp.html',
                context = {'ingredients': ingredients.keys()}
            )


class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            return render(
                request = request,
                template_name = 'ingredients_list.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type }
            )

```

Now that we've created a view, let's add it to our URL:

`sandwich/urls.py`

```python
from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
]
```

## Create template

-   Create an HTML file `ingredients_list.html` in `templates`

`sandwich/templates/ingredients_list.html`

```html
<h1>{{ ingredient_type|title }}</h1>

<ul>
    {% for ingredient in ingredients %}
    <li>{{ ingredient }}</li>
    {% endfor %}
</ul>
```

## Let's test it out!

-   Go to `http:localhost:8000/sandwich/ingredients/meats`
-   Go to `http:localhost:8000/sandwich/ingredients/cheeses`
-   Go to `http:localhost:8000/sandwich/ingredients/toppings`
-   Also, try using the hyperlinks at `http:localhost:8000/sandwich`

## Create a custom 404 message

We can create a custom 404 error if a user tries to look up an `ingredient_type` that doesn't exist--e.g., `/sandwich/ingredients/bread`

`sandwich/views.py`

Let's import `Http404`

```python
from django.http import Http404
```

Raise `Http404` if `ingredient_type` passed does not exist:

```python

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if request.method == 'GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type}')

            return render(
                request = request,
                template_name = 'ingredients_list.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type }
            )
```

## Let's test it out!

-   Go to `http:localhost:8000/sandwich/ingredients/bread`

# Sandwich generator page

Before we get started, let's review the page:

-   This page is at `/sandwich/random`
-   This page has a heading with a random sandwich combo
-   This page has a paragraph with an instruction to refresh the page for a new sandwich combo
-   Refresh the page to show that a new random sandwich combo is created each time

<img width="1678" alt="Screen Shot 2021-10-08 at 9 56 58 AM" src="https://user-images.githubusercontent.com/7483633/136570201-4d7831bd-df14-4f72-b1bd-4dc046fa2c87.png">

## Create route

```python
from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
]
```

## Create view

To randomize our selections of meats, cheeses and toppings, let's import `random`:

```python
from django.shortcuts import render
from django.http import Http404
from django.views import View
import random
```

```python

class SandwichGeneratorView(View):
    def get(self, request):
        if request.method == 'GET':
            selected_meat = random.choice(ingredients['meats'])
            selected_cheese = random.choice(ingredients['cheeses'])
            selected_toppings = random.choice(ingredients['toppings'])

            sandwich = f'{selected_meat} & {selected_cheese} with {selected_toppings}'
            return render(request, 'sandwich_generator.html', context = { 'sandwich' : sandwich})        
```
* While you're developing a class like this, you can use print statements to debug -- making sure your classes in `views.py` are working correctly internally before examining their output in HTML
Now that we've created a view, let's add it to our URL:

`sandwich/urls.py`

```python
from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    # sandwich/
    path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
]
```

## Create template

-   Create an HTML file `sandwich_generator.html` in `templates`

`sandwich/templates/sandwich_generator.html`

```html
<h1>{{ sandwich|title }}</h1>
<p>Keep refreshing the page for a new sandwich!</p>
```

## Let's test it out!

-   Go to `http:localhost:8000/sandwich/random` and keep refreshing!

# Dynamic URLs

-   We can use a built-in [url template tag](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#url) to make the URLs in our hyperlinks more DRY
-   This way if we were to change our URL paths `urls.py`, we wouldn't have to go to every file where we've hardcoded the URLs to change them

```html
<h1>Sandwich Home</h1>

<h3>Ingredients</h3>

<ul>
    {% for ingredient in ingredients %}
    <li>
        <a href="{% url 'ingredients_list' ingredient %}">{{ ingredient }}</a>
    </li>
    {% endfor %}
</ul>

<p>Click the button if you are hungry!</p>

<form action="{% url 'sandwich_generator' %}">
    <input type="submit" value="Make a sandwich!" />
</form>
```

# Conclusion

In this lesson we covered more concepts in Django:

-   Passing context data from our views to the template
-   More template syntax to make HTML dynamic
    -   Rendering lists with for loop like syntax
    -   Rendering dynamic URLs for hyperlinks
-   Created a custom 404 page message
