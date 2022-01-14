# Bootcamp Class 10 - Nested Loops

<img src="https://143530-415148-raikfcquaxqncofqfm.stackpathdns.com/wp-content/uploads/2016/12/loops-in-java.jpg" width="500">

# Before class

* Make sure you feel comfortable working with [lists](https://www.programiz.com/python-programming/list)
* Make sure you're comfortable with logic in python -- review the [logic lesson](https://github.com/Justice-Through-Code/fall_2020/blob/master/lessons/06_bootcamp_logic/06_bootcamp_logic.md) if you'd like to refresh!
* Make sure you're comfortable working with [loops](https://github.com/Justice-Through-Code/fall_2020/blob/master/lessons/09_bootcamp_loops/09_bootcamp_loops.md) in python

# Outline of class agenda

Today we'll learn about [**loops**](https://www.w3schools.com/python/python_for_loops.asp) in python. By the end of the lesson, you'll:

1. Feel comfortable using **for loops** with **logical statements** inside of them
2. Feel comfortable using **while loops** with **logical statements** inside of them
3. Feel comfortable exiting a loop using the `break` command
4. Feel comfortable putting **loops inside loops** with **nesting**


# What is nesting?

* Nesting in loops/logic python is when we have loops or logic **inside** existing loops and logic
* Python helps us visualize nesting with **indents**


### Example of nested logic

Here, we 'nest' `if` and `else` statements within the first `if` statement


```python
a = 0
if a > 1:
    print('above 1')
    if a > 2:
        print('above 2!')
    else:
        print('not above 2')
```

### Example of non-nested logic

This example is **not** nested because the second `if` statement and the `else` statement are not indented within the first `if` statement


```python
a = 0
if a > 1:
    print('above 1')
if a > 2:
    print('above 2!')
else:
    print('not above 2')
```

# 1. For loops with logic inside

It can be really useful to make loops that have nested logical statements inside of them.
* This allows us to 'go through' a bunch of items and apply operations to only certain ones


### Days of the week example
For example, let's loop through days of the week and print out a message about whether it is the weekend or not:

```python
# make a list of days
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']

# loop through each day
for day in days:
    # if the string 'day' starts with the character 's', then we know that it is a weekend
    if day.startswith('s'):
        print(f'{day} is on the weekend')
    else:
        print(f'{day} is a weekday')
```

So when we run this we get:

```console
monday is a weekday
tuesday is a weekday
wednesday is a weekday
thursday is a weekday
friday is a weekday
saturday is on the weekend
sunday is on the weekend
```

Python has looped through each day, and **then run the `if/else` statements for each one in sequence** to determine whether to print out that the day is a weekday or a weekend

### Numeric example: checking if numbers are even or odd


Here, we use the `%` operator, which is called 'modulo'. What this does is division, then returns the remainder. For example, `3 % 2` is 1, and `4 % 2` is 0. 


```python
# a list of integers
my_numbers = [1,222, 73, 4, -8, -19]

# for each number, check if it is odd or even
for num in my_numbers:
    # if the remainder after dividing by 2 is 0, it is even
    if num % 2 == 0:
        print(str(num) + ' is even!')
    else:
        print(str(num) + ' is odd!')
```

This returns:

```console
1 is odd!
222 is even!
73 is odd!
4 is even!
-8 is even!
-19 is odd!
```

# 2. While loops with logic inside

While loops can have logic inside them too! For example, we could design a while loop that prompts a user to type either `y` for yes and `n` for no, and keeps prompting until it gets that response:

```python
answered = False
while answered == False:
    response = input('Would you like to change your account password? (type y/n) ')
    if response == 'y':
        print('Great! Taking you to a new window to change your password now...')
        answered = True
    elif response == 'n':
        print('Okay! Keeping your password the same for now')
        answered = True
```

Okay! This one is a little tricky, but essentially, we first set the variable `answered` to `False`, and we keep going until this is true. Then, we keep prompting the user for a response until they type either `y` or `n`, then set `answered=True` to exit the loop.

So we could get something like this:
```console
$ python nested_loop_practice.py
Would you like to change your account password? (type y/n) don't know
Would you like to change your account password? (type y/n) y
Great! Taking you to a new window to change your password now...
```

# 3. Exiting a loop with `break`

The statement `break` in python is really useful. It tells python to **exit the current loop immediately**

For example, back to days of the week -- this time let's `break` after we get to a day that starts with 'w'

```python
# make a list of days
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']

# loop through each day
for day in days:
    print(day)
    # if the string 'day' starts with the character 'w', then stop
    if day.startswith('w'):
        break
```

So, when we run this it stops at wednesday:

```console
monday
tuesday
wednesday
```

# 4. Nested loops: loops inside loops

Alright, now the part you've really been waiting for! We're going to make **nested loops**, or loops insie loops!

Let's start with the days of the week again. This time, we'll loop through each day of the week. For each day, we'll loop though each **letter** in the string for that day and print them out:

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']

# loop through each day (outer loop)
for day in days:
    # loop through letters in each day (inner loop)
    for letter in day:
        print(letter)
```

So this gives us each letter of each day on a separate line:
```console
m
o
n
d
a
y
t
u
e
s
d
a
y
w
e
d
n
e
s
d
a
y
t
h
u
r
s
d
a
y
f
r
i
d
a
y
s
a
t
u
r
d
a
y
s
u
n
d
a
y
```

### Outer & inner loops

When we have nested loops, we call the first loop (the one least indented) the **outer** loop, and the indented loops **inner** loops. This is because **each inner loop finishes before the next outer loop starts**


Let's check this out:

```python
# outer variable loops through range(3)
for outer_var in range(3):
    # inner variable loops through range(3)
    for inner_var in range(3):
        # print values of both variables
        print(f'outer is {outer_var}, inner is {inner_var}')
```

So here, we've created both `outer_var` and `inner_var` as `range(3)`, so each will have indices 0,1,and 2. Let's watch and see how the values change as we go through the nested looping:

```console
outer is 0, inner is 0
outer is 0, inner is 1
outer is 0, inner is 2
outer is 1, inner is 0
outer is 1, inner is 1
outer is 1, inner is 2
outer is 2, inner is 0
outer is 2, inner is 1
outer is 2, inner is 2
```

So, we can see that the **inner loop iterates within each iteration of the outer loop**. In other words, the entire inner loop happens for each iteration of the outer loop.

### Indentation is your guide!

With nested loops and logic, the indentation syntax in python really starts to be very useful to help us read how the nesting is working! We can see that when code is indented after a logical statement or a loop, it is `nested` within this piece of control flow over your code.

If you do make a mistake with indentation, python will tell you! For example:

```python
for i in range(3):
print(i)
```

Here, we've forgotton that the second line (`print(i)`) needs to be indented. So when we run, we get:


```console
  File "nested_loop_practice.py", line 2
    print(i)
        ^
IndentationError: expected an indented block
```

This `IndentationError` points to the line that should have been indented, and tells us it expected an indent. Pretty helpful!

### A third layer of nesting

Just for fun...this doesn't have to stop at 1 inner loop! Let's see what happens if we have 3 layers. So here, we cal our looping variables `i`, `j`, and `k`, and each has a range of 2. 

```python
for i in range(2):
    for j in range(2):
        for k in range(2):
            # print out a list with the values of each variable
            print([i, j, k])
```

So this gives us:
```
[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
```

* The element in the first position is `i` 
* The element in the second position is `j` 
* The element in the third position is `k` 

# Overview of what we learned today

We learned about **nested loops** today! This included

* Putting logical statements in for loops
* Putting logical statements in while loops
* Using the `break` command to stop a loop
* Nesting loops within other loops

Nice! This might seem very counterintutive, but we'll get to practice a lot so you'll feel comfortable with this.
