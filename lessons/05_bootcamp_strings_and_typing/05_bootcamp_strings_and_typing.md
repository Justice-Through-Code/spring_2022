# Bootcamp class 2

<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

* Make sure you feel comfortable assigning and updating variables
* Make sure you can add comments to document your scripts

# Outline of class agenda

Today we'll learn more about the **string** data type in Python. By the end of the lesson, you'll:

1. Be able to work comfortably with **string** (text) data in python
2. Be able to do more type conversion between various data types
3. Have been introduced to the **boolean** data type
4. Take input from your program's user in the command line


## Strings (text)

In general, strings are how we work with text in python! The most important thing to remember about strings is that **they always must have quotes around the text**. The quotes can be either **single quotes** (`'`) or **double quotes** (`"`), but either way they have to match.

To work with strings today, let's make a new python script `bootcamp_scripts/strings_practice.py`

Strings are an incredibly powerful data type, because so much of human/computer interaction happens through text.

### Printing Strings

Let's remind ourselves of a basic string with a print statement:

```python
print('This is a basic string.')
```

We get

```console
$ python3 strings_practice.py
This is a basic string.
```

Let's add a variable to the mix, with a string in it. Create a variable that holds your name in it. Remember to put your name in quotes so python knows you're creating a string!

I don't just want to print my name, I want to print 'Hi, my name is Lillie.'. As simple as this goal may seem, there are many different ways to do it. Today we're going to learn about three.

#### 1. Printing out multiple things at once

We've talked about how python reads your code line by line, and how because of this, you can't do something like put two print statements on the same line. A single `print` statement, however, is very powerful. You can print multiple things in a single `print` statement by separating them with a comma. So to reach our goal of printing out a hello with our `name` variable, we can do:

```python
name = 'Lillie'

print('Hi, my name is', name, '.')
```

We're printing out 3 different items here: the first string (`'Hi, my name is'`), our name variable (`name`), and then the string with the period at the end of our sentence (`'.'`). Make sure you have a comma after each item you print out **except** the last one. The commas tell the print statement that more items are coming.

```console
$ python3 strings_practice.py
Hi, my name is Lillie .
```

You can print as many things as you want in a single print statement like this, and they don't even all have to be strings. You can print strings, integers, floats, etc, all in a single print statement, by separating them with commas.

But this method has some drawbacks-- you can see that the `print` statement adds a `space` between every item you print out, which is creating a problem with our period at the end of the sentence. Under the hood, it also handles each item you give it separately, which takes longer and is not always what you want.

#### 2. Concatenating strings

This brings us to our second option: concatenating strings. 'String Concatenation' is a fancy word for joining strings together. Concatenation is a super useful tool, and luckily, in python it's really easy-- to concatenate two strings together, use a plus sign.

Let's replace our commas with plus signs, to combine all three of our strings into one before we print it.

```python
name = 'Lillie'

print('Hi, my name is' + name + '.')
```

```console
$ python3 strings_practice.py
Hi, my name isLillie.
```

All the extra spaces went away! Concatenation is an important tool to have in your toolbelt, but when it comes to printing, there's one even better option to get what we're looking for.

#### 3. F-strings

There is a special type of string in python called an `f-string`. The 'f' stands for 'formatted' (or 'fancy', if you prefer). f-strings allow us to insert other items (like variables, integers, etc) into our strings directly.

We know what we want at the start of our string (`'Hi, my name is'`), and we know what we want at the end (`'.'`). What we don't know is the name in our `name` variable. So we can _insert_ that variable into our formatted string exactly where we want it, ala:

```python
name = 'Lillie'

print(f'Hi, my name is {name}.')
```

Notice we've changed a couple things. First of all we added the `f` before the string, which tells python that this is a formatted string. We've also condensed it down from dealing with three separate elements, so that they're visually all combined into one. The item that we've inserted, our `name` variable, is encased in curly brackets. These tell python that whatever's inside the curly brackets should be inserted into the `f-string`. And because it's formatted, we can see that there's a space _before_ the name, but not between the name and the period. Let's see what this prints out when we run it.

