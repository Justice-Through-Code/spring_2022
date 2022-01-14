# Bootcamp class 7 - Lists

<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

* Make sure you feel comfortable with all 4 primitive data types (integers, strings, floats, and booleans)
* Make sure you feel comfortable with both *logical operations* and *conditional statements*
* Make sure you can capture user input with the `input()` function

# Outline of class agenda

Today we'll learn about **lists** in python. This is a new data type! By the end of the lesson, you'll:

1. Feel comfortable using lists in python to store multiple pieces of data (using any of the 4 primitive data types)
2. Know how to add / remove items from lists using `append()` and `remove()`
3. Know how to find out how long a list is with `len()`
4. Feel confident with **list indexing** in python
    * Know the difference between a list *index* and the list *element* at that index
5. Be able to split strings up into lists, and also join lists to form strings

# What is a list?

A **list** in python is not so different from the everyday definition of a list, such as a grocery list or a to-do list. 
* In python, a list is a data type used to store multiple items (pieces of data) in a certain order (i.e. 'ordered'). 
* We can also edit lists to change what is in them (i.e. they are 'mutable')
* Just like with primitive data types in python, we can assign and update lists using **variables**


# 1. Storing data in lists

*Let's make a script `list_practice.py` to practice working with lists.*


Every list has a certain syntax:
* all the information is surrounded with hard brackets `[]`
* each piece of data, or **element**, is separated from the next with a comma
* lists can contain elements of almost any data type! today we'll focus on the 4 primitive data types though

So, let's make our first list!

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)
```

In this case, we've made a list with 4 elements in it, and each element is a string (that's why each has quotes around it). We separate each element with a comma. Now when we run the script, the `print()` function allows us to see our list:

```console
$ python list_practice.py 
['apples', 'eggs', 'pasta', 'carrots']
```

Lists can have other data types in them too:

```python
int_list = [1,-4,7]
float_list = [12.4,-199.22, 4.0, 84.3]
boolean_list = [True, False, False, True, True, True, False]
print(int_list)
print(float_list)
print(boolean_list)
```

We can print these out to see that lists work the same way for all these different data types:

```console
$ python list_practice.py 
[1, -4, 7]
[12.4, -199.22, 4.0, 84.3]
[True, False, False, True, True, True, False]
```

### One list can store multiple data types

One thing to know is that the same list can have multiple data types in it! For example:

```python
mixed_list = [2, 'apples', -13.8, True]
print(mixed_list)
```

This is perfectly acceptable to python, and it will accept and print out a list of varying datatypes:

```console
[2, 'apples', -13.8, True]
```

Generally, it's good to be careful about mixing data types like this in one list though -- it can sometimes lead us to confusion!

### Checking the data type of a list

You might recall from earlier that we can check what data type a variable is with `type()`. This is true with lists too:

```python
# make an integer and check the type
var1 = 2
print(type(var1))

# make a list of integers and check the type
var2 = [2,2,3]
print(type(var2))
```

This returns:

```console
<class 'int'>
<class 'list'>
```

So, type will tell us that a list is a list, but it won't tell us what kind of data is stored *inside* the list. We'll get to this later!

### Lists with variables inside them

If we have existing variables, we can put them inside lists! If we think about this with the box metaphor, this is like numbering a bunch of your boxes, and lining them up in numerical order. When you refer to the box, the contents are still the same!

```python
var_a = 'apple'
var_b = 'pear'
var_c = 'milk'
groceries = [var_a, var_b, var_c]
print(groceries)
```

So when we print out this list made of already assigned string variables, we get:

```console
['apple', 'pear', 'milk']
```

We still get the contents of each string variable, even though here we've made a list of all of them!


### Making a blank list

Sometimes, it can be really useful to assign an empty list (a list with 0 elements), then add data to it later. We can do this in python with the following syntax:

```python
my_list = []
print(my_list)
print(type(my_list))
```

So, we assign a blank list, then print it out, then check the variable type:

```console
$ python list_practice.py 
[]
<class 'list'>
```

So, we can see that printing out an empty list just gives us `[]`. But, an empty list is still a list!

# 2. Adding / removing items from lists

Once we have an existing list, we'll often want to add or remove elements! 
* We can add items to the end of the list with the `append()` function
* We can remove specific items with the `remove()` function

### Adding items

Let's say we have an existing grocery list but we want to add more:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)

# add another item
groceries.append('peanut butter')
print(groceries)
```

