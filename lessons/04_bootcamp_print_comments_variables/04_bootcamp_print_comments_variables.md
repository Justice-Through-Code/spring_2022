# Bootcamp 1
<img src="https://i.ytimg.com/vi/N_Ls37qeQ4c/hqdefault.jpg" width="300">

# Before class

* Make sure you feel comfortable with using the command line
* Make sure you feel comfortable pushing changes to your course folder to your course github repo
* Make a folder called `bootcamp_scripts` inside the `class_scripts` folder in your `jtc_class_code` repository (your github repo)

# Outline of class agenda

Today is our first class of Python Bootcamp material! By the end of the lesson, you'll:

1. Be able to write python scripts that output or `print` things
2. Be able to include comments in your python scripts
3. Feel comfortable assigning and updating variables
4. Feel comfortable working with the Integer data type
5. Feel comfortable working with the Float data type




# Class

One thing you might be wondering today as we start the bootcamp is: what exactly *is* a python script?
* A Python script is any bit of valid Python code in a file with the .py extension (there's actually nothing special about this extension, it just helps your computer label it as python code)
* The python code itself is just plain text in the syntax of the programming language


## 1. Print statements

When you think of 'printing', you might initially think about printing on paper. But, to **print** in python means to **send back output, or to 'print' to the screen**.

Over the whole course, print statements will be helpful to you because they give you way to **display** what your code is doing.

First, make a new file called `print_exercise.py` in your `bootcamp_scripts` folder. We'll use this script to get comfortable working with print statements. You can open this up in your text editor to get started.

### Printing text

To get started, let's print out some text just like we did with the `hello_world.py` script we made last week. On the first line of this file, let's add the following:

```python
print('hi, this is your computer speaking')
```

Now, run your script from the command line (make sure you've set bootcamp script as your working directory) with:

```console
$ python print_exercise.py
```

We can see that when we run the script, we get 'hi, this is your computer speaking' **printed** out for us. Nice!

### Printing requires parenthesis!

You might be wondering why we needed to put both *single quotes and parenthesis* around the actual text we wanted to print out here.
* We'll get to the reason for the single quotes soon when we cover [strings](https://www.w3schools.com/python/python_strings.asp) (hint: strings always have quotes around them).
* In Python version 3 (most likely what you're using for this class), you need to put what you want to print out in parenthesis.

Let's see what happens if we leave out the parenthesis and change the script to:

```python
print 'hi, this is your computer speaking'
```

Then if we run it from the command line again, we see:

```console
$ python print_exercise.py
  File "print_exercise.py", line 1
    print 'hi this is your computer speaking'
                                            ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hi this is your computer speaking')?
```

This error looks confusing, but it is trying to help us to let us know we forgot parenthesis in our print statement! So, if you see this in the future, you can know to check your print statements for completion.

### Printing multiple things

This might be a good place to point out that **python scripts generally execute line by line, in order from top to bottom**. So, if you write print statements on two consecutive lines, they'll print out in that order.

Try adding another print statement on a new line so your `print_exercise.py` script has:

```python
print('hi, this is your computer speaking')
print('i can run a lot of python code')
```
You should see both lines ouput on their own lines at the command line!


```console
$ python print_exercise.py
hi this is your computer speaking
i can run a lot of python code
```

In general though, each line in python can only have one statement though. For example, if you try to do two print statements on one line, it doesn't work:

```python
print('hi, this is your computer speaking') print('i can run a lot of python code')
```

You'll see an invalid syntax error when you run this
```console
$ python print_exercise.py
  File "print_exercise.py", line 1
    print ('hi this is your computer speaking') print ('i can run a lot of python code')
                                                    ^
SyntaxError: invalid syntax
```

Because python runs code line-by-line, we can only put one print statement per line.

## 2. Comments

One of the **most important** things to do when programming is to add *comments* to your scripts so that anyone [(including yourself, in the future)](https://dev.to/sunnysingh/writing-code-for-your-future-self-3da2) looking at them later will be able to better understand them. You can check out [this guide](https://realpython.com/python-comments-guide/) for writing effective comments in your code.

In python, you can use the `#` symbol to make comments. Anything on a line to the right of the `#` will be a comment, and will not be run as code

Try adding comments to your `print_exercise.py` script similar to this:

```python
# this line of code prints out a first line of text
print('hi, this is your computer speaking')

# this line of code prints out a second line of text
print('i can run a lot of python code')
```

When you run your script, you should see exactly the same output as before. Notice, we added extra lines with white space -- python doesn't care about these though.


### Commenting out lines of code

Comments are **super useful** for making notes for yourself and others! One other thing about comments is that you can also comment out lines with actual python code in them, and these lines will be ignored when you run the script. For example, if you run:

```python
# this line of code prints out a first line of text
print('hi, this is your computer speaking')

# this line of code prints out a second line of text
#print('i can run a lot of python code')
```

You'll only see the first line of text printed out. So, commenting out code can be a helpful way to toggle pieces of code on/off when you are trying to work out specific parts of your scripts.


#### Commenting out big chunks

Want to comment a bunch of lines out at one time? You can do this in many code editors on a Mac with `command` + `/`, or on Windows with `control` + `/`

## 3. Assigning & updating variables

To learn about variables, let's make a new script in the `bootcamp_scripts` folder called `variables.py`

#### What are variables?
Variables are ways to save things in your code. One way to think of them is as little boxes you can put other things into, and you can use the name of the box wherever you want in your code to refer to what's inside the box. Any time you work with variables in python, it is important to be able to think of the **variable name** as what refers to **what is actually stored in the variable**.

#### Assigning variables

Variables in python are always assigned with **a single equals sign**: `=`
Let's check this out by adding the following code to `variables.py`

```python
firstname = 'Paul'
```

What we've done here is assigned `'Paul'` to the variable name `firstname`. So, we can think of `firstname` as the box, and `'Paul'` as what is inside the box.

When we run `variables.py`, however, nothing comes out! Why?

One key thing to remember is that **assigning variables produces no output**. So, we've saved `'Paul'` to the variable `firstname`, but we haven't told python to print anything out for us. We have to add a print statement for that. We can add some comments on each line too to remember how this works:

```python
# assign the variable
firstname = 'Paul'

# print out the contents of the variable
print(firstname)
```

So, now if we run the script, we see:

```console
$ python variables.py
Paul
```

Great, now we have output! We can think about using `print()` with variables as printing out for us *what is inside the box* after we tell python which box we want to print out.


#### Variable naming conventions

There are a few rules for naming variables when we assign them:
 * They can't start with numbers
 * They can't have spaces in them

Rules aside, one very useful convention is to use all lowercase letters in variable naming, and to separate each word with an underscore (`_`).

For example: `my_new_variable` or `birthday_year`

Check out the [PEP 8 guide](https://www.python.org/dev/peps/pep-0008/#method-names-and-instance-variables) for more info on style in creating variable names.

#### Updating variables

Updating variables is very similar to assigning them initially. The only difference is that there is an existing value stored in that variable, and you replace it. You can think of this as finding a box, and replacing what is inside it. When you do this, the prior information stored inside the variable (inside the box) is deleted.

For example, if we run the following code:

```python
variable_a = 'this is variable a'
print(variable_a)
variable_a = 'this is variable b'
print(variable_a)
```

We get different a different printout when we **update** (or 're-assign') `variable_a`:
```console
$ python integers_floats.py
this is variable a
this is variable b
```

We can update variables as many times as we want, but it is important to keep in mind that we lose the prior value stored in a variable when we reassign it. So, if we need to store more information, we often need multiple variables at the same time.

#### Variable errors

One problem you might hit a lot is if you misspell a variable name. For example, try updating your `variables.py` script to:

```python
# assign the variable
first_name = 'Paul'

# print out the contents of the variable (but we misspelled it)
print(firstname)
```

Now, when you run the script, you'll see:

```console
$ python variables.py
Traceback (most recent call last):
  File "variables.py", line 2, in <module>
    print(firstname)
NameError: name 'firstname' is not defined
```

Python is telling us that it is *looking* for the variable called 'firstname' in the print statement, but it couldn't find it! That's because it is 'not defined', indicating that we never assigned a variable with that name. If you see this error, you'll know to check your variable names to make sure you've assigned the variable you want to work with.

## 4. Integers

For this section and the next, let's make a script in `bootcamp_scripts` called `integers_floats.py`

#### Primitive data types

We're now going to learn about the 'primitive' data types in python, that form the basis for all other kinds of data we'll work with this semester. There are [4 of them total](https://able.bio/ZoranPandovski/understanding-python-3-data-types-string-int-float-and-boolean--57tqcfp) (integers, strings, floats, and boolean variables), and we'll learn about integers and floats today.

#### What are integers?

Just as with math, integers are **whole numbers** -- they can be positive, negative, or zero. Integers do not contain any decimal points.

#### Math in python / working with integers

Here's how to do the most common mathematical operations in python:

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


## 5. Floats

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

## Overview

So, what have we learned during this lesson?
* How to get python to print out things to the command line when you run scripts
* How to document code with comments that will not be run
* How to make variables, reference them by name, and assign/update/print their contents
* How to work with the two numeric basic data types: integers and floats


All of these skills will be super important for progamming in python, and most will carry over to other coding languages too!
