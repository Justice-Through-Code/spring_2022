# Class 23 - Objected Oriented Programming

## Before class

* You are familiar with data types, logical statements, loops and functions

## Outline of class agenda

- What is an object?
- Objected Oriented Programming versus Procedural Programming
- How to write Python classes to create objects
- Adding more functionality to objects


# Procedural Programming

We've talked a little bit about how depending on what job you're doing in the future, you might be coding differently. The scripts that are required for [Dev Ops](https://searchitoperations.techtarget.com/definition/DevOps) and [Site Reliability Engineering](https://www.redhat.com/en/topics/devops/what-is-sre) work require a different way of thinking than backend software engineering, which requires a different way of thinking from frontend software engineering, etc etc.

It might surprise you to learn, however, that these differences go beyond particulars of the job-- there are actually multiple methods, or 'paradigms', of coding.

So far, we've been writing code in the style of **Procedural Programming**, i.e. there are steps that we tell our code to do, or _procedures_, in which we write chunks of logic that sometimes edit or manipulate data.

Now not to worry, we won't ever really stop doing this type of coding. Python in particular can blend a variety of different coding paradigms, to use the best of each and ignore the worst. This flexibility is part of what makes python so versatile, but it can also make the rules a little blurry. So let's talk about what exactly our next coding paradigm is.

Let's go back to our restaurant example. Say we're tracking restaurant data to put on Google, and we've been keeping it in dictionaries. We know that we need the same information for each restaurant, something like this:

```python
# Restaurant 'blueprint'
restaurant = {
    'name': '',
    'addresses': [],
    'menu_url': '',
    'hours': {
        'Sunday': [0, 0],
        'Monday': [0, 0],
        'Tuesday': [0, 0],
        'Wednesday': [0, 0],
        'Thursday': [0, 0],
        'Friday': [0, 0],
        'Saturday': [0, 0],
    }
}
```

Each restaurant will need to have a name, at least one address, hopefully a menu url, and hours of operation (the hours of operation could be tracked numerous different ways, here we went with a list of two integers: the hour of opening and the hour of closing, in military time).

Every restaurant object we make should have all of this data filled in. But we may not have all of the info for a give restaurant when we create its dictionary.

Let's make a new restaurant object called islands, where all we know is the name (Islands), and the rest of the data is still the defaults from above--

```python
islands = {
    'name': 'Islands',
    'addresses': [],
    'menu_url': '',
    'hours': {
        'Sunday': [0, 0],
        'Monday': [0, 0],
        'Tuesday': [0, 0],
        'Wednesday': [0, 0],
        'Thursday': [0, 0],
        'Friday': [0, 0],
        'Saturday': [0, 0],
    }
}
```

And now let's create some functions that we might use to go into our restaurant object and update it.

Some functionality that comes to mind that we might need are things like

a) Updating the hours of operation for a given day
b) Checking if the restaurant is open at a given time on a given day

So let's write functions that can do that for us. Let's start at the top.

What information will will we need in order to update the hours of operation for a specific day at a restaurant?

Firstly, we'll need the restaurant object, the dictionary, to update.
Second, we'll need to know which day we're updating.
Lastly, we'll need the new opening and closing times for that day.

^ Those are the _parameters_ our function will need. So:

```python
def update_hours(restaurant_object, day, opening, closing):
    hours_for_day = restaurant_object['hours'][day]
    hours_for_day[0] = opening
    hours_for_day[1] = closing
```

Let's check our work.

```python
islands = {
    'name': 'Islands',
    'addresses': [],
    'menu_url': '',
    'hours': {
        'Sunday': [0, 0],
        'Monday': [0, 0],
        'Tuesday': [0, 0],
        'Wednesday': [0, 0],
        'Thursday': [0, 0],
        'Friday': [0, 0],
        'Saturday': [0, 0],
    }
}


def update_hours(restaurant_object, day, opening, closing):
    hours_for_day = restaurant_object['hours'][day]
    hours_for_day[0] = opening
    hours_for_day[1] = closing


# Use military time to avoid confusion
update_hours(islands, 'Wednesday', 8, 17)

print(islands['hours'])
```

