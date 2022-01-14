## 1. Refresh on box metaphor
* Variables are boxes: variable names are like labels, the data are what's stored in the box

## 4. Integers

**For this section and the next, have students make a new script in `bootcamp_scripts` called `integers_floats.py`**

#### Primitive data types

* Give brief overview that there are 4 primitive data types

#### What are integers?

* Whole numbers

#### Math in python / working with integers

Show students these common math operations in python with print statements using integers

* Addition: `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Exponents `**` (i.e. `5**2` means 5 squared (to the 2nd power), or `3**9` means 3 to the 9th power)


```python
print(1+3)
print(1*3)
print(1-3)
```


#### Integers as variables

* Show that integers can be assigned to variables, and you can do math with the variables

```python
# assign a positive integer to a variable
positive_number = 10

# assign a negative integer to a variable
negative_number = -5

# add the values of the two variables and print
print(positive_number + negative_number)
```


## 5. Floats

* Floats, unlike integers, **do have decimal points**
* Show some math operations with floats too
* Show that some operations on integers (divison) return a float back

```python
print(1.1+3.1)
print(1.5*2)
print(1-3.736)
```


#### Order of operations

* Explain briefly that python math follows order of operations
* Show that parentheses matter

```python
var_a = 2+3*4
var_b = (2+3)*4
print(var_a)
print(var_b)
```
### Type conversion

* Show using `float()` to convert to float and `int()` to convert to integer
* Explain that you can lose info when going from float to integer

## 2. Strings!

* explain these are for text, always have quotes
* make a new script `strings_practice.py` to practice with strings

## 3. making strings

* show they can be assigned to variables /printed
* strings *(what's in the box)* CAN have spaces even though var names can't *(box labels)*
* show that strings can have numbers inside of them (numbers can be text too)


## 4. Demonstrate escape characters

Can use a bunch of lyrics to demonstrate how long strings are inconvinient

```python
# note: this text may go out on one line of your python script if you're in atom/sublime
lyrics = 'At first I was afraid, I was petrified, Kept thinking I could never live without you by my side, But then I spent so many nights thinking how you did me wrong, And I grew strong'
print(lyrics)
```

* show how to use `\` to break up the string in the script
    * show that this ONLY affects how the code is seen, not print output



Show how to make new lines/tabs in strings
 * `\n` adds a new line
 * `\t` adds a tab indent
 

Demonstrate by separating the lyrics with lines/tabs


## 5. f-strings

* Show an example of using an f string
* Explain this is a good way to print out text with embedded variables

For example:

```python
# set an integer variable called profit
profit = 120

# make a formatted string that includes the profit variable
my_f_string = f'The profit today is ${profit}'

# print it
print(my_f_string)
```



## 6. String concatenation with `+`

* Ask students what they think will happen if two strings are added together with `+`
* show them that this concatenates them!



## 7. `.upper()` and `.lower()`

Strings have some special functions that allow us to make them all upper (`.upper()`) or all lower (`.lower()`) case.


* Show students making all the lyrics all caps or all lower
* Show that this is a STRING method, doesn't work with another data type


## 8. Boolean variables (`True`/`False`)

* Explain that this is the 4th primitive data type
* We use this for true/false, and say this will be useful later when we will need python to EVALUATE things and MAKE DECISIONS in an automated way
* make a script `boolean_practice.py` to practice:


## 9. Demonstrate some boolean variables

* Show they print out as `True` or `False`
* Show that the capitalized first letter matters -- not boolean if not



## 10. Finding out variable classes with `type()`

Mention that we'll review this from last time

* it's helpful to know **what kind of object** a variable is.
* We can use the `type()` function to do this. 
* show what happens when we look at the type for variables of string/boolean data types


## 11. More type conversions

* Show that all other primitive data types can be converted to strings with `str()`
* If time, show how converting from string --> other primitive data types won't always work depending on the contents of the string