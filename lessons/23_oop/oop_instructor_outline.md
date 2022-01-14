# 1. Define Procedural Programming

## So far...

* We've been writing code in the style of **Procedural Programming**, i.e. we take blocks of logic and put them inside functions to manipulate data:
* Show students the below code as an example, and explain that if we want add more twitter users, staying organized can start to get really difficult

```python
ash = {
    'name': 'Ash',
    'bio': 'Software Developer in NYC',
    'tweets': []
}

def add_tweet(user, text):
        user['tweets'].append(text)
        

add_tweet(ash, 'Today was the longest day of the summer.')

print(ash['tweets'][0])
```


# 2. Introducing Objected Oriented Programming

Key idea behind OOP: 
- We combine data and functionality and wrap it inside something called an **object**. 
- Objects are created from a blueprint called a **class** that dictates data and functionality the objects would contain. 
    - In fact, the primitive data types, lists, and dictionaries are all built-in classes in python
    - Today we'll learn to make our own classes
- OOP (and making your own classes) especially useful with large programs where you need custom data types / functionality

# 3. Creating a class

* Class names are usually capitalized to keep them distinct from variable names

```python
class Person():
    pass
```

# 4.  The `__init__()` function

* `def __init__(self):` is an initialization function. This is where we set up **attributes**. 
* We can think of attributes as key/value pairs of a dictionary. 


```python
class Person():
    def __init__(self, name):
        pass
```

# 5. Setting up an attribute within the `__init__()` function

* Explain that `self` always refers back to the class (technically, the 'instance' of that class)
* `self` refers to the object that will be created from the class blueprint. This object creation is also called instantiating a class. `self.name` will be assigned a name during instantiation.

```python
class Person():
    def __init__(self, name):
        self.name = name
```


# 6. Instantiating a class or creating an object from a class

* Now we make an actualy "instaace" of the class. You can compare this to defining vs. running a function
* Explain that now `person` (the variable name), becomes `self` now that the class has been instantiated


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

## Review the differences between creating a class and instantiating it

* We only create a given class once, but we can instantiate it many times (give examples -- people, twitter users, tweets)

# 7. Adding a method or a function to a class

* A function specific to a class is called a **method** of that class
* Methods are always used with the `.method_name()` syntax (for example, the `.append()` method for a list)

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

# 8. Checking types

* Show that we can check an object's type against custom classes


```python
print(person)
print(type(person))
print(type(person) == Person)
```

# 9. Adding more attributes

* Show how to add an additional `age` attribute to the class


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

# 10. A grocery cart class with an `add()` method

* Show this as an example for creating a method that updates the data within the already instantiated object

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

# 11. A method with a loop in it: getting the cart total price

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

# 12. Adding attributes outside of  the `__init__()` function

* Explain that this can be a way to hard code attributes for all instantiations

```python
class Person:
    role = 'Teacher'
    def __init__(self, name):
        self.name = name

Person('Ash').role # 'Teacher'
Person('Ash').name # 'Ash'
```


# Final thoughts

- Object-oriented programming (OOP), especially defining and organizing custom classes, is the backbone of many development projects
- Making custom classes is especially useful when projects get large
- You'll make heavy use of OOP when making a Django full-stack app
