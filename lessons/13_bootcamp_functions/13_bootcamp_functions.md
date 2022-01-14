# Bootcamp class 13 - Functions

<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

- Make sure you feel comfortable with all primitive data types, lists and dictionaries
- Make sure you feel comfortable with both logical operations and conditional statements
- Make sure you feel comfortable with loops

# Outline of class agenda

Today we'll learn about **functions** in python. By the end of the lesson, you'll:

1. Feel comfortable creating and using functions to group lines of code
2. Know how to add parameters to functions to make functions more flexible
3. Know how a return statement works and how it differs from print
4. Know where to look for python's built-in functions

# What is a function?

A **function** is a block of code that only runs when it's called. Using functions we can:

- Reduce the need for copying and pasting block of code that is frequently written in a program
- Thinking of a program as series of procedures or steps where function names are the names for those procedures

# 1. Function syntax

_Let's make a script `bootcamp_scripts/functions_practice.py` to practice working with functions._

Here is a line of code we have seen before:

```python
print('Hello World')
```

Let's introduce function syntax:

```python
# start of function
def say_hello():
    # block of code
    print('Hello World')
# end of function

# invoke or call the function
say_hello()
# invoke or call the function
say_hello()
```

Output:

```console
Hello World
Hello World
```

### How it works

When creating a function, we can indent lines of code that we want to re-use. Every time we invoke or call the function later, we are running those lines of code. This way never have to repeat ourselves!

Let's add more print statements to `say_hello` function:

```python
# start of function
def say_hello():
    # block of code
    print('Hello World')
    print('Good Morning')
    print('And Good Night')
# end of function

# invoke or call the function
say_hello()
# invoke or call the function
say_hello()
```

Output:

```console
Hello World
Good Morning
And Good Night
Hello World
Good Morning
And Good Night
```

### Functions in the wild

We can also nest function calls inside of other python code:

```python
say_hello()

# if/else
if 1 < 2:
    print('1 is less than 2')
    say_hello()
else:
    print('1 is not less than 2')

# for loops
for num in range(100):
    print(num)
    say_hello()
```

(See output in command line)

# 2. Parameters

Sometimes you will want your code to be more flexible. Let's say we want the following output in our command line:

```console
Hello Ash
Good Morning
And Good Night
Hello Paul
Good Morning
And Good Night
```

One way to do it would be to create two functions:

```python
def say_hello_ash():
    print('Hello Ash')
    print('Good Morning')
    print('And Good Night')

def say_hello_paul():
    print('Hello Paul')
    print('Good Morning')
    print('And Good Night')

say_hello_ash()
say_hello_paul()
```

But we can do better. We could create another function:

```python
def say_morning_night():
    print('Good Morning')
    print('And Good Night')

def say_hello_ash():
    print('Hello Ash')
    say_morning_night()

def say_hello_paul():
    print('Hello Paul')
    say_morning_night()

say_hello_ash()
say_hello_paul()
```

Not bad, but once we have more names to print, we would have to create more functions that look like `say_hello_ash` and `say_hello_paul`. Imagine trying to do that for a thousand names. Luckily, functions have something called **parameters** that will dramatically cut down the number of lines of code we have to write to accomplish this task.

```python
def say_hello(name):
    print(f'Hello {name}')
    print('Good Morning')
    print('And Good Night')

say_hello('Ash')
say_hello('Paul')
```

### How it works

`name` here is called a **parameter**. A parameter is like a variable, we can call it anything we want, but the main idea is that it contains a reference to a value. When we call `say_hello('Ash')`, `name` is a parameter referring to the string value `Ash` which then gets printed as `Hello Ash`.

A parameter can reference any data type we have learned so far.

```python
def times_two(num):
    # parameter num is an int or a float
    print(num*2)

times_two(4) # 8
times_two(4.0) # 8.0

def first_num(nums):
    # print first value in nums list
    print(nums[0])

first_num([100, 233, 443]) # 100

more_nums = [133, 445, 667, 88]
# pass a variable containing a list
first_num(more_nums) # 133
```

### Multiple parameters

Parameters are powerful! Even better: we can have more than one parameter.

```python
def multiply(a, b):
    print(a*b)

multiply(2, 3) # 6
```

In order to apply more than one parameter for our function, we need to separate the parameter names by a comma. Here's another example:

```python
def greeting(first_name, middle_name, last_name):
    print(f'Hi, {first_name} {middle_name} {last_name}')

greeting('George', 'Orson', 'Welles') # Hi, George Orson Welles
```

### Argument

The specific value that is passed to the function at the time of calling a function is called an **argument**. Parameter is the variable between the parenthesis at the time of the function declaration.

```python
def times_two(num):
    # num is a parameter
    print(num*2)

# 2 is the argument
times_two(2)
```

### Default arguments

Functions can also take a default argument for a parameter.

```python
def ice_cream(flavor='chocolate'):
    print(f'A {flavor} ice cream sundae with a cherry on top')

ice_cream('vanilla')
ice_cream()
```

### Keyword arguments

Functions can take arguments in a `key = value` syntax. This way the order of the arguments does not matter.

```python
def greeting(first_name, middle_name, last_name):
    print(f'Hi, {first_name} {middle_name} {last_name}')

greeting(last_name='Rahman', middle_name='', first_name='Ash')

```

# 3. Return

The **return** statement is used to return from a function i.e. break out of the function:

```python
def multiply(a, b):
    return
    print(a*b)

multiply(2, 3)
```

We can optionally return a value from the function as well:

```python
def multiply(a, b):
    return a*b

# returning the value doesn't print it to the console.
multiply(3, 3)

# you have to explicitly print the function call to see the returned value
print(multiply(3, 3) # 9

# 'returning' the value also allows us to save the value to a variable
six = multiply(2, 3)
print(six) # 6
```

### Print versus return

You might be wondering, why use **return** when we can just use **print**? They are fundamentally different in their applications:

1. **Return** - Saving it for later

```python
num = multiply(2, 3)
```

2. **Return** - Writing complex expressions

```python
num = multiply(multiply(2, 3), 4)
```

3. **Print** - Printing a value to the command line

```python
num = multiply(multiply(2, 3), 4)
print(num) # 24
```

# 4. Built-in functions

We have been using python's built-in functions so far in our lessons. Here's a few of them:

```python
# prints to console
print('This only shows up in console')

# returns python data type of argument
type('the type is a string')
type([])

# returns a float of integer or string argument
float(54)
float('34.4')

# returns an integer of a float or string argument
int(23.2)
int('34.4')

# returns a string of any data type
str(33.2)
str({})

# returns a range object based on an integer argument
range(100)
```

### `func()` versus `object.func()`

We have also written functions before that look different from the one's we've created this class.

```python
# returns a string uppercased
text = 'this is uppercased'
print(text.upper())
```

Functions that have a period preceding them are called **methods**. Functions like `.upper()` are only available to strings, so we call it a **string method**.

```python
# returns a list of methods available to strings
print(dir(text))
```

We will learn more about **methods** and how to create them in a future topic called Objected Oriented Programming.

## Extra: more python built-in functions:

We won't spend more time on these today, but here's a handy reference with more methods for lists in python. You can check out [the documentation](https://docs.python.org/3/tutorial/datastructures.html) for more info too!

# Overview of what we learned today

- How functions help us organize logic and not repeat ourselves
- How to create them and make them flexible with parameters
- How to invoke them in our python code and return new values
