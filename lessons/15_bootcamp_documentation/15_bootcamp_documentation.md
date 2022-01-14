# NumPy -- Working with documentation

# Outline of class agenda

Todays class is focused on learning how to work with *documentation* to implement code solutions, with a special focus on the NumPy library

During this class you'll:

1. Practice working with NumPy more
2. Get comfortable working with the NumPy documentation
3. Learn about working with documentation more generally


### What is documentation? 
* Libraries are essentially sets of functions and classes that share a purpose (e.g. machine learning libraries). They can be imported to eliminate the need to write certain code from scratch.

### What is documentation? 

* Documentation is basically a formal way for a python library to provide a 'users guide'
* Documentation usually shows how code works, especially
    * Available functions, their arguments, and what they return
    * Available classes and their attributes
    * Example use cases of functions/classes
* Almost every python library has documentation of some form on the web, including [base python itself](https://docs.python.org/3/)
* Documentation for some libraries is much better than others 
    * Some examples of well documented python libraries are:
        * [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) 
        * [NumPy](https://numpy.org/doc/stable/contents.html) 
        * [Requests](https://requests.readthedocs.io/en/master/) 
    
    
### Why use documentation?

Often, if a library has good documentation, the documentation is the first place to go if:
* You're stuck trying to get a function to work
* You want to be able to do a certain thing and you think the library might have a function that can do it

### Alternative Forms of Documentation

When libraries have bad or incomplete documentation, information on how to use those libraries can be found elsewhere online. Some examples of websites that are incredibly useful for figuring how to use certain libraries are:
* [W3 Schools](https://www.w3schools.com/python/)
* [Geeks for Geeks](https://www.geeksforgeeks.org/python-programming-language/)
* And, as always, [Stack Overflow](https://stackoverflow.com/questions/tagged/python)


# Class


### Setup

To get started, we'll be working with NumPy arrays. Remember, in python, lists are the name for the data structure called arrays in most other programming languages (essentially, an ordered, indexed set of data). NumPy arrays differ from python lists in a few ways:
* NumPy arrays can only store 1 data type; python lists can store many
* NumPy arrays have a lot of associated methods that help with computations, unlike lists
* it is possible to perform many operations on the elements of a NumPy array without a for/while loop; this isn't possible with lists


```python
# don't forget to import! 
import numpy as np
```

# Demos on working with the [NumPy documentation](https://numpy.org/doc/stable/contents.html)

We'll browse the NumPy documentation first, then show a few examples of searching for things using it

# Example 1: Using NumPy docs to figure out how to create an array

In this example we want to make a new array with the integers 1, 2, and 3 (similar to the python list `[1, 2, 3]`).

#### Step 1 -- go to NumPy docs

It is at https://numpy.org/doc/stable/contents.html

#### Step 2 --- go to the user guide

One of the most helpful parts of the NumPy documentation (though not the only part) is the [user guide section](https://numpy.org/doc/stable/user/index.html)


This can seem a little intimidating at first because there is a LOT on here -- take a minute to click around and explore a few pages.

#### Step 3 -- go to the ['NumPy: the absolute basics for beginners'](https://numpy.org/doc/stable/user/absolute_beginners.html) section

Still a LOT of info on this page, but we are getting close to the right information! 
* We can see more links on the right hand side telling us what types of information we might find on this page.

If we look at the middle of that right column, we can see the spot in the docs that really seems to answer our question. Click on the link that says [How to create a basic array](https://numpy.org/doc/stable/user/absolute_beginners.html#how-to-create-a-basic-array).

This seems to be telling us that the way to create an array is:
```
a = np.array([1, 2, 3])
```

Perfect! This is exactly what we were looking for.

# Example 2: using NumPy docs to create an array of zeroes

Let's say we know we need an array of length 10 but we don't know what we're going to put in it yet. NumPy has the really useful functionality of allowing us to create an array of 0s. 

Since we're still in the area of the docs dedicated to the creation of arrays, let's scroll down a little to see if we can find what we're looking for. 

Looks like the code to create an array of 0s is:
```
zs = np.zeros(10)
```

# Example 3: using NumPy docs to find shape of array

NumPy arrays can have more than 1 dimension. For example, a 1-d array looks like:
```
[1, 2, 3]
```
A 2-d array looks like:
```
[ 
    [1, 2, 3],
    [4, 5, 6]
]
```

The shape of a NumPy array tells us how many dimensions there are and how many elements in each dimension. 


#### Step 1: google for the right place in the docs?
This might be a good place to mention that **GOOGLING** is often one of the best ways to find the right part of the docs. For example, if we google 'numpy documentation shape of array', the first hit brings us to [a very relevant page in the docs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html). 

Now, this page is in the ['API reference'](https://numpy.org/doc/stable/reference/index.html) section of the NumPy documentation, which is essentially a guide to each function/method available (with examples).


#### Step 2 - investigate the documentation

On this page, we can see that it's talking about something called `numpy.ndarray.shape`. We know what numpy is, so ndarray.shape must belong to numpy. Since we're not sure what an ndarray is yet, let's scroll down the page a bit to look at the example. 

#### Step 3 - check out the examples 

Here we see the ndarray:
```
x = np.array([1, 2, 3, 4])
```
This is created the same way as our array of 0s, so this is what we're looking for! Now we see the command:
```
x.shape
```
There are no parentheses, so this is an *attribute* not a *method* of the array. Let's try this with our array of 0s:
```
print(zs.shape)
>>> (10,)
```
We can see here that we have one dimension with 10 elements in it!


# Overview

Nice work! Today we learned:
* What documentation is and why it might be helpful
* How to get started with the [NumPy documentation](https://numpy.org/doc/stable/contents.html)
* How to create a NumPy array
* How to look through the NumPy documentation to uncover further functionality for NumPy arrays

This has been a very brief overview of a few ways of using the NumPy documentation. Most python libraries have their own documentation, so they key to getting used to working with documentation is practice. That's exactly what we'll do in the challenge -- you'll have to figure out a few things using the documentation.