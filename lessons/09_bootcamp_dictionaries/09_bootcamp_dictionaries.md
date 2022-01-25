# Bootcamp Class 9 - Dictionaries

<img src="https://lh3.googleusercontent.com/proxy/Mw1Z5gcj1XZrURnu4sMZrzDQJ6m1JEM3MgVu7opC_24OJ3SCKnY04aD4K-4AjQO0FBfKxWkNimg2RqA0PVHrIFPLwLo-cM56dskbbyew6-k" width="600">

# Before class

* Make sure you feel comfortable with both *logical operations* and *conditional statements* using **all 4 primitive data types**
* Make sure you feel comfortable working with [**list**](https://www.w3schools.com/python/python_lists.asp) objects in python

# Outline of class agenda

Today we'll learn about [**dictionaries**](https://www.python-course.eu/dictionaries.php) in python. This is a new data type! By the end of the lesson, you'll:

1. Feel comfortable using dictionaries in python to store multiple pieces of data (using any of the 4 primitive data types, and lists)
2. Know how to add, remove, and updating data in dictionaries
3. Understand the key differences between lists and dictionaries, especially in terms of:
    * Labels (lists do not have, dictionaries do)
    * Order (lists have, dictionaries do not)

# What is a dictionary?

We can think of **dictionary** in python through using the metaphor of a physical dictionary.
* In a physical dictionary, we look up a word, and then get information about that word (the definition, pronunciation, etc).
* A dictionary in python is very similar in that each part of the dictionary has a **key** (i.e. the word), and a corresponding **value** (i.e. the definition). All data in a dictionary is made up of these [**key-value pairs**](https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/#:~:text=Dictionary%20in%20Python%20is%20an,key%2Fvalue%20inside%20the%20dictionary.).
    * Another way of thinking about this is that every piece of data in a dictionary has a **label** (i.e. the key). This is unlike lists, where each element does not have a label
* Unlike lists, **dictionaries do not have order in python**
* We can also edit dictionaries to change what is in them (i.e. they are 'mutable')
* Just like with primitive data types in python, we can assign and update dictionaries using **variables**


# 1. Storing data in dictionaries

*Let's make a script your github repo at `jtc_class_code/class_scripts/bootcamp_scripts/dictionary_practice.py` for today*

### Dictionaries use curly braces `{}`

While lists use hard brackets, dictionaries use the curly braces `{}` to enclose all their data. In fact, a pair of curly braces with nothing inside does make an empty dictionary.

```python
blank_dict = {}
print(blank_dict)
print(type(blank_dict))
```

We can see that we now have a dictionary, with nothing in it:

```console
{}
<class 'dict'>
```

### Key-value pairs

All data in dictionaries are stored in key-value pairs. The key is usually a string, but the value can be almost anything. The syntax for this is always `key:value` where there is a colon between the key and value, then different key-value pairs are separated within the dictionary by commas. For example, here's one dictionary with one key-value pair:

```python
user_account = {'username':'pbloom'}
```
In this instance, the value was also a string. Here's an example now of a dictionary with 2 key-value pairs, where the second value is a float

```python
user_account = {'username':'pbloom', 'balance':270.26}
```

So, now there is a 'username' and a 'balance', which are represented by a string and a float, respectively. Also, while we can write the dictionary this way, it can also be handy to make a new line for each key-value pair. This is the convention, and is treated exactly the same by python.

```python
# this is equivalent to the previous code block
user_account = {'username':'pbloom',
                'balance':270.26}
```

This format is especially useful if we have a lot of key value pairs.

### Printing the contents of a dictionary

We can use `print()` on an entire dictionary to see what all the contents are!

```python
user_account = {'username':'pbloom',
                'balance':270.26}
print(user_account)
```

When we run this code, we get:
```console
{'username': 'pbloom', 'balance': 270.26}
```


### Retrieving data from a dictionary

If we want to pull out a specific value from the dictionary, we reference it by it's key. So, if I want to get just the `balance` variable from `user_account`, I can run:

```python
user_account = {'username':'pbloom',
                'balance':270.26}
my_money = user_account['balance']
print(my_money)
```

When we print `my_money`, we now just have the float **value**, that was paired with the key `balance` inside our `user_account` dictionary.

```console
270.26
```

Every time we want a **specific value** from a dictionary like this, we use this syntax -- the name of the dictionary, followed by hard brackets with the string name of the **key** (in quotes) inside.

As another example, if we wanted to get just the username, we could run:

```python
my_username = user_account['username']
```

Now, `my_username` is a *string* that is the **value** paired with the key `username` in the `user_account` dictionary.


### Dictionaries can store all sorts of data

So far we've seen strings and floats in a dictionary, but the *values* can be almost any kind of data. To demonstrate this, let's add some extra information to `user_account`.

```python
user_account = {'username':'pbloom',
                'balance':270.26,
                'deposits':[100.00, 21.34, 2.31, 8.06],
                'withdrawals':[-2.31, -21.43, -78.00],
                'email_notifications': True}
print(user_account)
```

So, now `user_account` has an item called `deposits` that is a list of floats representing deposits, and a similar list of withdrawals. There is also an item `email_notifications` that is a boolean variable. When we run this code, everything prints out, although it is a little harder to see clearly because there are so many items:

```console
{'username': 'pbloom', 'balance': 270.26, 'deposits': [100.0, 21.34, 2.31, 8.06], 'withdrawals': [-2.31, -21.43, -78.0], 'email_notifications': True}
```

Having a list inside a dictionary might seem confusing, but it can be really useful! We'll come back to this concept, called 'nesting', in later lessons and explore it more.

# 2. Adding / removing / updating data in dictionaries

### Adding items

To add a new item to a dictionary, we add a new key-value pair like so:

```python
user_account = {'username':'pbloom',
                'balance':270.26}

# add a new value of '9/15/2020' using the key 'last_transaction'
user_account['last_transaction_date'] = '9/15/2020'
```
So, this adds a new key-value pair with the key `last_transaction` and the value of `'9/15/2020'`. We **assign** the value to the new key as part of the dictionary. Now, if we print out `user_account`, we can see our addition has worked:

```console
{'username': 'pbloom', 'balance': 270.26, 'last_transaction_date': '9/15/2020'}
```

**We can add almost any data to a dictionary in this way**

For example, let's add an integer value to the dictionary:
```python
user_account['user_birth_year'] = 1993
```

Now, if we print out the dictionary again, we can see this integer `1993` has been added with the key `'user_birth_year'`

```console
{'username': 'pbloom', 'balance': 270.26, 'last_transaction_date': '9/15/2020', 'user_birth_year': 1993}
```

### Updating items

Updating items in a dictionary is almost exactly the same as adding new items, except that the **key** we reference is an *already existing key in the dictionary*. This is very similar to the way that updating a variable is like assigning a variable that already exists (re-assigning). We write over the old value and replace it with the new one.

So here, let's update the `balance`:

```python
user_account = {'username':'pbloom',
                'balance':270.26}

# update the balance
user_account['balance'] = -500.00

print(user_account)
```

So, we've updated our balance to `-500.00` by assigning this value to the existing key `'balance'` in `user_account`. When we print out `user_account`, we see our new balance:

```console
{'username': 'pbloom', 'balance': -500.0}
```

Note: when updating a variable in a dictionary, we don't have to replace it with something of the same type. We *could* have changed the balance to a string or a list, or another data type here if we wanted

### Removing items

When removing data from a dictionary, we remove an entire key value pair, since the value can't exist in the dictionary without the key. To do this, we use the `pop()` function with the name of the **key** to remove the whole pair. For example

```python
user_account = {'username':'pbloom',
                'balance':270.26}

# we remove 'balance'
user_account.pop('balance')

print(user_account)
```

Since we remove `'balance'`, we just have left:
```console
{'username': 'pbloom'}
```

# 3. Key differences between lists and dictionaries

Lists and dictionaries are both foundational data types in python, and you'll most likely be using these a lot in the future. So, it's important to think about the differences between these two data types, and why you might use one over the other.

## Lists have order, dictionaries do not
* Because lists have numeric indices, they are ordered
* Dictionaries, because they are organized by string labels, don't have a specific order
* If our data has an **order** that is important, we probably want to use a list, and not a dictionary
* Order allows us to do [numeric indexing](https://towardsdatascience.com/the-basics-of-indexing-and-slicing-python-lists-2d12c90a94cf) to get items by their position. We can only do this with lists
* We haven't gotten there yet, but **loops** only really work with ordered data. So, we can use loops with lists but can't use them with dictionaries in the same way

## Dictionaries have labels, lists do not
* Dictionaries are **labeled** in the form of their **keys** -- so every piece of data inside (the values) has a corresponding label
* So, dictionaries are really useful when we want to retrieve items by 'name', rather than an order
* Lists do not have such labels

<img src="https://www.i2tutorials.com/wp-content/media/2020/05/Append-a-Dictionary-to-a-list-in-Python-5-i2tutorials.jpg" width="800">




# Overview of what we learned today

* How to use a dictionary to store several types of data
* How key-value pairs work in a dictionary
* How to add, update, and remove, items in a dictionary
* Some key differences between lists and dictionaries

### Next up: loops!

We've hinted at this a few times, but we will soon be getting to loops! This is a powerful way to apply operations to many pieces of data in sequence. If you can't wait to give this a try, you can check out [this page](https://www.w3schools.com/python/python_for_loops.asp) for a quick intro.
