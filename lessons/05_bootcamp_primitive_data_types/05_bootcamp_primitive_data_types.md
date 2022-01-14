# Bootcamp class 2

<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

* Make sure you feel comfortable assigning and updating variables
* Make sure you can add comments to document your scripts

# Outline of class agenda

Today we'll learn about the **primitive data types in python - integers, floats, strings and booleans**. By the end of the lesson, you'll:

1. Be able to work comfortably with **integer and float** data in python
1. Be able to work comfortably with **string** (text) data in python
2. Be able to work comfortable with **boolean** (True/False) data in python
3. Be able to do some type conversion between various data types


# Primitive data types

We're now going to learn about the 'primitive' data types in python, that form the basis for all other kinds of data we'll work with this semester. There are [4 of them total](https://able.bio/ZoranPandovski/understanding-python-3-data-types-string-int-float-and-boolean--57tqcfp) Let's get started!

## Integers

For this section and the next, let's make a script in `bootcamp_scripts` called `integers_floats.py`

#### What are integers?

Just as with math, integers are **whole numbers** -- they can be positive, negative, or zero. Integers do not contain any decimal points.

#### Math in python / working with integers

We can perform mathematical operations with integers using arithmetic operators. Let's look at some operators we can use:

* Addition: `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Exponents `**` (i.e. `5**2` means 5 squared (to the 2nd power), or `3**9` means 3 to the 9th power)

Python can function as a calculator for working with integers, let's try it!

```python
print(1+3)
print(1*3)
print(1-3)
```

This gives us the answers we'd expect for each equation:

```console
python integers_floats.py
4
3
-2
```

We can also assign integers to variables and work with them that way. To test this out, in `integers_floats.py`, let's do the following:

```python
# assign a positive integer to a variable
positive_number = 10

# assign a negative integer to a variable
negative_number = -5

# add the values of the two variables and print
print(positive_number + negative_number)
```

When we run this from the command line, we get:

```console
$ python integers_floats.py
5
```

## Floats

Floats, unlike integers, **do have decimal points**. They take up slightly more memory than integers, but they allow for precision if we have numbers that aren't whole.

Math works as we'd expect with floats too. For example:

```python
print(1.1+3.1)
print(1.5*2)
print(1-3.736)
```

Gives us:

```console
$ python integers_floats.py
4.2
3.0
-2.736
```

Now let's try something a little bit tricky here. What if we try the following?

```python
my_answer = 1/2
print(my_answer)
```

Here, we've divided one integer by another integer, but the answer is 0.5, which is not an integer! So, what happens when we run this?


```console
$ python integers_floats.py
0.5
```

We get a float back! So, python has automatically recognized that even though we started with two integers, we need a float for an answer.


#### Order of operations

Just like a calculator, python obeys order of operations conventions on which types of math equations are evaluated first. The acronym [PEMDAS](https://thehelloworldprogram.com/python/python-operators-order-precedence/) indicates that python will evaluate math in this order:
* **P**arenthesis
* **E**xponenents
* **M**ultiplication
* **D**ivision
* **A**ddition
* **S**ubtraction

So, if we write the following code:
```python
var_a = 2+3*4
var_b = (2+3)*4
print(var_a)
print(var_b)
```

We get:
```console
$python integers_floats.py
14
20
```

Parentheses like these can be especially important for controlling the order that python evaluates code with math in it.

### Type conversion

Sometimes, we'll want to convert integers to floats ourselves, and vice versa. This is called *type conversion*. We can do so by using `int()` to convert to integer, and `float()` to convert to float. For example:


```python
my_int = 2
my_float = float(my_int)
print(my_float)
```

So, we create an integer variable, convert it to float, then print it.

```console
$ python integers_floats.py
2.0
```

Now, we see that the variable prints out as `2.0`, showing us that it *is* a float, and has decimal places represented. Notably, this doesn't actually change the numerical value of the variable. (i.e. 2 is equal to 2.0 in math).

However, things are a bit different if we convert a float to an integer, then print:

```python
my_float_2 = 2.777
my_int_2 = int(my_float_2)
print(my_int_2)
```

Here, we **actually lose information and change the value of the number, because converting from a float to an integer basically just 'cuts off' everything after the decimal point**. Also, this is **not** what we'd get if we rounded the number (if we rounded to the nearest whole, we'd round up to 3!).

```console
$ python integers_floats.py
2
```

So, 2.777 gets changed to 2 when we go from a float to an integer. So, we have to be careful about our math if we convert in this direction!

## Strings (text)

In general, strings are how we work with text in python! The most important thing to remember about strings is that **they always must have quotes around the text**, and quotes can be either **single quotes** (`'`) or **double quotes** (`"`)

To work with strings today, let's make a new python script `bootcamp_scripts/strings_practice.py`

#### Creating strings

Just like we learned last time, strings can be assigned to variables using the `=` sign. In fact, when we learned about variable assignment, we were working with strings! We just hadn't talked about it yet

```python
# assign a string variable. 
street = 'Amsterdam Avenue'
# print the string variable
print(street)
```

Here I'm using single quotes, but double quotes would work too. The key is just to be consistent! This prints out the string variable as text:

```console
$ python strings_practice.py 
Amsterdam Avenue
```

One important point is that even though **variable names can't have spaces in them, strings themselves can include spaces**. Back to the box metaphor from last time, your box name can't have spaces in, but what you put inside the box can.  


#### Escape characters

In the above example, my string was nice and short. But maybe I have a longer bit of text, like some Gloria Gaynor lyrics:

```python
# note: this text may go out on one line of your python script if you're in atom/sublime
lyrics = 'At first I was afraid, I was petrified, Kept thinking I could never live without you by my side, But then I spent so many nights thinking how you did me wrong, And I grew strong'
print(lyrics)
```

When we run this, the text prints out in the console with as much as can fit on each line. (If you resize your command line window, you'll notice it might look different)

```console
$ python strings_practice.py 
At first I was afraid, I was petrified, Kept thinking I could never live without you by my side, But then I spent so many nights thinking how you did me wrong, And I grew strong
```

But, we can add what are called [**escape characters**](https://www.w3schools.com/python/gloss_python_escape_characters.asp) to get python to read strings in a nicer way for us and format them more particularly. For example, we can use the `\` to break up big chunks of text inside the code editor. This can be really useful so that we don't have lines that extend too far to the right. In fact, many code style guides recommend that each line is 80 characters long or shorter, so this keeps us organized and within this guideline.

```python
# this will help keep the formatting neater in the text editor
lyrics = 'At first I was afraid, I was petrified \
Kept thinking I could never live without you by my side \
But then I spent so many nights thinking how you did me wrong \
And I grew strong'
```

This helps in the code editor, but it actually doesn't change the printout when we run the code. However, there are two super helpful escape characters we can use to format the printed text.
 * `\n` adds a new line
 * `\t` adds a tab indent
 

Let's try making each line of the lyrics on a new line:

```python
lyrics = 'At first I was afraid, I was petrified \
\nKept thinking I could never live without you by my side'
print(lyrics)
```

When we run this, we get two separate lines split where we put the `\n`:

```console
At first I was afraid, I was petrified 
Kept thinking I could never live without you by my side
```

Here's an example with a tab indent:

```python
lyrics = 'At first I was afraid\tI was petrified.'
print(lyrics)
```

This prints as:

```console
At first I was afraid	I was petrified.
```

We can also combine as many new lines and tab indents as we want, for example:
```python
lyrics = 'At first I was afraid\n\tI was petrified\
\n\n\nKept thinking I could never live without you by my side'
print(lyrics)
```

This prints as:

```console
$ python strings_practice.py 
At first I was afraid
	I was petrified


Kept thinking I could never live without you by my side
```

#### Strings with code in them (f-strings)

It can be really helpful to have strings with other variables inside them. These are called formatted strings, or 'f-strings', and we can make them by adding a lower case f before the first quote sign in a string. Then, code can be inserted inside the string within `{}`

For example:

```python
# set an integer variable called profit
profit = 120

# make a formatted string that includes the profit variable
my_f_string = f'The profit today is ${profit}'

# print it
print(my_f_string)
```

So, when we run this, we get:

```console
$ python strings_practice.py 
The profit today is $120
```

So, f-strings can be really useful if we want to print out values of variables with some other text. F-strings can also have equations right inside them, like this:

```python
print(f'If I earn $200 and expenses are $60, my profit is ${200-60}')
```

This shows up as 

```console
If I earn $200 and expenses are $60, my profit is $140
```

#### Concatenating strings

We can concatenate, or join together strings with the `+` sign. It might seem a little weird that 'addition' works with strings, but you can think of this more like joining them together.

For example:
```python
# make 2 strings
fruit1= 'apple'
fruit2 = 'banana'

# concatenate the strings
fruit3 = fruit1 + fruit2

# print out
print(fruit3)
```

This gives us the combined strings:

```console
python strings_practice.py 
applebanana
```

#### Upper case & lower case

Strings have some special functions that allow us to make them all upper (`.upper()`) or all lower (`.lower()`) case.


```python
lyrics = "At first I was afraid"
print(lyrics.upper())
print(lyrics.lower())
```

We can see that these functions convert our entire text to upper or lower case:

```console
$ python strings_practice.py 
AT FIRST I WAS AFRAID
at first i was afraid
```


#### Strings can have numeric characters in them

We haven't explicitly talked about it yet, but strings CAN have numbers in them, but inside strings, these numbers are **characters** -- i.e the numbers are just read as parts of the text. When numbers are inside a string, python doesn't consider them to have numeric values in the ways that integers and floats do. 

## Booleans (`True`/`False`)

The [Boolean data type](https://problemsolvingwithpython.com/04-Data-Types-and-Variables/04.02-Boolean-Data-Type/#:~:text=In%20Python%2C%20boolean%20variables%20are,the%20True%20and%20False%20keywords.&text=The%20output%20%3Cclass%20'bool',lowercase%20true%20returns%20an%20error.) in python can take two values, either `True` or `False`. 
Lets make a script at `bootcamp_scripts/boolean_practice.py` to practice:

Just like with strings, integers, and floats, we can save Boolean data to variables:

```python
var_a = True
var_b = False
print(var_a)
print(var_b)
```

When we run the script, we get:

```console
$ python boolean_practice.py 
True
False
```

One special thing about `True` and `False` in python is that they are ["reserved words"](https://www.programiz.com/python-programming/keywords-identifier) -- meaning they have special meaning in Python and are used for specific purposes only. 

We aren't going to spend a lot of time on Booleans now, but it is important to know them ast one of the four primitive data types. These types of data will come in very handy when we work with logic later on in this course!

## More type conversions

Now that we've familiarized ourselved with the primitive data types, it would be useful to know how to do convert one data type into another. However, this can be a little tricky -- as we saw last time, we can accidentaly lose information when we convert (for example from a float to an integer), so it's good spend some time thinking about how these conversions work.

### Finding the data type of a value

First, it's helpful to know **what kind of object** a variable is. We can use the `type()` function to do this. For example:


```python
# assign variables of each primitive data type
a = 'hi'
b = 2
c = 2.0
d = True

# print out which type they are
print(f'a: {type(a)}')
print(f'b: {type(b)}')
print(f'c: {type(c)}')
print(f'd: {type(d)}')
```

This gives us:
```console
$ python boolean_practice.py 
a: <class 'str'>
b: <class 'int'>
c: <class 'float'>
d: <class 'bool'>
```

Great, this prints out what **class** each variable is for each of the primitive data types. We'll learn more about classes later on in the course. This kind of use of `type()` can be especially useful if we have complex code and we're not sure what data types are assigned to variables at a given point in time. 

### Integers and floats to strings

We can convert integers and floats to strings using the `str()` function:

```python
# convert an integer to a string
my_string1 = str(2)

# convert a float to a string
my_string2 = str(2.7)

# print out the type to show they're both strings
print(type(my_string1))
print(type(my_string2))
```


### Strings to integers and floats

Converting strings to floats can be done with the `float()` function:

```python
my_string = '2.5'
my_float = float(my_string)
print(my_float)
```

This returns:
```console
$ python boolean_practice.py 
2.5
```

Converting strings to integers using the `int()` function, we have to be careful. This works...

```python
my_string = '2'
my_int = int(my_string)
print(my_int)
```

This returns:
```console
$ python boolean_practice.py 
2
```

But, if we have decimal points *inside the string*, python doesn't know how to convert these directly to an integer:

```python
my_string = '2.5'
my_int = int(my_string)
print(my_int)
```

This returns an error
```console
$ python boolean_practice.py 
Traceback (most recent call last):
  File "boolean_practice.py", line 2, in <module>
    my_int = int(my_string)
ValueError: invalid literal for int() with base 10: '2.5'
```

It isn't clear to python how to literally convert the string with decimal points into an integer, so it gives us an error. (If we really wanted to, we could convert string --> float first, then float --> integer)


**What if we have multiple numbers in a string though?**

```python
my_string = '2 + 5 + 0.3 + h89.403'
my_float = float(my_string)
print(my_float)
```

We get an error here because python isn't sure exactly how to treat this information as a number:

```console
$ python boolean_practice.py 
Traceback (most recent call last):
  File "boolean_practice.py", line 2, in <module>
    my_float = float(my_string)
ValueError: could not convert string to float: '2 + 5 + 0.3 + h89.403'
```

Why are we getting this error? Well, if we have a string with multiple numeric values in it, python isn't sure how we want to treat this as a number. Because there might be multiple ways we could get numeric value from this, it gives us an error just to be safe.

## Overview of what we learned today

Okay! So in this lesson we learned about

* The 4 primitive data types in Python
* We learned how to use operators with integers and floats to do math
* We learned how to format string in different ways
* We learned how to do type conversions between different data types

**What's next?**
Soon we'll be moving on to learning about *logic* in programming -- how to check if certain conditions are met or now, and how to use this to control which code runs, and how. 
