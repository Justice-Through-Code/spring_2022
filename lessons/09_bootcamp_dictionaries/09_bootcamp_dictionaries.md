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
    * Labels (dictionaries have them instead of indexes, lists have indexes)
    * Order (lists have, dictionaries do not)

# What is a dictionary?

We can think of **dictionary** in python through using the metaphor of a physical dictionary.
* In a physical dictionary, we look up a word, and then get information about that word (the definition, pronunciation, etc).
* A dictionary in python is very similar in that each part of the dictionary has a **key** (i.e. the word), and a corresponding **value** (i.e. the definition). All data in a dictionary is made up of these [**key-value pairs**](https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/#:~:text=Dictionary%20in%20Python%20is%20an,key%2Fvalue%20inside%20the%20dictionary.).
    * Another way of thinking about this is that every piece of data in a dictionary has a **label** (i.e. the key). This is unlike lists, where each element has an _index_ instead.
* Unlike lists, **dictionaries do not have order in python**
* We can also edit dictionaries to change what is in them (i.e. they are 'mutable')
* Just like with primitive data types in python, we can assign and update dictionaries using **variables**


# 1. Storing data in dictionaries

*Let's make a script your github repo at `jtc_class_code/dictionary_practice.py` for today*

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

Let's think again about how a real life dictionary works. Every word in the dictionary has a definition.

programmer: a person who writes computer programs

For every word, there is one (or more) definition. We can think of this as a 'key-value' pair. All that means is that
for each key (word) in the dictionary, there is a value (definition) for it.

All data in dictionaries are stored in key-value pairs. The key is often a string, but the value can be almost anything. The syntax for this is always `key: value` where there is a colon between the key and value, then different key-value pairs are separated within the dictionary by commas. So the example above would become

```python
word_dictionary = {'programmer': 'a person who writes computer programs'}
```

Our dictionary values can be anything. For instance, say we wanted to add a word with multiple meanings to our dictionary. What's a data type we know that can hold more than one thing in it?

We can have a list of defitions for one word:

```python
# We can put each key-value pair on its own line to see our dictionary contents more clearly
word_dictionary = {
    'programmer': 'a person who writes computer programs',
    'bow': ['a knot tied with two loops and two loose ends', 'a weapon for shooting arrows']
}
```


### Printing the contents of a dictionary

We can use `print()` on an entire dictionary to see what all the contents are!

```python
word_dictionary = {
    'programmer': 'a person who writes computer programs',
    'bow': ['a knot tied with two loops and two loose ends', 'a weapon for shooting arrows']
}
print(word_dictionary)
```

When we run this code, we get:
```console
{'programmer': 'a person who writes computer programs', 'bow': ['a knot tied with two loops and two loose ends', 'a weapon for shooting arrows']}
```


### Retrieving data from a dictionary

If we want to pull out a specific value from the dictionary, we reference it by it's key. So, if I want to get just the value of `programmer` from `word_dictionary`, I can run:

```python
word_dictionary = {
    'programmer': 'a person who writes computer programs',
    'bow': ['a knot tied with two loops and two loose ends', 'a weapon for shooting arrows']
}
my_job = word_dictionary['programmer']
print(my_job)
```

When we print `my_job`, we now just have the definition that was paired with the key `programmer` inside our `word_dictionary` dictionary.

```console
a person who writes computer programs
```

It's similar to indexing into a list-- if you print something like `my_list[0]`, the index number (0) doesn't print out. Similarly here, when we key into our dictionary at a specific key (`word_dictionary['programmer']`), the key doesn't print out either.

Every time we want a **specific value** from a dictionary like this, we use this syntax -- the name of the dictionary, followed by hard brackets with the string name of the **key** (in quotes) inside.

As another example, if we wanted to get just the 'bow' definition, we could run:

```python
bow_definitions = word_dictionary['bow']
```

Now, `bow_definitions` is the *list* we wrote of bow definitions tied to the 'bow' key in our `word_dictionary`.


### Dictionaries can store all sorts of data

So far we've seen strings and list in a dictionary, but the *values* can be almost any kind of data. To demonstrate this, let's create a new dictionary called `user_account`.

```python
user_account = {
    'username': 'pbloom',
    'balance': 270.26,
    'deposits': [100.00, 21.34, 2.31, 8.06],
    'withdrawals': [-2.31, -21.43, -78.00],
    'email_notifications': True
}
print(user_account)
```

So, now `user_account` has an item called `deposits` that is a list of floats representing deposits, and a similar list of withdrawals. There is also an item `email_notifications` that is a boolean variable. When we run this code, everything prints out, although it is a little harder to see clearly because there are so many items:

```console
{'username': 'pbloom', 'balance': 270.26, 'deposits': [100.0, 21.34, 2.31, 8.06], 'withdrawals': [-2.31, -21.43, -78.0], 'email_notifications': True}
```

# 2. Adding / removing / updating data in dictionaries

### Adding items

To add a new item to a dictionary, we add a new key-value pair like so:

```python
user_account = {
    'username':'pbloom',
    'balance':270.26
}

# add a new value of '9/15/2020' using the key 'last_transaction'
user_account['last_transaction_date'] = '9/15/2020'

print(user_account)
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
user_account = {
    'username':'pbloom',
    'balance':270.26
}

# update the balance
user_account['balance'] = -500.00

print(user_account)
```

We've updated our balance to `-500.00` by assigning this value to the existing key `'balance'` in `user_account`. When we print out `user_account`, we see our new balance:

```console
{'username': 'pbloom', 'balance': -500.0}
```

Note: when updating a variable in a dictionary, we don't have to replace it with something of the same type. We *could* have changed the balance to a string or a list, or another data type here if we wanted

### Removing items

When removing data from a dictionary, we remove an entire key value pair, since the value can't exist in the dictionary without the key. To do this, we use the `pop()` function with the name of the **key** to remove the whole pair. For example

```python
user_account = {
    'username':'pbloom',
    'balance':270.26
}

# Remove the key 'balance', along with its value
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

# 4. Looping through dictionaries

Just like with lists, we will often want to loop through our dictionaries. But what happens when we loop through a dictionary?

```python
user_account = {
    'username':'pbloom',
    'balance':270.26,
    'deposits': [100.00, 21.34, 2.31, 8.06],
    'withdrawals': [-2.31, -21.43, -78.00],
    'email_notifications': True
}

for item in user_account:
    print(item)
```

What is `item` in this case-- is it the key, is it the value, is it the key-value pair? Let's find out.

```console
username
balance
deposits
withdrawals
email_notifications
```

Looping through a dictionary will only print out the keys of the dictionary. We can _use_ the keys to get the definitions, as we've learned, like so:

```python
user_account = {
    'username':'pbloom',
    'balance':270.26,
    'deposits': [100.00, 21.34, 2.31, 8.06],
    'withdrawals': [-2.31, -21.43, -78.00],
    'email_notifications': True
}

for key in user_account:
    print(f'{key}: {user_account[key]}')
```

```console
username: pbloom
balance: 270.26
deposits: [100.0, 21.34, 2.31, 8.06]
withdrawals: [-2.31, -21.43, -78.0]
email_notifications: True
```

You can also use dictionary methods (like string methods and list methods, and like `pop` that we used above!) to get the keys, values, or key-value pairs specifically.

```python
for key in user_account.keys():
    print(key)
```

brings us back to

```console
username
balance
deposits
withdrawals
email_notifications
```
,
```python
# Remember, the variable `value` here can be named whatever we want it to
for value in user_account.values():
    print(value)
```

gets us

```console
pbloom
270.26
[100.0, 21.34, 2.31, 8.06]
[-2.31, -21.43, -78.0]
True
```

and finally,

```python
for pair in user_account.items():
    print(pair)
```

gets us

```console
('username', 'pbloom')
('balance', 270.26)
('deposits', [100.0, 21.34, 2.31, 8.06])
('withdrawals', [-2.31, -21.43, -78.0])
('email_notifications', True)
```

There's a lot that these methods enable you to do, as you get comfortable with them!

# Overview of what we learned today

* How to use a dictionary to store several types of data
* How key-value pairs work in a dictionary
* How to add, update, and remove, items in a dictionary
* Some key differences between lists and dictionaries

### Next up: functions!

As we write more (and more complex) code, we'll want to be able to save whole chunks of code to use in multiple places or in later programs. We do this by creating our own functions!
