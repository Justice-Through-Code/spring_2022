# 1. Refresh students on OOP
* Classes
* In particular, we're learning how *to create our own custom classes*

# 2. What is inheritance?

* Introduce concepts of **parent class** and **child class**
* Children "inherit" attributes and methods from parents, but can have their own unique features
    * Parent class `Vehicle` with children `Car` and `Motorcycle`


# 3. Making a parent & child class

* A parent class isn't anything special, any class can *become* a parent class if it is used for child classes

## Instruments as an example

* Parent class `Instrument` with children `Guitar` and `Drums`


First make the `Instrument` parent class
```python
class Instrument():
    def __init__(self, volume):
        self.volume = volume

    def display_info(self):
        print(f'Instrument set to volume {self.volume}')
```


Now, make the `Guitar` child class, even with no additional attributes. Explain how `Guitar` "inherits" from `Instrument`


```python
class Guitar(Instrument):
  pass
```

# 4. Show students that the parent/child can be used identically so far:

```python
instrument1 = Instrument('11')
instrument2 = Guitar('11')
instrument1.display_info()
instrument2.display_info()
```

We get the same output

```console
Instrument set to volume 11
Instrument set to volume 11
```

# 5. Adding the `__init__()` function to the child class

* Explain that if the child class has its own `__init__()` function, it will no longer *inherit* the parent's version of this.
* Explain that to be able to have **new attributes**, a child class must have a new init function

## Add an `__init__()` function for the `Guitar` class

