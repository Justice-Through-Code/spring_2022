# Before class

-   Navigate to `mysite` project
-   Run virtual environment

# Outline

In this lesson, we're going to learn how to create a Blog app.

<img width="1680" alt="Screen Shot 2021-10-30 at 1 47 51 PM" src="https://user-images.githubusercontent.com/7483633/139553817-a928edc5-7c3e-497f-8c79-cf888d803739.png">

-   Run a live demo of the Blog app
-   Describe the app by its views, content, URLs and its CRUD-like (Create, Read, Update, Delete) functionality

# Initial setup

Before we start building the app, we must do some initial setup:

## Create `blog` app

```

$ python manage.py startapp blog
$ ls
db.sqlite3 manage.py\* blog/ myapp/ mysite/ sandwich/ todo/

```

## Register `blog` app with the `mysite` project

Edit `mysite/settings.py`

```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'sandwich.apps.SandwichConfig',
    'todo.apps.TodoConfig',
    'blog.apps.BlogConfig'
    ... # Leave all the other INSTALLED_APPS
]
```

## Create `blog/urls.py`

`blog/urls.py`

```python
from django.urls import path

urlpatterns = []
```

## Add `blog` urls to `mysite` project

`mysite/urls.py`

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('sandwich/', include('sandwich.urls')),
    path('todo/', include('todo.urls')),
    path('blog/', include('blog.urls')) # add this line of code
]
```

# Blog models

-   Revisit database design lesson
-   A model translates to one table in the database

## Designing tables

### Posts

| post_id | img_link                          | title        | body                     |
| ------- | --------------------------------- | ------------ | ------------------------ |
| 1       | https://www.somewebsite.com/image | first title  | this is my article       |
| 2       | https://www.somewebsite.com/image | second title | this is my other article |

### Tags

-   Posts have a **many-to-many relationship** with Tags.
-   Typically we would have to create an intermediary table but Django takes care of this complexity for us (more on this soon!)

| tag_id | name            |
| ------ | --------------- |
| 1      | web development |
| 2      | python          |

## Create model

`blog/models.py`

```python
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title =  models.CharField(max_length=255)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
```

## Run migrations

```
$ python manage.py makemigrations
```

```
$ python manage.py migrate
```

# Register model in admin site

-   Log into admin interface
-   We can see database tables here

Let's register the blog models to make it available in the admin site:

`blog/admin.py`

```python
from django.contrib import admin
from .models import Post, Tag

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
```

Refresh the admin site! Now you should see new tables appear on the left:

<img width="277" alt="Screen Shot 2021-10-30 at 2 13 44 PM" src="https://user-images.githubusercontent.com/7483633/139553861-299d5728-c57b-4bf4-a6ad-99f0e928486c.png">

Let's add some entries in these tables!

## Create 2 new tags in the Tags table

-   Web Development
-   Python

<img width="1680" alt="Screen Shot 2021-10-30 at 2 14 44 PM" src="https://user-images.githubusercontent.com/7483633/139553895-5594d793-5255-4f90-a96f-cedaa0206bb9.png">

## Create 2 new posts in the Posts table

<img width="1680" alt="Screen Shot 2021-10-30 at 2 14 57 PM" src="https://user-images.githubusercontent.com/7483633/139553897-f753b6cf-e31b-4700-bc14-ccb082c80022.png">

-   Enter anything you like for title and body
-   Select one or two tags for every post

# Working with Models

Let's run Django's python interactive shell to play around with Models:

```
$ python manage.py shell
```

## Manager

When working with Models, we will be frequently accessing the `Manager` object which is assigned to the `objects` attribute:

```python
>>> from blog.models import Post
>>> Post.objects
<django.db.models.manager.Manager object at 0x10abb5340>
```

The `Manager` object allows us to interact with the database and has a lot of useful methods:

```python
>>> dir(Post.objects)
['__class__', '__class_getitem__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', '_constructor_args', '_db', '_get_queryset_methods', '_hints', '_insert', '_queryset_class', '_set_creation_counter', '_update', 'aggregate', 'alias', 'all', 'annotate', 'auto_created', 'bulk_create', 'bulk_update', 'check', 'complex_filter', 'contribute_to_class', 'count', 'create', 'creation_counter', 'dates', 'datetimes', 'db', 'db_manager', 'deconstruct', 'defer', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'explain', 'extra', 'filter', 'first', 'from_queryset', 'get', 'get_or_create', 'get_queryset', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'name', 'none', 'only', 'order_by', 'prefetch_related', 'raw', 'reverse', 'select_for_update', 'select_related', 'union', 'update', 'update_or_create', 'use_in_migrations', 'using', 'values', 'values_list']
```

Let's run through a few methods:

`Manager.all()` to get all posts in the table:

```python
>>> from blog.models import Post, Tag
>>> Post.objects.all()
<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>]>
```

Running `Post.objects.all()` returns a `QuerySet` object that is an iterable containing all the posts in the Posts table. The shell is great for this purpose! Whenever we run a function, we immediately see what data was returned

`Manager.create()` to create a new post:

```python
>>> Post.objects.create(title='random title', body='here is some content')
<Post: Post object (3)>
```

`Manager.filter()` to filter posts based on specific value(s):

```python
>>> Post.objects.filter(pk=3)
<QuerySet [<Post: Post object (3)>]>
```

## QuerySet

`QuerySet` object also has many [useful methods](), let's run through a few:

`QuerySet.update()` to update field(s) in posts:

```python
>>> Post.objects.filter(pk=3).update(title='better title')
1
```

`QuerySet.delete()` to delete posts:

```python
>>> Post.objects.filter(pk=3).delete()
(1, {'blog.Post': 1})
```

## ManyRelatedManager

Let's look at how we can manage a many-to-many relationship. Let's start by creating a new post:

```python
>>> post = Post.objects.create(title='Learning to set tags', body='Using ManyToManyField')
>>> post
<Post: Post object (4)>
```

If you check the `tags` attribute, it will show that it's a ManyRelatedManger object:

```python
>>> post.tags
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x10ac3fbb0>
```

`ManyRelatedManager.all()` to get all tags in the current post:

Check if there are tags in this Post object:

```python
>>> post.tags.all()
<QuerySet []>
```

`ManyRelatedManager.set()` to set tags in the current post:

ManyRelatedManager has a method called `set()` that allows us to set tags to a post:

```python
>>> tag = Tag.objects.filter(name='Python')
>>> post.tags.set(tag)
>>> post.tags.all()
<QuerySet [<Tag: Tag object (2)>]>
```

Exit the interactive shell:

```python
In [3]: exit()
```

-   We will refer to the [QuerySet](https://docs.djangoproject.com/en/3.2/ref/models/querysets/) documentation throughout this lesson

# Run Django server

```
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 31, 2021 - 21:59:34
Django version 3.2.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Blog home page

