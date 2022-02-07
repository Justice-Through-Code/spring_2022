# Bootcamp 1
<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

* Make sure you feel comfortable with using the command line
* Make sure you feel comfortable pushing changes to your course folder to your course github repo
* Make a folder called `jtc_class_code` wherever you're keeping your JTC content

# Outline of class agenda

Today is our first class of Python Bootcamp material! By the end of the lesson, you'll:

1. Be able to write python scripts that output or `print` things
2. Feel comfortable working with the Integer data type
3. Feel comfortable working with the Float data type
4. Be able to include comments in your python scripts
5. Feel comfortable assigning and updating variables


# Class

One thing you might be wondering today as we start the bootcamp is: what exactly *is* a python script?
* A Python script is any bit of valid Python code in a file with the .py extension (there's nothing special about this extension, it just tells your computer that the file has python code)
* Code itself is just text written with the syntax and key words of the programming language


## 1. Print statements

In coding terms, 'printing' means to **'print' to the screen**. This allows you to **display** what your code is doing. Printing is useful both to do some pretty cool things with, _and_ to debug your code when things go wrong.

First, make a new file called `print_exercise.py` in your `jtc_class_code` folder. We'll use this script to get comfortable working with print statements. You can open this up in your text editor to get started.

### Printing text

To get started, let's print out some text just like we did with the `hello_world.py` script we made last week. On the first line of this file, let's add the following:

```python
print('hi, this is your computer speaking')
```

Now, run your script from the command line (make sure you've `cd`'d into your `jtc_class_code` folder) with:

```console
$ python3 print_exercise.py
```

We can see that when we run the script, we get 'hi, this is your computer speaking' **printed** out for us. Nice!

### Printing requires parentheses!

You'll notice that we needed to put both *single quotes and parentheses* around the actual text we wanted to print out.
* The quotes are to turn our text into something called a 'string'. We'll get into more detail about this soon when we cover [strings](https://www.w3schools.com/python/python_strings.asp) (tldr: strings always have quotes around them).
* In Python version 3 (most likely what you're using for this class), you need to put any _text_ that you want to print out in parentheses.

Let's see what happens if we leave out the parentheses and change the script to:

```python
print 'hi, this is your computer speaking'
```

Then if we run it from the command line again, we see:

```console
$ python3 print_exercise.py
  File "print_exercise.py", line 1
    print 'hi this is your computer speaking'
          ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hi this is your computer speaking')?
```

Errors can feel overwhelming, but they actually give us a lot of useful knowledge about how to fix our code. You can see it tells us

`File "print_exercise.py", line 1`: which file and line the error starts on,

`print 'hi this is your computer speaking'`: The breaking code on that line, and

`SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hi this is your computer speaking')?`: Even gives us a suggestion of how to fix it, along with what _type_ of error it is (in this case a `SyntaxError`. We'll see a lot of those).

### Printing multiple things

This might be a good place to point out that **python scripts generally execute line by line, in order from top to bottom**. So, if you write print statements on two consecutive lines, they'll print out in that order.

Try adding another print statement on a new line so your `print_exercise.py` script has:

```python
print('hi, this is your computer speaking')
print('i can run a lot of python code')
```
You should see each string ouput on its own line in the terminal!


```console
$ python3 print_exercise.py
hi this is your computer speaking
i can run a lot of python code
```

In general, each line of python code should be on its own line in the file. For example, if you try to do two print statements on one line, it doesn't work:

```python
print('hi, this is your computer speaking') print('i can run a lot of python code')
```

You'll see an invalid syntax error when you run this
```console
$ python3 print_exercise.py
  File "print_exercise.py", line 1
    print ('hi this is your computer speaking') print ('i can run a lot of python code')
                                                    ^
SyntaxError: invalid syntax
```

Because python runs code line-by-line, we can only put one print statement per line.


## 2 & 3. Integers and Floats

You can print out a lot more than just words with the print function. Python lets you print out numbers, and even do math inside your print statements. Let's make a new file called `integers_floats.py`.

In this new file, print an integer. (Hint: Just like in math, integers are **whole numbers** -- they can be positive, negative, or zero. Integers do not contain any decimal points.)

```python
print(4)
```

Notice that you don't need quotes when you're working with numbers. We'll talk about why that is later in class. Let's try some math!

```python
print(1 + 3)
print(1 * 3)
print(1 - 3)
```

This gives us the answers we'd expect for each equation:

```console
$ python3 integers_floats.py
4
4
3
-2
```

Where does that first `4` come from? Notice that our earlier printout, `print(4)` is still there. When we don't want to erase code, but we want the computer to ignore it, we can do something called 'commenting it out'. You can turn any line in your script into a **comment** by putting a `#` at the front of the line. The computer will ignore any line with a hashtag at the front. Let's try it.

```python
# print(4)

print(1 + 3)
print(1 * 3)
print(1 - 3)
```

Now we see the output we expect.

```console
$ python3 integers_floats.py
4
3
-2
```

Note that the computer also ignored the empty line we added. It ignores all of those too.

Commenting out code that we want to ignore isn't the only thing comments are good for. In fact, adding comments to your code that describe what the code is doing is one of the most important things you can do. Both [for yourself](https://dev.to/sunnysingh/writing-code-for-your-future-self-3da2) and for any teammates you're writing your code with. You can check out [this guide](https://realpython.com/python-comments-guide/) for writing effective comments in your code.

### Commenting out big chunks

Want to comment a bunch of lines out at one time? You can do this in many code editors on a Mac with `command` + `/`, or on Windows with `control` + `/`

### Math in python

One of the benefits of code is that it can do complex work (like math) for us. In order for us to utilize this power, we need to know how to tell the computer what to do.

Here's how to do the most common mathematical operations in python:

* Addition: `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Exponents `**` (i.e. `5**2` means 5 squared (to the 2nd power), or `3**9` means 3 to the 9th power)

Let's add a couple more printouts for division and exponents (feel free to comment out the previous printouts as you go).

```python
print(4 / 2)
print(5 ** 2)
```

```console
$ python3 integers_floats.py
2.0
25
```

Notice anything interesting about the division output? Python added a decimal point to the answer. In Python3, a single slash (`/`) is what's called 'float division'. Floats are what coding languages call numbers with decimals in them. Computers differentiate between integers and floats because floats take up slightly more memory than integers, but they allow for more precision if we have numbers that aren't whole.

Math works as we'd expect with floats too. For example:

```python
print(1.1 + 3.1)
print(1.5 * 2)
print(1 - 3.736)
```

Gives us:

```console
$ python integers_floats.py
4.2
3.0
-2.736
```

#### Order of operations

Just like a calculator, python uses the 'order of operations' to evaluate equations. The acronym [PEMDAS](https://thehelloworldprogram.com/python/python-operators-order-precedence/) tells us the order in which python will evaluate:

* **P**arentheses
* **E**xponents
* **M**ultiplication
* **D**ivision
* **A**ddition
* **S**ubtraction

So, if we have the following code:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

We can expect the result to be:

`2 + 3 * 4`: 3 * 4 = 12; 2 + 12 = **14**

`(2 + 3) * 4`: (2 + 3) = 5; 5 * 4 = **20**

And we get:

```console
$ python3 integers_floats.py
14
20
```

Don't worry, you won't need to do too much math in this course! And like everything, these math rules can always be googled if and when you need them.

### Type conversion

Sometimes, we'll want to convert integers to floats ourselves, and vice versa. This is called *type conversion*, because you are _converting_ the _type_ of the object from one thing (`int`) to another (`float`) etc etc. We can do so by using the `int()` function to convert to integer, and the `float()` function to convert to float. For example:


```python
print(float(2))
print(int(3.856))
```

gets

```console
$ python3 integers_floats.py
2.0
3
```

Is it surprising that turning `3.856` into an integer returns `3` instead of `4`? Type conversion is _not_ the same as rounding. Using the `int()` function ONLY pays attention to the `int` part of a number. There is also a `round()` function if you're looking for that functionality instead.

```python
print(round(3.856))
```

```console
$ python3 integers_floats.py
4
```

### Primitive data types

So far today we've worked with 3 different types of data: strings, integers, and floats. Along with a fourth data type called a `boolean` that we'll learn about in a later class, these are what's called the [primitive data types](https://able.bio/ZoranPandovski/understanding-python-3-data-types-string-int-float-and-boolean--57tqcfp) of python (and most other coding languages). You can think of the primitive data types kind of like the primary colors-- all more complex colors, and more complex types of data, will be built on top of these.


## BREAK - 5 minutes

## 4. Variables

Often you'll want to keep track of different pieces of data so that you can use them multiple times. When we want to save a piece of data to use later in our script, we can save it in a **variable**.


To learn about variables, let's make a new script in the `jtc_class_code` folder called `variables.py`

#### What is a variable?

One way to think of a variable is as a box you can put other things into, and you can use the name of the box wherever you want your code to refer to what's inside.

Let's see a real life example:

Think of an actual box you might keep in your attic, say a box of christmas decorations. You might write 'christmas decorations' on the box so that you have an idea of what's inside. But _inside_ the box, there might be `'tinsel'`, or `'christmas lights'`, or `'ornaments'`, or even all of the above. The _name_ of the box, or in our case, the `variable`, doesn't change, but what's inside can.

#### Assigning variables

Let's see how this actually works in python.

Variables in python are always assigned as `<variable_name> = <variable_data>`. So to turn our example above into code, write the following in `variables.py`

```python
# assign a variable
christmas_decorations = 'tinsel'
```

What do you think will happen when we run this code? Nothing! Why?

There's no error, which means we didn't break the code, but we also didn't print anything out.

If we add a print statement, we can see what's inside the variable:

```python
# assign a variable
christmas_decorations = 'tinsel'
print(christmas_decorations)
```

```console
$ python3 variables.py
tinsel
```

There it is! Note that we don't need quotes around our variable name in order to print it out. In fact, putting quotes around the variable name would print out the word `'christmas_decorations'`, not our variable. By printing out the variable name, we're telling Python that hey, we have a 'box' in our code, called `christmas_decorations`, that's holding some data. Please go grab that box and print out what's inside it.

As with any box, we can change what's inside without changing the box. For instance, let's change what's inside our variable and print it out each time.

```python
# assign a variable
christmas_decorations = 'tinsel'
print(christmas_decorations)

# update the variable data
christmas_decorations = 'christmas lights'
print(christmas_decorations)

# update the variable data
christmas_decorations = 'ornaments'
print(christmas_decorations)
```

```console
$ python3 variables.py
tinsel
christmas lights
ornaments
```

We're changing what's _inside_ our variable in between each time we print it out, so the output changes each time.

We can update variables as many times as we want, but it is important to keep in mind that we lose the previous value stored in a variable when we reassign it. So, if we need to store more information, we often need multiple variables at the same time.

#### Variables in action

We can see how powerful variables are when we need to keep track of things like amounts.

Say you're having some people over and you need to figure out how much food and drink to get. We can use variable names to help us decide:

```python
number_of_people = 5

drinks_per_person = 3
ice_cream_per_person = 1

print('How many drinks to get:')
print(number_of_people * drinks_per_person)

print('How much ice cream to get:')
print(number_of_people * ice_cream_per_person)
```

This gets us:

```console
$ python3 variables.py
How many drinks to get:
15
How much ice cream to get:
5
```

Note that we use the variable `number_of_people` twice. This is where variables get super helpful-- say someone cancels. Instead of looking through your code to find all the places you used the number 5 (and hoping they were all referencing the number of guests), you can just change the number inside the variable, and it updates everywhere.

```python
number_of_people = 4

drinks_per_person = 3
ice_cream_per_person = 1

print('How many drinks to get:')
print(number_of_people * drinks_per_person)

print('How much ice cream to get:')
print(number_of_people * ice_cream_per_person)
```

Becomes

```console
$ python3 variables.py
How many drinks to get:
12
How much ice cream to get:
4
```

### Variable naming conventions

There are a few rules for naming variables:
 * They can't start with numbers
 * They can't have spaces in them

I should also note that while these variable names are very descriptive, which is good, they're also a little long. You want to make your variable names as short as possible while still being descriptive. So maybe `number_of_people` becomes `num_guests`.

Rules aside, one very useful convention is to use all lowercase letters in variable naming, and to separate each word with an underscore (`_`).

Check out the [PEP 8 guide](https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables) for more info on style in creating variable names.

### Variable errors

One problem you might hit a lot is if you misspell a variable name. For example, let's update our variable name to shorten it like we talked about:

```python
num_guests = 4

drinks_per_person = 3
ice_cream_per_person = 1

print('How many drinks to get:')
print(number_of_people * drinks_per_person)

print('How much ice cream to get:')
print(number_of_people * ice_cream_per_person)
```

Now, when you run the script, you'll see:

```console
$ python3 variables.py
Traceback (most recent call last):
  File "variables.py", line 7, in <module>
    print(number_of_people * drinks_per_person)
NameError: name 'number_of_people' is not defined
```

Oops! We changed the name of our variable, but tried to print out the old name. If you see this error, you'll know to check your variable names to make sure you've created the variable you want to work with. If we update the rest of our code with our new variable name, our code will work again.

## Overview

So, what have we learned during this lesson?
* How to get python to print out things to the command line when you run scripts
* How to work with the two numeric basic data types: integers and floats
* How to document code with comments that will not be run
* How to make variables, reference them by name, and assign/update/print their contents


All of these skills will be super important for progamming in python, and most will carry over to other coding languages too!

## Challenges

In your pods, start with `first_python_challenge.py`. `temperature_challenge.py` should also be completed for this class, though you may not finish (or start!) with your pod. Have fun!


## Extras

Python can do a lot more math than what we talked about in class! For instance, try googling the three different types of division: float division (`/`), integer division (`//`), and remainder division (`%`).
