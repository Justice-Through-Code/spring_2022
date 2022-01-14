# Class 23 - Objected Oriented Programming

## Before class

* You are familiar with data types, logical statements, loops and functions

## Outline of class agenda

- Objected Oriented Programming versus Procedural Programming
- How to write Python classes to create objects
- Adding more functionality to objects
 

# Procedural Programming

### So far...
We've been writing code in the style of **Procedural Programming**, i.e. we take blocks of logic and put them inside functions to manipulate data:


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

If want to add more users our code would look like this:


```python
ash = {
    'name': 'Ash',
    'bio': 'Software Developer in NYC',
    'tweets': []
}

def add_tweet(user, text):
        user['tweets'].append(text)
        

add_tweet(ash, 'Today was the longest day of the summer.')

print(ash['name'])
print(ash['bio'])
print(ash['tweets'][0])

paul = {
    'name': 'Paul',
    'bio': 'PhD student at Columbia University',
    'tweets': []
}

add_tweet(paul, 'Cambridge looks great during fall!')

print(paul['name'])
print(paul['bio'])
print(paul['tweets'][0])
```

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

# Final thoughts

- It is a common pattern seen in Python and other languages to organize complex projects
- This will also be instrumental in understanding `pandas` and other Python libraries
- Beside procedural and objected oriented programming, there's one more style of coding called functional. We won't be covering it in this course, but it is definitely worth exploring.

# Other Resources

- https://docs.python.org/3/tutorial/classes.html
- https://realpython.com/python3-object-oriented-programming
- https://www.w3schools.com/python/python_classes.asp


```python

```