Before we get started, let's review the page:

-   This page is at `/blog`
-   This page has a heading - "Ash's Blog"
-   This page has a `Create Post` link
-   This page has a list of posts
-   Each post has an image, title, body, tags and `Edit Post` link for each post

<img width="1680" alt="Screen Shot 2021-10-30 at 1 47 51 PM" src="https://user-images.githubusercontent.com/7483633/139553824-85683516-44ca-4d90-87a9-de3aa218d382.png">

For a jumpstart, the home page is already implemented:

`blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # blog/
    path('', views.blog, name='blog')
]
```

`blogs/views.py`

```python
from django.shortcuts import render
from .models import Post

def blog(request):
    # get QuerySet object containing posts in descending order of post_id
    posts = Post.objects.all().order_by('-post_id')
    return render(request=request, template_name='blog.html', context={ 'posts': posts })

```

`blog/templates/blog.html`

```html
<h1>Ash's Blog</h1>


{% for post in posts %}
<div style="padding: 32px 0px">
    <img style="display: block" src="{{ post.img_link }}" height="200" />
    <a href="">Edit Post</a>
    <h2>{{ post.title }}</h2>
    <p>{{ post.body }}</p>
    <div>
        {% for tag in post.tags.all %}
        <span
            style="color: black; background-color: lightblue; margin-right: 4px"
            >{{ tag.name }}</span
        >
        {% endfor %}
    </div>
</div>
{% endfor %}
```

## Let's test it out!

-   Go to `http:localhost:8000/blog`

# Edit post page

Before we get started, let's review the page. This page has a pre-populated form:

-   'Title' text field
-   'Img link' URL field
-   'Body' textarea
-   'Tags' multiple checkbox fields
-   'Save' button
-   'Delete' button

<img width="574" alt="Screen Shot 2021-10-30 at 1 51 38 PM" src="https://user-images.githubusercontent.com/7483633/139553831-f3eb6453-eadc-4ad4-a456-a69bc7ceea59.png">

## Create route

`blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # blog/
    path('', views.blog, name='blog'),
    # blog/<int:post_id>
    path('<int:post_id>')
]
```

## Create view

`blog/views.py`

```python
def edit(request, post_id):
    if request.method == 'GET':
        return render(request, 'edit.html', { 'post_id': post_id })
```