```console
{'Sunday': [0, 0], 'Monday': [0, 0], 'Tuesday': [0, 0], 'Wednesday': [8, 17], 'Thursday': [0, 0], 'Friday': [0, 0], 'Saturday': [0, 0]}
```

Our Wednesday hours have successfully been updated! Great! Let's move onto the next function.

b) Checking if the restaurant is open at a given time on a given day

What information will our second function need in order for us to answer this question?

Again, we will need the restaurant object to check for operating hours. Again, we'll need to know which day we're talking about. And this time, we'll need to know which hour it is that we're checking. So for example, say we want to check if Islands is open at 7am on Wednesdays. And then we also want to check if it's open at noon. Let's write our function.

```python
def is_open(restaurant_object, day, time):
    hours_for_day = restaurant_object['hours'][day]

    # Fancy python functionality-- check if the time is between the opening and closing hours
    return hours_for_day[0] < time < hours_for_day[1]
```

That's it! Let's check it.

```python
print(is_open(islands, 'Wednesday', 7))
print(is_open(islands, 'Wednesday', 12))
```

```console
False
True
```

Got it! So let's take a look at all of our code thus far. We have a standard set of information that we want to track for every single restaurant, those are the attributes that every restaurant shares (they all have names, addresses, hours of operation, etc). And then we have these functions that all operate on a restaurant object. So what that's telling me looking at this code, is that we have the perfect opportunity to use Object Oriented Programming. Let's turn our restaurant dictionary into a `Restaurant` object.

...How do?

## Syntax time!

Remember when we were first talking about data types, and we printed out what `type` of object our integer was?

```python
print(type(9))
```

and we got back

```console
<class 'int'>
```

And we basically said to ignore the word 'class'. No longer! `int` is a type of `class` because `class` is python's key word to build a new type of object. So what does that look like for us?

```python
class Restaurant:
    """An object to track data about Restaurants"""
```

All of the classes (aka objects) that we create should start with a capital letter, to keep with convention.

But we're not done-- remember, we have our 'blueprint' of what should go _in_ each Restaurant object that we create.

Every `class` needs a 'constructor' function, to tell Python what data the `class` is expected to have. The 'constructor' function in python has a special name that is used for every class: `def __init__`. 'init' is short for initialize, because this function initializes each of our restaurant objects. What that means is that whenever we create a `Restaurant` object, this function _always runs_. That's why our defaults go in it.

The double underscores on each side of the word are some 'magic' python syntactical 'sugar', as it's called. The underscores are doing something behind the scenes that we're not going to get into in this class, but it is a google away if you want to look into it.

So what does our constructor take in? For our purposes, all we need to know when we create a restaurant is its name. So what will our constructor look like?

```python
class Restaurant:
    """An object to track data about Restaurants"""

    def __init__(self, name):
```

What is `self`? If we look back at our functional code, each function we wrote to manipulate restaurant data had to take in the `restaurant_object` it was updating. The same is true in our class. And the convention of what we call that object inside of the class, is `self`. This will make more sense honestly in like 6 months, it just takes practice.

So once we have our parameters, what do we do with them? We set our defaults.

```python
class Restaurant:
    """An object to track data about Restaurants"""

    def __init__(self, name):
        """Initialize a Restaurant object with a name and default hours of operation"""
        self.name = name

        # Set defaults
        self.hours = {
            'Sunday': [0, 0],
            'Monday': [0, 0],
            'Tuesday': [0, 0],
            'Wednesday': [0, 0],
            'Thursday': [0, 0],
            'Friday': [0, 0],
            'Saturday': [0, 0],
        }
        self.addresses = []
        self.menu_url = ''
```

Every variable that we want our class to have access to needs to use `self.`. Try to think about it like this-- if the restaurant we're creating is `islands`, we want to keep track of `islands.name`. Inside the class, `self` is `islands`. Again, this will make more sense the more we practice it.

These `self.` variables are called 'attributes' of our class. Because that's what they are-- every restaurant has a name, and hours of operation, that are attributes of that restaurant.