```console
$ python3 strings_practice.py
Hi, my name is Lillie.
```

Success! `f-strings` are incredibly powerful.

### String Methods

There's a lot of builtin things that you can do to strings in python. These are called 'string methods'. We'll talk more about methods later, but you can think of 'string methods' as 'methods of manipulating strings'. We won't learn them all today, but if you ever find yourself wondering if you can do something with or to a string, google will be able to tell you everything you need to know. For now, let's go through a couple commonly used python string methods.

#### <str>.upper()

You may want to turn a whole string into uppercase letters. Python has a method for that:

```python
print("Hi, I'm really excited to be here (: ".upper())
```

```console
$ python3 strings_practice.py
HI, I'M REALLY EXCITED TO BE HERE (:
```

Note that the spaces and punctuation marks didn't change, but the letters did. Python knowsss.

#### <str>.lower()

Alternatively you can turn an entire string to lowercase too.

```python
print("Bell Hooks wrote her name all lowercase.".lower())
```

```console
$ python3 strings_practice.py
bell hooks wrote her name all lowercase.
```

And there we are.

#### <str>.replace()

Sometimes you'll want to replace all the times something shows up in your string with something else. For instance, say you want to protect all instances of your password in a string (silly example, but cool output).

```python
password_info = 'do NOT FORGET, the password is 1234. Remember, 1234. easy peasy, 1234.'

print(password_info)
```

This is probably bad. But, we can `replace` all the instances of the password in our print statement so that they don't print out:

```python
password_info = 'do NOT FORGET, the password is 1234. Remember, 1234. easy peasy, 1234.'

print(password_info.replace('1234', '*******'))
```

2 things! You'll notice that the `replace` method has items inside its parentheses. `replace` needs to know a) what substring it's replacing, and b) what substring it's replacing (a) with. We give it that information inside its parentheses. Also, remember that even though `1234` is a number, it's part of a **string**. This means that to change it, we need to put quotes around it.

```console
$ python3 strings_practice.py
do NOT FORGET, the password is *******. Remember, *******. easy peasy, *******.
```

Success!

#### <str>.count()

Sometimes you'll want to count the number of times something occurs in a string. Just for fun, try:

```python
sentence = 'How many times does the letter "t" show up in this string?'
num_ts = sentence.count('t')

print(num_ts)
```

```console
$ python3 strings_practice.py
7
```

That is correct! This one is especially interesting, because even though `.count()` is a method that we use on our _string_, the answer that it gives us is a number.

But how do we know that what's printing out this time is a number and not a string? Just looking at the printout, it's hard to tell the difference:

```python
print('7', 7)
```

```console
$ python3 strings_practice.py
7 7
```

They look exactly the same. We need a way to tell which _type_ of data we're looking at.


### Data Types

We talked a bit last class about 'type conversion' for turning integers into floats and floats into integers. If we don't _know_ which type of data something is, there's a function we can use to figure it out called `type()`.

We can check our 7's using this function (and let's add a float for good measure):

```python
print(type('7'), type(7), type(7.0))
```

```console
$ python3 strings_practice.py
<class 'str'> <class 'int'> <class 'float'>
```

We'll talk more about what `class`es are in the future (by the end of the course you'll be writing your own!), but for now we can see that that the data types that get printed out match what we'd expect.

This shows us something else too: just like you can turn a float into an int with `int(5.4)` and vice versa with `float(8)`, you can do the same thing with strings using `str(8.423)`.

```python
int_var = 9
var_as_string = str(int_var)
var_as_float = float(int_var)

print(f'int_var: {type(int_var)}')
print(f'var_as_string: {type(var_as_string)}')
print(f'var_as_float: {type(var_as_float)}')
```

