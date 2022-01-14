# Bootcamp class 6 - logic (instructor lecture outline)


# Outline of class agenda

Today we'll learn about **logic** in python. By the end of the lesson, you'll:

1. Understand what [**logical operators are**](https://realpython.com/python-operators-expressions/) and feel comfortable using them to test whether conditions are true or not
    * Get comfortable with using both single equals signs (`=`) and double equals signs (`==`)
    * Use `True`/`False` logic with all primitive data types
2. Combine logical operations into compound statements with `and`, `or`, and `not`
3. Feel comfortable with [**conditional statements**](https://realpython.com/python-conditional-statements/), and be able to use them to control how code runs 
    * Use `if`,`elif`, and `else` to control code flow
    * Get comfy with syntax for conditional statements (colons, indenting)
    * Get some experience with nested conditional statements
    * Using conditional statements with user input
4. Feel comfortable using `assert()` to check whether a certain condition is true before the rest of your code runs    
    

## 1. Comparison Operators

* Explain how logic can only result in `True` or `False` answers

### Numeric logic (math comparisons)

Show logical operators with math

* this code asks whether `1` is greater than `0`
```python
print(1 > 0)
```

Show students a variety of  **comparison operators**:

```python
a = 0
b = 1
c = 1

print(f'is a equal to b?: {a==b}')
print(f'is a not equal to b?: {a!=b}')
print(f'is a greater than b?: {a>b}')
print(f'is a less than b?: {a<b}')
print(f'is b greater than or equal to c?: {b>=c}')
print(f'is b greater less or equal to c?: {b<=c}')
```


### Equals signs (`=` vs. `==`)

Show students the difference between a single/double equals sign

```python
a = 2
```

```python
print(a == 2)
```

### Comparing integers and floats with another

Show that integers and floats compare in mathematical ways across data types 
```python
print(3 == 3.00000)
```


### Logic with Boolean variables

When it comes to logic in python, Boolean variables can be used mathematically such that:

* `True` is equal to `1`
* `False` is equal to `0`

```python
print(True == 1)
print(True == 1.0000)
print(True == 0)
print(True > 0)
print(False == 0)
```

**However, Boolean variables are NOT equal to strings with the same spelling:**
```python
print(True == 'True')
```

So, in summary, we can see that booleans can be treated mathematically and compared with floats and integers, but they are not so directly comprable with string data. 

### String Logic

Show that case matters with comparing strings
```python
# make some string variables
a = 'cat'
b = 'cat'
c = 'CAT'

# check if they're equal to one another
print(a == b)
print(a == c)
print(a != c)
```

Introduce that greater than / less than with strings might be weird because of Unicode comparisons


```python
print('cat' > 'bat')
```

This code evaluates to:
```console
True
```


## 2. Logical Operators (`or`, `and`, & `not`)


### `or`

With `or`, we can combine two conditions, and we will get `True` if **at least one (or both) is true**. For example:

```python
print(2 < 3 or 4 < 3) # only the first is true here
print(2 > 3 or 4 > 3) # only the second is true here
print(2 > 3 or 4 < 3) # neither are true here
print(2 < 3 or 4 > 3) # both are true here
```
Here we get:

### `and`

With `and`, we get `True` **only if both conditions are true**. So, if we repeat the same code as the previous piece but with `and`:

```python
print(2 < 3 and 4 < 3) # only the first is true here
print(2 > 3 and 4 > 3) # only the second is true here
print(2 > 3 and 4 < 3) # neither are true here
print(2 < 3 and 4 > 3) # both are true here
```

We would also see the same results by plugging in boolean variables themselves:
```python
print(True and False) # only the first is true here
print(False and True) # only the second is true here
print(False and False) # neither are true here
print(True and True) # both are true here
```

### `not`

With `not`, this **reverses** whatever existing logical operation exists. For example
```python
print(not 2 > 3)
print(not False)
print(not True)
```


#### Combining `and` and `not`

We can combine these two statements like so:

```python
a = 1
b = 2
print(a < 10 and not a > b)
```

## 3. Conditional Statements

* Tell students that THIS is really where logic starts to come in useful
* Diagram that this is where INDENTS really start to matter

### Introduce `if` statements

```python
# assign a to be equal to 5
a = 5
if a > 3:
    print('greater than 3!')
```

If we change it to be not true

```python
a = 2
if a > 3:
    print('greater than 3!')
```


### Introduce `else`

`else` is what we can use to tell python what to do if a condition is not met! So, if we return to the previous example, we can add an `else` statement below:

```python
a = 2
if a > 3:
    print('greater than 3!')
else:
    print('less than or equal to 3!')
```

we can have multiple lines of code inside these conditional statements, like so:

```python
a = 2
if a > 3:
    print(a)
    print('greater than 3!')
else:
    print(a)
    print('less than or equal to 3!')
```


* This is because all the code inside the indented `if` statement is being run. 

### Introduce `elif`

```python
a = 2
if a < 0:
    print('a negative number')
elif a > 0:
    print('a positive number')
```

**Another example to demonstrate differences between elif and else**

```python
season = 'fall'
if season == 'spring':
    print('getting warmer')
elif season == 'winter':
    print('cold out')
elif season == 'summer':
    print('hot out')
elif season == 'fall':
    print('getting colder')
```

If we use else for the last condition, any mistake in the input will default to that instead..

```python
season = 'Winter'
if season == 'spring':
    print('getting warmer')
elif season == 'winter':
    print('cold out')
elif season == 'summer':
    print('hot out')
else:
    print('getting colder')
```


#### Multiple `if` statements

Show that all sequential if statements are evaluated
```python
a = 2
b = 30
if a > 10:
    print('a greater than 10')
if b > 10:
    print('b greater than 10')
```




### Conditional statements with user input

Show how to use the `input()` function

```python
name=input('What is your name? ')
print(f'Hi, {name}.')
```

Show that it can be used with a conditional statement (Mitch Hedberg joke example)

```python
# ask the user if they want to hear a joke
answer = input("Do you want to hear a joke? (press y / n) ")

# code responds accordingly
if answer == "y":
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedberg (RIP)
elif answer == "n":
    print("Fine.")
else:
    print("I don't understand.")
```

## 4. Assertions
 
* Explain that with we can also use `assert()` with a logical statement to get our code to stop and throw an error if a certain condition isn't met
* Show that the Mitch Hedberg joke can be rerun using `assert()`

```python

# ask the user if they want to hear a joke
answer = input("Do you want to hear a joke? (press y / n) ")

# make sure the answer is 'y'. if not, throw an error
assert(answer == 'y')

print("I'm against picketing, but I don't know how to show it.")

```


# Overview of what we learned today

* Logical operators -- how to compare variables in python and assess if conditions are true or not
* The difference between a single and a double equals sign in python
* How to use logic with the 4 primitive data types
* Compound logic using `and`, `or`, and `not`
* How to use the conditional statements `if`, `else`, and `elif`
* How to get user input, and to use this with conditional statements
* How to use `assert()` to thrown an error depending on a conditional statement


All of these things are VERY powerful tools, especially once we combine them with new data types -- coming soon!
