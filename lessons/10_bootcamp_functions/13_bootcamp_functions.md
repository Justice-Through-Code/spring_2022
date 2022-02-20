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

Let's create a new file in our class code folder called `functions_practice.py` for tonight's content.

Think back to when you learned about variables. When we create a variable, say

```python
days_per_week = 7
```

we're telling python 'hey, there's a new keyword you need to know-- `days_per_week` is the name of a box I just made, with the integer `7` inside of it. When I type `days_per_week` in my code, I want you to go get that box, and use whatever's inside of it, which in this case is 7.'

Throughout the course, we've been using variables to hold a bunch of different data, and different data types. We've made variables of floats, integers, strings, booleans, lists, and dictionaries. All of the different data types we've encountered can be saved in variables. But sometimes, we don't want to save a piece of data to use later, we want to save a piece of _code_ to use later. This is where **functions** come in.

# What is a function?

A **function** is a chunk of code that's been given a name (like a variable), so that we can use it as many times as we want without having to write those lines of code over and over again. We can put any line/s of code that we want into a function--

```python
def say_hello():
    print('Hello!')
    print('My name is Lillie.')
    print("It's nice to meet you!")
```

What's happening here? A few things! `def` is a keyword in Python (short for 'define', to 'define' a function) that tells the computer that we're about to create a function. Then, just like we name our variables, we name our function-- the name of this function is `say_hello`. Functions in python need parentheses at the end, we'll get into why in a little bit. Then, just like conditionals and loops that we've seen before, when we need to tell Python 'hey, all the code that's indented here happens inside of the if statement or inside of the loop', we use a colon at the end of the line, and then indentation to tell Python that everything indented after the colon is part of this chunk of code.

If we run our code right now, what do we think will happen? We have print statements, will they run?

Nope! Much like when we define a variable, when we define a function, it doesn't automatically do anything. We _create_ the variable, and then afterwards, we use it. Same here. We've created our function, but how do we make it run? We may already know the answer--

You might recall, we've actually been using functions throughout this course without talking about what they _are_. What are some examples of functions that we've used so far?

```python
print()

int()
float()
str()

type()

len()
```

So we know that to _use_ a function in Python, we type the name of the function plus open and close parentheses after. (We've also seen a type of function called a method (string methods, list methods, etc), but we'll get into that specialized type of function next week.)

Knowing that, how can we _run_ our `say_hello` function?

```python
def say_hello():
    print('Hello!')
    print('My name is Lillie.')
    print("It's nice to meet you!")

say_hello()
```

and we get

```console
Hello!
My name is Lillie.
It's nice to meet you!
```

We just used our own function! We can use it just like we've been using other functions this whole time--

```python
def say_hello():
    print('Hello!')
    print('My name is Lillie.')
    print("It's nice to meet you!")


is_friendly = input('Would you like to say hello? (yes/no) ')

if is_friendly == 'yes':
    say_hello()
```

etc etc etc.

But this feels a little brittle. I don't want my function to _always_ say my own name, I want it to be able to use any name. This is where the parentheses come in!!

## Parameters

When we use a function like `len`, we don't just say `print(len())`. `len` of what?? We send the `len` function a string or a list or another type of data, and it tells us how long the item is. We send data to the `len` function, inside of its parentheses, and then the function uses that data. We can rewrite our function to take in a piece of data as well, in this case, a _name_ to print out.

```python
def say_hello(name):
    print('Hello!')
    print(f'My name is {name}.')
    print("It's nice to meet you!")
```

This is called a **parameter**. Much like creating a variable when you write a for loop (`for garment in laundry_basket`), parameters are variables we create when we write a function. But in this case, the variable _only exists inside of your function._

You can write functions to take in any number of parameters (try to keep it to 5 at most). But now that our function expects a parameter, we need to _send_ the function a name to use when we run it!

```python
say_hello('Yusuf')
```

```console
Hello!
My name is Yusuf.
It's nice to meet you!
```

A parameter can reference any data type we have learned so far. Let's make a new function--

```python
def times_two(num):
    # parameter num is an int or a float
    print(num * 2)

times_two(4) # 8
times_two(4.0) # 8.0
```

### Multiple parameters

Parameters are powerful! We can have more than one.

```python
def multiply(a, b):
    print(a * b)

multiply(2, 3) # 6
```

Just like when we have a `list` of items, when we have a bunch of parameters, we can separate them with commas.

### Arguments

Another word you'll probably hear a lot with parameters is **arguments**. This isn't important to remember right now, but is useful when you're talking about code-- the _value_ that is passed to a function is called an **argument**. The _parameter_ is name of the variable inside the function itself:

```python
# `num` is a parameter
def times_two(num):
    print(num * 2)

# `2` is an argument
times_two(2)
```

You can start to see how powerful this can be when you think about challenges you've done so far-- if we wrote a `convert_to_celsius` function for the temperature challenge, we'd only have to write the formula once no matter how many temperatures we want to calculate:

```python
def convert_to_celsius(degrees):
    print((degrees - 32) * 5 / 9)

convert_to_celsius(100)
convert_to_celsius(0)
convert_to_celsius(34.2)
```

```console
37.77777777777778
-17.77777777777778
1.2222222222222239
```

Functions also have the added benefit of making our code much cleaner to read and less prone to human error. I can easily understand what `convert_to_celsius` is doing, rather than seeing a bunch of math that I might have written right in one place and wrong in another.

## BREAK

### Return

We've seen how to make functions powerful by giving them _inputs_ (parameters/arguments). But we can also make them more powerful by making them _output_ something to.

So far our functions have printed stuff out, but if we think about all the built in Python functions we've used so far, they haven't actually done that. Think about a function like `len()`. If we just do

```python
len('this is a string')
```

nothing will happen, right? This tells us that the `len` function doesn't print anything out. Which is a good thing-- in a situation like this:

```python
word = 'functional'

for i in range(len(word)):
    print(f'{i}: {word[i]}')
```

we wouldn't want `len()` to print something out when we're using it this way. So what does it do instead? It **return**s the answer.

Let's refactor our function that multiplies a number by 2 to return the answer instead of printing it out:

```python
def times_two(num):
    return num * 2
```

Now, we can use it the same way we use built in python functions--

```python
def times_two(num):
    return num * 2

small_num = times_two(3)  # 6
big_num = times_two(750)  # 1500

print(small_num < big_num)
```

We can _catch_ the output of the function in a variable and then use it later.

```console
True
```

Just like with parameters, we can return any type of data type we want, and as many items as we want (separated by commas). But it's important to keep in mind-- when a function returns something, that's the end of the function! The code does not go back into the function and keep going after it returns something, a `return` statement ends a function. So

```python
def times_two(num):
    return num * 2
    print('Hello!')

small_num = times_two(3)  # 6
big_num = times_two(750)  # 1500

print(small_num < big_num)
```
Still only prints out `True`. The print statement in our function might as well not exist, because we've told Python to exit the function already.

And those are the building blocks of functions!

# Overview of what we learned today

- How functions help us organize logic and not repeat ourselves
- How to create them and make them flexible with parameters
- How to run them in our python code and return new values


## Extra: more python built-in functions:

We won't spend more time on these today, but here's a handy reference with more methods for lists in python. You can check out [the documentation](https://docs.python.org/3/tutorial/datastructures.html) for more info too!