* Here, we add a new attribute `electric` for the child `Guitar` class
* Emphasize that we still need to create the `volume` attribute in this case (or demonstrate that the `Guitar` class will not have `volume` if we don't include it here)

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        self.volume = volume
        self.electric = electric
```

* Show students that only a `Guitar` has the `electric` attribute, but not `Instrument` more generally
* Emphasize that parent/child classes can have different attributes, may need to be instantiated differently

```python
instrument1 = Instrument(volume = '11')
instrument2 = Guitar(volume = '11', electric = False)
print(instrument2.electric)
print(instrument1.electric)
```

Output

```console
False
Traceback (most recent call last):
  File "inheritance_demo.py", line 30, in <module>
    print(instrument1.electric)
AttributeError: 'Instrument' object has no attribute 'electric'
```

## 6. Inheriting the `__init__()` function from the parent class

* Explain that the drawback to the previous example is that we had to repeat things again already created in the parent class.
* If we *inherit* the `__init__()` function, that gives a better place to work from

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        Instrument.__init__(self, volume)
        self.electric = electric
```

## 7. Generalized inheritance using the `super()`

* Show students that for any child class, we can inherit using the `super()` function to implicitly inherit the parent class' attributes and methods without naming it again

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric
```


## 8. Adding methods specific to a child class

* We add a new `tune()` method for the `Guitar` child class, but note that it does not apply to the `Instrument` class more broadly
* Note that the method name is *not the same* as any method in the parent class

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric

    def tune(self):
        print('Guitar is in tune now!')
```

## 9. Overriding a method from the parent class

* Explain that we can make a *different version* of the same method in the child class by "overriding" the method from the parent class
* Here, we override the `display_info()` method to display guitar-specific information


```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric

    def display_info(self):
        print(f'Guitar set to volume {self.volume}')
        if self.electric:
            print('Guitar is electric!')
        else:
            print('Guitar is acoustic!')
```

Instantiate them

```python
instrument1 = Instrument(volume = '11')
instrument2 = Guitar(volume ='11', electric=True)

instrument1.display_info()
instrument2.display_info()
```

We get different outputs for the `display_info()` method for the `Instrument` vs. `Guitar`

```console
Instrument set to volume 11
Guitar set to volume 11
Guitar is electric!
```

# 10. Multiple children with the same parent

* Explain parent can have multiple child classes
* Make a new class `Drums` that also inherits `Instrument`

```python
class Drums(Instrument):
    def __init__(self, volume):
        super().__init__(volume)

    def play(self):
        print('boom boom bap!')
```

Neither `Guitar` nor `Instrument` have the `play()` method yet


# Multiple inheritance

* Demonstrate that one class can inherit from *multiple* other parent classes
* `Guitar` inherits from `Instrument` and `Luggage`

```python
class Luggage():
    item_type = 'luggage'
    def __init__(self, weight):
        self.weight = weight

class Guitar(Instrument, Luggage):
    def __init__(self, volume, electric, weight):
        Instrument.__init__(self, volume)
        Luggage.__init__(self, weight)
        self.electric = electric

    def display_info(self):
        print(f'Guitar set to volume {self.volume}')
        if self.electric:
            print('Guitar is electric!')
        else:
            print('Guitar is acoustic!')

g = Guitar(volume = 11, electric = False, weight = 20)

print(g.electric, g.volume, g.weight, g.item_type)
```

## Why is this relevant?
* Inheritance is a key part of a lot of software, particularly when the software needs custom data structures to keep track of info
* We are later going to use inheritance when working with ["Class-based views in Django"](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)


Let's think about the data that a school like Columbia needs to keep track of for its students.
What are some pieces of data that they might need to know?

- Name (first, last)
- Student ID
- Major
- Class list
- email address

That's a lot of data to keep track of for each student. So far with our procedural programming, what data type have we learned about that could hold all of this information for each student?

A dictionary. Let's see this in action:

student_1 = {
    'name': {'first': 'Lillie' 'middle_initial': 'S', 'last': 'Schachter'},
    'student_id': 8923,
    'major': 'Computer Science',
    'email_address': 'lillie.schachter@gmail.com',
    'class_list': ['Data Structures', 'Discrete Math', 'Intro to Sociology', 'Web Development']
}

Yeah, that's a lot of data! And to access it, we have to already know what keys are in there. What if I was expecting there to be a payment method in my student dictionary? What if I had a thousand students, each with their own dictionary like this, and suddenly I had to go through and add a payment method to every single dictionary? We know how to do this (for loop!), but at a certain point, we're going to have to accept that there might be a better way to keep track of all this data.




We have seen versions of this code before like the music playlist challenges. However, there are other styles of programming! Here's the same code but applying concepts of **Objected Oriented Programming**:


```python
class TwitterUser():
    def __init__(self, name, bio):
        self.name = name
        self.bio = bio
        self.tweets = []

    def add_tweet(self, text):
        self.tweets.append(text)

ash = TwitterUser('Ash', 'Software Developer in NYC')
ash.add_tweet('Today was the longest day of the summer.')

paul = TwitterUser('Paul', 'PhD student at Columbia University')
paul.add_tweet('Cambridge looks great during fall!')

print(ash.name)
print(ash.bio)
print(ash.tweets[0])
print(paul.name)
print(paul.bio)
print(paul.tweets[0])
```

The key changes in how we code here are the following lines:


```python
ash = TwitterUser('Ash', 'Software Developer in NYC')
ash.add_tweet('Today was the longest day of the summer.')
```

The creation of a user is simpler and the `add_tweet` function is now tied to that user (similar to functions we learned that are attached by the dot notation to data type like `list.append()` or `str.capitalize()`

# Objected Oriented Programming

Before we dig deeper into the syntax, here's the key idea behind OOP:
- We combine data (name, bio, tweets) and functionality (add_tweet) and wrap it inside something called an **object**. The user `ash` and `paul` are now objects.
- Objects are created from a blueprint (TwitterUser) called a **class** that dictates data and functionality the objects would contain
- When you're writing large programs or have a problem that is better suited to this method, you can use object oriented programming technique

## Creating a class


```python
class Person():
    pass
```

## Adding an attribute


```python
class Person():
    def __init__(self, name):
        pass
```

`def __init__(self):` is an initialization function. This is where we setup **attributes**. We can think of attributes as key/value pairs of a dictionary.


```python
class Person():
    def __init__(self, name):
        self.name = name
```

`self` refers to the object that will be created from the class blueprint. This object creation is also called instantiating a class. `self.name` will be assigned a name during instantiation.

## Instantiating a class or creating an object from a class


```python
# name gets assigned to self.name
person = Person('Mattan')
# person.name now contains 'Mattan'
print(person.name)

# name gets assigned to self.name
person_2 = Person('Yusuf')
# person_2.name now contains 'Yusuf'
print(person_2.name)
```

## Adding a method or a function to a class


```python
class Person():
  def __init__(self, name):
    self.name = name

  # greeting function is a method of Person class
  def greeting(self):
    return f'Hello, my name is {self.name}'

person = Person('Mattan')

print(person.greeting()) # 'Hello, my name is Mattan'
```

## Checking types


```python
print(person)
print(type(person))
print(type(person) == Person)
```

## Updating Person class
Let's add an additional detail in the greeting output:


```python
print(person.greeting()) # 'Hello, my name is Mattan and I am 28 years old'
```

**Implementation**


```python
class Person():
    def __init__(self, name, age):
        self.name = str(name)
        self.age = int(age)

    def greeting(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'

person = Person('Mattan', 28)

print(person.greeting()) # 'Hello, my name is Mattan and I am 28 years old'
```

## Let's dive deeper with other data types



```python
class Cart():
    def __init__(self):
        self.items = []

    def add(self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)

cart = Cart()

# add a few items
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.items) # [{'name': 'oreos', 'price': 12}, {'name': 'bananas', 'price': 2}]
```

## Adding more functionality

Let's create a method `total` that returns the total of all items added to Cart including a `$` before it:


```python
cart.add('oreos', 12)
cart.add('bananas', 2)
print(cart.total()) # $14
```


```python
class Cart():
    def __init__(self):
        self.items = []

    def add(self, name, price):
        item = {}
        item['name'] = name
        item['price'] = price
        self.items.append(item)

    # total function goes here
    def total(self):
        cart_total = 0
        # self.items allows us to access the items list local to the object
        for item in self.items:
            cart_total += item['price']
        return f'${cart_total}'

cart = Cart()
cart.add('oreos', 12)
cart.add('bananas', 2)

print(cart.total())
```