# Bootcamp 1

**First, have students make a folder called `bootcamp_scripts` in the `class_scripts` folder in their `jtc_class_code` github repo (`.../jtc_class_code/class_scripts/bootcamp_scripts`).**

-   We can use this folder over the rest of the bootcamp for storing practice scripts made in lessons

** Tell students this is day 1 of Python Bootcamp and explain lesson outline**

Today is our first class of Python Bootcamp material! By the end of the lesson, you'll:

1. Be able to write python scripts that output or `print` things
2. Feel comfortable working with the Integer data type
3. Feel comfortable working with the Float data type
4. Be able to include comments in your python scripts
5. Feel comfortable assigning and updating variables

## 1. Print statements

-   Demonstrate what printing is by printing a string in a new script called `print_exercise.py` in the `bootcamp_scripts` folder

```python
print('hi, this is your computer speaking')
```

### Printing requires parenthesis!

-   Show what happens if you don't use parenthesis in the print statement -- explain the error

```python
print 'hi, this is your computer speaking'
```

### Printing multiple things

Show students that

-   python scripts execute line by line
-   print statements on multiple lines will print out in order

```python
print('hi, this is your computer speaking')
print('i can run a lot of python code')
```

-   you can't have multiple print statements on the same line

```python
print('hi, this is your computer speaking') print('i can run a lot of python code')
```

## 2 & 3 Integers and Floats

Show students that numbers don't need

## 2. Comments

-   Show students how to add comments to code
-   Explain some good commenting practice
-   Show how commented out code does not evaluate

```python
# this line of code prints out a first line of text
print('hi, this is your computer speaking')

# this line of code prints out a second line of text
print('i can run a lot of python code')
```

#### Commenting out big chunks

-   Show how to toggle commenting out big chunks of code

## 3. Assigning & updating variables

To learn about variables, let's make a new script in the `bootcamp_scripts` folder called `variables.py`

#### What are variables?

-   We can explain what variables are using the box metaphor.
    -   "Variables are boxes -- we can refer to the box by name and select which box we want, and each box also can have stuff stored inside it"

#### Assigning variables

-   Explain that variable assignment always uses **a single equals sign**: `=`
-   assign a string variable and run the script with no other code -- ask students why they get nothing back

```python
firstname = 'Paul'
```

-   show that the assigned string variable can be printed by adding a print statement
    -   Back to the box metaphor, this is like looking at the contents of the box

```python
# assign the variable
firstname = 'Paul'

# print out the contents of the variable
print(firstname)
```

#### Variable naming conventions

There are a few rules for naming variables when we assign them:

-   They can't start with numbers
-   They can't have spaces in them
-   Rules aside, one very useful convention is to use all lowercase letters in variable naming, and to separate each word with an underscore (`_`).
    -   For example: `my_new_variable` or `birthday_year`

#### Updating variables

-   show students that an existing variable can be reassigned
-   explain that this 'overwrites' the previous value

```python
variable_a = 'this is variable a'
print(variable_a)
variable_a = 'this is variable b'
print(variable_a)
```

#### Variable errors

-   Show what happens if you misspell a variable name and try to print a variable that doesn't exist

```python
# assign the variable
first_name = 'Paul'

# print out the contents of the variable (but we misspelled it)
print(firstname)
```

## Overview

So, what have we learned during this lesson?

-   How to get python to print out things to the command line when you run scripts
-   How to document code with comments that will not be run
-   How to make variables, reference them by name, and assign/update/print their contents
-   All of these skills will be super important for progamming in python, and most will carry over to other coding languages too!