Now, when we run this, we can see that we've added 'peanut butter' to the end of the list

```console
$ python list_practice.py 
['apples', 'eggs', 'pasta', 'carrots']
['apples', 'eggs', 'pasta', 'carrots', 'peanut butter']
```

Great! Now we can add items at the end of the list. We won't go over it today, but there is also an [insert function](https://www.programiz.com/python-programming/methods/list/insert) for adding an item at whatever place in the list you want, feel free to check out the [documentation](https://docs.python.org/3/tutorial/datastructures.html)!

### Removing items

Now, maybe we realized we actually have enough eggs and we want to take that off the list. We can do that via

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)

# remove the eggs
groceries.remove('eggs')
print(groceries)
```

Now, we can see that this is gone from our list:

```console
['apples', 'eggs', 'pasta', 'carrots']
['apples', 'pasta', 'carrots']
```

**We can't remove an item that doesn't exist though:**

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# remove candy
groceries.remove('candy')
print(groceries)
```

So, here we're trying to remove 'candy' from the list, even though it isn't in the list.

```console
Traceback (most recent call last):
  File "list_practice.py", line 4, in <module>
    groceries.remove('candy')
ValueError: list.remove(x): x not in list
```

We get this error that 'x not in list' to tell us that we tried to remove something that wasn't there in the first place. 

# 3. Using `len()` to get the list length

The length of a list indicates how many items are stored inside. It can be really helpful to know exactly how many items are in a list, and for this, we can use the function `len()`.

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# print out the list length
print(len(groceries))
```

When we run this code, we print out the length of our grocery list:

```console
4
```

What happens if we try this with a blank list?
```python
empty_list = []
print(len(empty_list))
```

We get:
```console
0
```



# 4. List indexing in python

`append()` and `remove()` are really useful ways of getting data into and out of lists, but the fact that lists have **order** makes them extra useful. Because lists are in order, each item in the list also has what is called an **index**, which is a number to mark it's position. Something that is a bit strange but **really** important in python is that **the first index is always index 0**. We can see this in this graphic depiction of a list:

<img src="https://railsware.com/blog/wp-content/uploads/2018/10/positive-indexes.png" width="800">

* So, 'red' is the *first* item, and the corresponding index is 0
* 'green' is the *second* item, and the corresponding index is 1
* And so on...until
* 'black' is the *last* item, and the corresponding index is 5

### How to index a list in python

Numeric list indexing in python is done with hard brackets **after** the list variable. Inside the hard brackets, we can put a number for the index of the item we want. For example, if we want to get the first item in our grocery list:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[0])
```

This gives us:
```console
apples
```

Great! We can do that with the other indices too. For example, if we want 'pasta', the 3rd element in the list:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[2])
```

We get:

```console
pasta
```

### Out of range errors

Let's say I wanted to select out only 'carrots', the last item in the list. There are 4, items, so I start off by trying to `groceries[4]` to index just this item:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[4])
```

But, when we run this code, we get:
```console
$ python list_practice.py 
Traceback (most recent call last):
  File "list_practice.py", line 2, in <module>
    print(groceries[4])
IndexError: list index out of range
```

This 'list index out of range' error is an error you will probably see a LOT, because it is really easy to make this kind of mistake! `groceries[4]` would really refer to the 5th item in the list, and there are only 4 items, so python is telling us we're 'off the end' of the list, or 'out of range'. 


### Indexing from the end

It can be helpful to try to take the last item in a list though, or to always get an item that is second to last. So, we can index a list in reference to the end by putting a minus sign in front of the index. For example, the index of `-1` is always the last item in the list, `-2` is the second last, etc.

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[-1])
print(groceries[-2])
print(groceries[-3])
```

We get:

```console
carrots
pasta
eggs
```

### Slicing to get multiple items

So far, we've used the list indices to get just 1 element back, but we can specify a range of indices with `:` to get multiple items. This is called **slicing**, and returns a list back, rather than just individual elements. 

The syntax of slicing follows `[position1:position2]` to get the items starting at index `position1` up to but **not** including index `position2`. This can be confusing! This visual may help:

<img src="https://railsware.com/blog/wp-content/uploads/2018/10/first-slice.png" width="800">

So, we can see that `nums[2:7]` here gives us the items in indices 2-6, but does NOT include 7. 

Let's try this with our grocery list.

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# slice to get items 1-2 but NOT 3
my_items = groceries[1:3]
print(my_items)
```