We will flesh out the view in a bit. Now that we've created a view, let's add it to our URL:

`blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    # blog/
    path('', views.blog, name='blog'),
    # blog/edit/<int:post_id>
    path('edit/<int:post_id>', views.edit, name='edit')
]
```

-   Go to `localhost:8000/blog/edit/1`

## Create form

Let's create the form for the Edit Post page

-   Django lets us handle complex flows around submitting forms to the server
-   We can use Django's form functionality to submit a task securely, validate it before creating an entry in our posts table

`blog/forms.py`

```python
from django import forms

class EditorForm(forms.Form):
    title = forms.CharField(max_length=255)
    img_link = forms.URLField()
    # override the default widget tied to CharField
    body = forms.CharField(widget=forms.Textarea)
     # create tag choices for MultipleChoiceField
    choices = []
    for tag in Tag.objects.all():
        choices.append((tag.tag_id, tag.name))
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=choices)
```

## Create template

`blog/templates/edit.html`

```html
<style>
    /* break form elements into separate lines using CSS */
    input[type='text'],
    input[type='url'],
    textarea {
        display: block;
    }
</style>

<h1>Edit Post</h1>

<form action="{% url 'edit' post_id %}" method="POST">
    {% csrf_token %} {{ form }}
    <input type="submit" name="save" value="Save" />
    <input type="submit" name="delete" value="Delete" />
</form>
```

-   Explain `action` and `method` attributes
-   Explain `csrf_token` is required to make a POST request to Django

## Handle GET requests

`blog/views.py`

```python
from django.shortcuts import render
from .models import Post
from .forms import EditorForm

def edit(request, post_id):
    if request.method == 'GET':
        # get Post object by its post_id
        post = Post.objects.get(pk=post_id)
        # get a list of tag_id from ManyRelatedManager object
        tags = []
        for tag in post.tags.all():
            tags.append(tag.tag_id)
        # pre-populate form with values from Post attributes
        form = EditorForm(initial={
            'title': post.title,
            'body': post.body,
            'tags': tags,
            'img_link': post.img_link
        })
        return render(
            request=request,
            template_name='edit.html',
            context={ 'form': form, 'id': post_id }
        )
```

-   Explain how to work with `EditorForm()` instance
-   Explain that we must access the `Post` object in order to pre-populate the form
-   Go to `localhost:8000/blog/edit/1`

## Handle POST requests

`blog/views.py`

```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import EditorForm

def edit(request, id):
    if request.method == 'GET':
        # get Post object by its post_id
        post = Post.objects.get(pk=post_id)
        # get a list of tag_id from ManyRelatedManager object
        tags = []
        for tag in post.tags.all():
            tags.append(tag.tag_id)
        # pre-populate form with values from Post attributes
        form = EditorForm(initial={
            'title': post.title,
            'body': post.body,
            'tags': tags,
            'img_link': post.img_link
        })
        return render(
            request=request,
            template_name='edit.html',
            context={ 'form': form, 'id': post_id }
        )

    if request.method == 'POST':
        # capture POST data as EditorForm instance
        form = EditorForm(request.POST)
        # validate form
        if form.is_valid():
            # if form was submitted by clicking Save
            if 'save' in request.POST:
                # get cleaned data from form
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                body = form.cleaned_data['body']
                tags = form.cleaned_data['tags']
                # filter QuerySet object by post_id
                posts = Post.objects.filter(pk=post_id)
                # update QuerySet object with cleaned title, body, img_link
                posts.update(title=title, body=body, img_link=img_link)
                # set cleaned tags to ManyRelatedManager object
                posts[0].tags.set(tags)
            # if form was submitted by clicking Delete
            elif 'delete' in request.POST:
                # filter QuerySet object by post_id and delete it
                Post.objects.filter(pk=post_id).delete()
        # redirect to 'blog/'
        return HttpResponseRedirect(reverse('blog'))
```

-   Explain `save` and `delete` come from `name` attributes in the text fields
-   Explain that `EditorForm` instance can be used to validate the incoming POST request form data
-   Explain that `filter()` filters the entries in the table by finding a match for `post_id`
-   Explain that `update()` updates an existing entry in the table
-   Explain that `set()` sets new tags to the Post object
-   Explain that `delete()` deletes an existing entry in the table
-   Explain `HTTPResponseRedirect()`
-   Explain `reverse()`

## Let's test it out!

-   Go to `http:localhost:8000/blog/edit/1`

# Conclusion

In this lesson we covered more concepts in Django:

-   Managing one-to-many and many-to-many relationships between models
-   How to use various interfaces to work with models
-   Working with other types of data in our models and the related form fields