```console
$ python3 strings_practice.py
int_var: <class 'int'>
var_as_string: <class 'str'>
var_as_float: <class 'float'>
```

As expected!

### Booleans

So far we've worked with `int`s, `float`s, and `str`s. These are the basic building blocks that all other more complex data types are based off of, but there's one more that we haven't encountered yet. The fourth of these building blocks is called a `boolean`. Booleans are incredibly powerful, and there's only two options of what they can be: `True` or `False`.

To see a boolean in action, let's take a look at another couple string methods.

#### <str>.startswith()/<str>.endswith()

Another useful set of string methods are `startswith` and `endswith`. These will tell us whether or not a string starts or ends (respectively) with the given substring. In action, this looks like:

```python
phone_num = '718 555 1234'

is_nyc = phone_num.startswith('718')

print(phone_num)
print(is_nyc)
```

```console
$ python3 strings_practice.py
718 555 1234
True
```

`is_nyc` is `True`, because the phone number starts with 718. If we go in and change it, the result should change too.

```python
phone_num = '312 555 1234'

is_nyc = phone_num.startswith('718')

print(phone_num)
print(is_nyc)
```

```console
$ python3 strings_practice.py
312 555 1234
False
```

We can do the same thing with `endswith`.

```python
address = '555 Beverly Dr, Beverly Hills CA 90210'

is_fancy = address.endswith('90210')

print(address)
print(is_fancy)
```

```console
$ python3 strings_practice.py
555 Beverly Dr, Beverly Hills CA 90210
True
```

And it will give us `False` if we change the address:

```python
address = '555 Beverly Dr, Beverly Hills CA 90211'

is_fancy = address.endswith('90210')

print(address)
print(is_fancy)
```

```console
$ python3 strings_practice.py
555 Beverly Dr, Beverly Hills CA 90211
False
```

Now that you've encountered `boolean`s, you know all four building blocks of python, also referred to as the four `primitive data types`. All future complex data types will be built on top of these 'primitive' ones.

## BREAK: 3 minutes

## User Input

The last thing we'll be learning today is how to take input from someone using a program we write, in the command line.

If you want to show your friend what you've been working on in this class, you don't want your code to print out _your_ name, you want it to print out _theirs_. User input makes things a lot more interesting.

For getting user input through the command line, python has actually made it pretty simple: there's a function for that!

Let's go back to one of our first examples of the day:

```python
name = 'Lillie'

print(f'Hi, my name is {name}.')
```

Let's switch this up a bit. instead of saying 'my name is', let's have the computer say hello to the person:

```python
name = 'Lillie'

print(f'Hello, {name}!')
```

This gets us:

```console
$ python3 strings_practice.py
Hello, Lillie!
```

Now all that's left to change is that instead of 'hard-coding' your name into your script, we want our `name` string to come from the user.

Here's what we need to do:

```python
name = input('What is your name? ')

print(f'Hello, {name}!')
```

This gets us:

```console
$ python3 strings_practice.py
What is your name?
```

And our code _waits_ for the user input! Type in a name and hit enter.

```console
$ python3 strings_practice.py
What is your name? Yusuf
Hello, Yusuf!
```

Strings can do a lot of cool things, and now so can you!

## Overview of what we learned today

Okay! So in this lesson we learned about

* The `string` data type
* String 'concatenation' (adding strings together)
* Common string methods
* Data Types
* Booleans
* Taking user input

**What's next?**
Soon we'll be moving on to learning about *logic* in programming -- how to check if certain conditions are met or now, and how to use this to control which code runs, and how.


## Challenges

Today's challenge is `strings_challenge.py` in your pod repos. There is also an extra challenge in the folder (`nba_challenge_EXTRA.py`), but this one is not required to be turned in! If you'd like more practice, feel free to finish it, but it will not be required for your grade.

## Extras

In python, there are special characters for things like new lines (like hitting `return` on your keyboard) (`'\n'`) and tabs (`'\t'`). Try them out!
