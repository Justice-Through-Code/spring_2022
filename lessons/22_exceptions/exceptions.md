# Class 22 - Errors and Exceptions

# Before class

- Familiarity with Python data types, logical statements, loops and functions
- Experience googling for potential solutions to a problem

# Outline of class agenda

1. Understanding Traceback
2. Common error types
3. Handling exceptions in buggy code

# Running into Errors and Exceptions

Whether you're a beginner or an exprienced programmer, you will run into errors with your code. Seeing the error output can seem overwhelming, but once you learn how to read these outputs, it gets easier to fix issues with your code.

## Traceback


```python
# This code has an intentional error. You can type it directly or
# use it for reference to understand the error message below.
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[3])

favorite_ice_cream()
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-1-e5b074b4d20d> in <module>
          9     print(ice_creams[3])
         10 
    ---> 11 favorite_ice_cream()
    

    <ipython-input-1-e5b074b4d20d> in favorite_ice_cream()
          7         'strawberry'
          8     ]
    ----> 9     print(ice_creams[3])
         10 
         11 favorite_ice_cream()


    IndexError: list index out of range


The traceback is the official name of the output we see in the command line. It contains a wealth of information to diagnose the issue. Some of the key components of a traceback output are:
- Lines of code or function calls that led to the error (indicated with an arrow). The most recent function call starts at the bottom. You should start at the bottom, if you see a long traceback output. 
- An error type is indicated at the top and at the bottom. The bottom indication also has a description detailing the specifics of why this error type was raised. There are lots of error types, we will look at some common ones.

# Common Error Types

There's a more exhaustive list in the official Python documentation [here](https://docs.python.org/3/library/exceptions.html). Below are some common error types we will look at today.

## SyntaxError


```python
print('hello world'
```


      File "<ipython-input-36-7b9f7a40f599>", line 1
        print('hello world'
                           ^
    SyntaxError: unexpected EOF while parsing



## IndentationError


```python
def multiply(a, b):
return a * b
```


      File "<ipython-input-32-f9ff7cac4506>", line 2
        return a * b
             ^
    IndentationError: expected an indented block



## TabError


```python
def some_function():
	msg = 'hello, world!'
	print(msg)
        return msg
```


      File "<ipython-input-61-6aedb297b13f>", line 4
        return msg
                  ^
    TabError: inconsistent use of tabs and spaces in indentation



## NameError


```python
a = b + 2
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-9a8484cfca97> in <module>
    ----> 1 a = b + 2
    

    NameError: name 'b' is not defined


## IndexError


```python
groceries = ['apples', 'oranges', 'bananas']
print(groceries[2])
print(groceries[3])
```

    bananas



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-30-ebedfc14855b> in <module>
          1 groceries = ['apples', 'oranges', 'bananas']
          2 print(groceries[2])
    ----> 3 print(groceries[3])
    

    IndexError: list index out of range


## TypeError


```python
def square(num):
    return num * num

square('abc')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-1-d5abdb400d73> in <module>
          2     return num * num
          3 
    ----> 4 square('abc')
    

    <ipython-input-1-d5abdb400d73> in square(num)
          1 def square(num):
    ----> 2     return num * num
          3 
          4 square('abc')


    TypeError: can't multiply sequence by non-int of type 'str'


# Handling Exceptions

Sometimes it's difficult to account for all the potential errors that may arise in your code. This is fairly common when there are parts of your code relying on dynamic data, for e.g. A user providing incorrect user id or password during login. When our code is met with data it is not expecting leading to exceptions, we don't necessarily want our code to stop working, but rather handle it gracefully and proceeding. 

## Try/except


```python
try:
  # try to run this block
  print(x)
except:
  # if an exception exists, run this block
  print("Something went wrong!")
```

    Something went wrong!


## Multiple exceptions


```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```

    Variable x is not defined


## Else


```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  # Runs if an exception does not exist
  print("Nothing went wrong")
```

    Hello
    Nothing went wrong


## Finally


```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  # Always runs, whether there's an exception or not
  print("We made it to the end!")
```

    Something went wrong
    We made it to the end!


# Final Thoughts

Daunting as it may seem first, reading tracebacks gets easier. It may be discouraging to see an error in your command line but it gives us control over being able to address an issue. Programming would be so much more difficult if there were no error outputs! 