Let's recreate our islands object as a `Restaurant`.

```python
islands = Restaurant('Islands')

print(islands.name)
print(islands.addresses)
print(islands.hours)
```

Boom. Now that we're using a class, all we need is _one line_, `islands = Restaurant('Islands')`, and python knows that all of the attributes in our blue print exist for our restaurant. We don't need to copy-paste the whole dictionary every time we want to create a new restaurant. We just write _one line_, and we're set. In fact, let's create a second restaurant to compare.

```python
islands = Restaurant('Islands')
spudz = Restaurant('Spudz')

print(islands.name)
print(islands.addresses)
print(islands.hours)

print()

print(spudz.name)
print(spudz.addresses)
print(spudz.hours)
```

So fresh. So clean.

And now, for the thing we've been talking about since week 2. We have these functions that update our restaurant dictionaries. but we don't want to be able to send those functions any dictionary of data. We _only_ want them to be run on a restaurant object. So let's move them onto our `Restaurant` class, making them **methods**. Take a look--

```python
class Restaurant:
    """An object to track data about Restaurants"""

    def __init__(self, name):
        """Initialize a Restaurant object with a name and default hours of operation"""
        self.name = name

        # Set defaults
        self.hours = {
            'Sunday': [0, 0],
            'Monday': [0, 0],
            'Tuesday': [0, 0],
            'Wednesday': [0, 0],
            'Thursday': [0, 0],
            'Friday': [0, 0],
            'Saturday': [0, 0],
        }
        self.addresses = []
        self.menu_url = ''

    def update_hours(self, day, opening, closing):
        hours_for_day = self.hours[day]  # No more nested indexing
        hours_for_day[0] = opening
        hours_for_day[1] = closing

    def is_open(self, day, time):
        hours_for_day = self.hours[day]

        # Fancy python functionality-- check if the time is between the opening and closing hours
        return hours_for_day[0] < time < hours_for_day[1]
```

It's pretty similar! But now, we match the constructor method and call the restaurant object `self`, and some things get cleaned up. But the real fanciness here is that our **class methods** cannot be called on any objects other than `Restaurants`. Just like

```python
print('asdfashdouha'.upper())
```

`upper()` can only be called on a string, because it is a _method_ of the _string class_. `is_open` and `update_hours` are now methods of the `Restaurant` class. Let's see them in action:

```python
islands = Restaurant('Islands')
spudz = Restaurant('Spudz')

islands.update_hours('Sunday', 8, 17)
print(islands.hours)
print()
print(f'{islands.name} is open at 9 on Sunday: {islands.is_open("Sunday", 9)}')
print(f'{islands.name} is open at 19 on Sunday: {islands.is_open("Sunday", 19)}')
```

```console
{'Sunday': [8, 17], 'Monday': [0, 0], 'Tuesday': [0, 0], 'Wednesday': [0, 0], 'Thursday': [0, 0], 'Friday': [0, 0], 'Saturday': [0, 0]}

Islands is open at 9 on Sunday: True
Islands is open at 19 on Sunday: False
```

You'll notice that we don't actually send the restaurant object to our methods. We don't send `.upper()` the string as a parameter, either. This is more behind the scenes magic that python is doing, that can be confusing at the start. But it's syntax that you've been using this whole time with string, list, and dictionary methods etc.

Your classes can have as many attributes and methods as you want, just remember that the more complicated it is to read, the more complicated it is to use.

This is a big conceptual jump from what we've been doing thus far. It's gonna take a while to process, and a lot (a LOT) of practice! Keep working on it and you'll get the hang of it, and then one day it'll really click into place. Until then, welcome to OOP!

# Final thoughts

- It is a common pattern seen in Python and other languages to organize complex projects
- Beside procedural and objected oriented programming, there's one more style of coding called functional. We won't be covering it in this course, but it is definitely worth exploring.

# Other Resources

- https://docs.python.org/3/tutorial/classes.html
- https://realpython.com/python3-object-oriented-programming
- https://www.w3schools.com/python/python_classes.asp