So, this gives us back:
```console
['eggs', 'pasta']
```

But, we don't include 'carrots' here, because that was in index 3.

A few other things to remember about slicing are that:
* Indexing is *reset* if we assign the sliced list to a new variable
* Slicing where we use consecutive numbers (i.e. `[1:2]` or `[15:16]`) will give us back a list with only 1 item

So, going from the last example:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# slice to get items 1-2
my_items = groceries[1:3]

# print index 0 of the resulting list
print(my_items[0])
```
This returns:
```console
eggs
```

So, even though 'eggs' was the second item, or index 1, in `groceries`, when we slice this list to make `my_items`, eggs is the first item, so it now occupies index 0 in `my_items`.

### What type of data do we get from indexing?

If we index a single element of a list, we get whatever type of data that list element is. For example, if we have a list full of strings like `groceries`, if we pull out one index, that item is a string:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
my_item = groceries[2]
print(my_item)
print(type(my_item))
```

We get:

```console
pasta
<class 'str'>
```

However, if we are **slicing** the list, this returns a list back to us **even if the slice only has 1 item**:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
my_items = groceries[1:2]
print(my_items)
print(type(my_items))
```

This returns: 

```console
['eggs']
<class 'list'>
```

So, even though we only have 'eggs', the fact that we are *slicing* here, rather than just taking 1 index, means we get a list back with a single item in it. 

# 5. Splitting strings into lists, and vice versa


### Splitting
There is a really useful function to split a string variable up into a list, called `split()`. Basically, we give python a string pattern to split your string by. For example if we split by `,`, python will split the string up by where the commas are, and put each piece as a separate item in the list. Let's try it!

```python
my_string = 'row, row, row, your boat, gently down the stream'
# split the string by commas
my_list = my_string.split(',')
print(my_list)
```

So, when we split up the string, we get this:
```console
['row', ' row', ' row', ' your boat', ' gently down the stream']
```

Technically, we can actually split by whatever we want! Let's try splitting by 'ow':

```python
my_string = 'row, row, row, your boat, gently down the stream'
# split the string by 'ow'
my_list = my_string.split('ow')
print(my_list)
```
This gives us:
```console
['r', ', r', ', r', ', your boat, gently d', 'n the stream']
```

Why does this look so strange? Well, when we split by 'ow', all the 'ow's get removed from the list elements (in the previous example, all the commas were removed too)

### Joining

We can also do the opposite, and merge list items into a single string with `.join()`. In this case, we put the name of the list we want to merge inside the `.join()` call, and right before it goes a string that will go between every element of the list in the output string:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# join the list with no space in between
my_string1 = ''.join(groceries)
print(my_string1)

# join the list with 1 space in between
my_string2 = ' '.join(groceries)
print(my_string2)

# join the list with 1 comma in between
my_string3 = ','.join(groceries)
print(my_string3)

# join the list with the word FOOD in all caps in between
my_string4 = 'FOOD'.join(groceries)
print(my_string4)
```

So, we can see the results of all these joins

```console
appleseggspastacarrots
apples eggs pasta carrots
apples,eggs,pasta,carrots
applesFOODeggsFOODpastaFOODcarrots
```

## Extra: more python list methods:

We won't spend more time on these today, but here's a handy reference with more methods for lists in python. You can check out [the documentation](https://docs.python.org/3/tutorial/datastructures.html) for more info too!

<img src="https://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1592084676/list3_ldpeim.png" width="600">




# Overview of what we learned today

* **Lists!** A new more complex data type that can store multiple pieces of data in an ordered and editable way. Pretty cool!
* How to create, add, and remove list items
* How to get the length of a list with `len()`
* How to **index** and **slice** lists
* How to split strings into lists, and join lists to strings

We haven't gotten there yet today, but there is one major thing about lists that is extra useful and related to the fact that they are being ordered. Because they are ordered, we can use **loops** to iterate through them and apply operations to each element. This is coming up in a few classes!
