# Bootcamp Class 8 - Loops

<img src="https://dq-blog-files.s3.amazonaws.com/list-tutorial/py1m2_loops.gif" width="500">

# Before class

* Make sure you feel comfortable working with both [lists](https://www.programiz.com/python-programming/list) and [dictionaries](https://www.programiz.com/python-programming/dictionary#:~:text=Python%20dictionary%20is%20an%20unordered,when%20the%20key%20is%20known.) in python
* Make sure you're comfortable with logic in python -- review the [logic lesson](https://github.com/Justice-Through-Code/fall_2020/blob/master/lessons/06_bootcamp_logic/06_bootcamp_logic.md) if you'd like to refresh!

# Outline of class agenda

Today we'll learn about [**loops**](https://www.w3schools.com/python/python_for_loops.asp) in python. By the end of the lesson, you'll:

1. Feel comfortable using **for loops** to *iterate* through items in a list
2. Feel comfortable using **for loops** to *iterate* through characters in a string
3. Feel comfortable using the `range()` function with for loops to iterate across many items
4. Understand how a **while loop** is different from a **for loop** and how to create one

**Let's make a script in `loop_practice.py` for the lesson today.**


# What is a loop?

You can kind of think of a loop as an 'apply all'. We use **loops** in python to iterate over sequential items (like lists, or even strings).
* **Iterate** means that we go through each item, one-by-one, and do something each time
* Loops can be as simple as printing out each item in a list, or contain very complex logic and operations
* Loops allow us to perform **many** operations **in few lines of code**

# 1. Looping through a list

Almost every **for loop** starts with the syntax: `for x in y:`
* Where y is the object you are *iterating across*
    * "for (each) person in (the list of) people"
    * "for (each) stock in (the list of) stocks"
    * "for (each) random_thing in (the list of) random_things"
* What x is called **actually doesn't matter** -- it stands for each element in y as you go through the loop
* This statement **always** ends with a colon, and the next line will indent

So, let's see an example where we loop through a list of integers and print each one:

```python
# make a list of integers
numbers = [12, 8, 41]

# loop through and print them
for number in numbers:
    print(number)
```

This gives us the following printout. Notice that each number is printed on a line of its own:

```console
$ python loop_practice.py
12
8
41
```

So, what is actually happening here?
* Each iteration of the loop, `number` takes on the value of each item in `numbers` in order
* So, the first time, `number` is equal to `12`, so `print(number)` prints 12 on its own line
* The second time, `number` is equal to `8`, so `print(number)` prints 8 on its own line
* The third time, `number` is equal to `41`, so `print(number)` prints 41 on its own line
* Then, we're at the end of `numbers`, so we're done!

### The name of the iterator variable doesn't matter

Here, we used a variable called `number` to iterate through a list of numbers, but what this variable is called actually doesn't matter -- we just have to be consistent with how we use it. In fact, we can change this variable to be called whatever we want, and we'll get the same output.

```python
# make a list of integers
numbers = [12, 8, 41]

# loop through and print them
for spaghetti in numbers:
    print(spaghetti)
```

Even though we changed the iterator variable here to `spaghetti`, which has nothing to do with our list of integers, this still works fine.

### Any indented code happens inside the loop

Because the loop keeps going until it gets to the end of whatever it is iterating over (in this case, the list), any code inside the loop is repeated each time. For example, if we add more print statements:

```python
# make a list of integers
numbers = [12, 8, 41]

# loop through and print them
for spaghetti in numbers:
    print(spaghetti)
    # print hello world each time we go through the loop
    print('hello world')
# print hi computer just once at the end
print('hi, computer!')
```

Here's the output we get

```console
12
hello world
8
hello world
41
hello world
hi, computer!
```

Because `print('hello world')` is **indented**, it runs **each time** in the loop. However, because  `print('hi, computer!')` is not, it is **outside the loop**, and just runs once after the loop is finished.

### Loops can contain lots of different operations

So far, our loops have just printed things out, but we can put any python code inside a loop really! For example, we could take a list of strings, loop through and convert each string to upper case, then add these upper case strings to a new list:

```python
# list of lower case strings
lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']
# a blank list for upper case strings
upper_list = []

# loop through lower_list, convert each element to upper, and append to upper_list
for i in lower_list:
    # remmember that the append() function adds to the end of a list
    upper_list.append(i.upper())

# print out upper_list
print(upper_list)
```
So, when we run this code we get
```console
['HERE', 'ARE', 'MY', 'LOWER', 'CASE', 'WORDS']
```

# 2. Looping through characters in a string

So far, we've used loops only with lists. But, we can use them in a really similar way to loop through the individual characters in a string! Let's try it out:

```python
my_string = 'ice cream'
for letter in my_string:
    print(letter)
```
It's a bit annoying to look at the output of this one, but we get each letter printed out on its own line (even the spaces)

```console
i
c
e

c
r
e
a
m
```

We could use this to check if each letter is a vowel by combining this loop with a logical `if() `statement. For each character, we ask whether it is `in()` the list of vowels:

```python
my_string = 'ice cream'
# define the vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# loop throug each letter in the string and decide if a vowel or not
for letter in my_string:
    # this logical statement checks whether the letter is equal to ANY of the elements in vowels and returns TRUE if so
    if letter in vowels:
        print(f'{letter} is a vowel')
    else:
        print(f'{letter} is not a vowel')
```

So we get:
```console
i is a vowel
c is not a vowel
e is a vowel
  is not a vowel
c is not a vowel
r is not a vowel
e is a vowel
a is a vowel
m is not a vowel
```

Looks correct! We also get python telling us that a blank space is not a vowel, because the blank space is treated like a character, like any other!

# 3. Loops with the `range()` function

What if someone asked you to square all the numbers from 0 to 1000?
* There's *no way* you would actually want to write down all of those numbers
* The `range()` function can help us accomplish this

`range(n)` is a [useful function](https://www.w3schools.com/python/ref_func_range.asp) that, by default, gives us all the integers from 0 to n (but not including n). We can use this in a loop to iterate through these integers.

```python
for i in range(8):
    print(i)
```

This gives us:

```console
0
1
2
3
4
5
6
7
```

Notice, like with indices, this starts at 0 and does NOT include 8.

However, where `range()` can come in most useful is in looping through lists using their **indices**. For example, if we combine `range()` with `len()` to get the length of a list `range(len(my_list))` will always give all the indices of the list for iterating through.

```python
lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']
for i in range(len(lower_list)):
    print(i)
```

This prints out:

```console
0
1
2
3
4
5
```

The **key** thing here is that here, **i stands for the indices of `lower_list`, not the actual elements**. We are iterating through the elemtns of the list, but unlike earlier, i is just an integer that stands for each index in the list in turn.

If we want to, we can still access each **element of the list** this way by using bracket indexing.

```python
lower_list = ['here', 'are', 'my', 'lower', 'case', 'words']
for i in range(len(lower_list)):
    # use an f-string to show what the index and list element is
    print(f'the index is {i} and the element is: {lower_list[i]}')
```

So, now we see both the index and the list element itself on the same line:

```console
the index is 0 and the element is: here
the index is 1 and the element is: are
the index is 2 and the element is: my
the index is 3 and the element is: lower
the index is 4 and the element is: case
the index is 5 and the element is: words
```

Differentiating the **index from the list element** can be tricky in loops especially, but we'll practice this a lot!

# 4. For loops vs. while loops

We've mostly talked about **for loops** today, but there is one other kind of loop in python that is really important to know about, the **while loop**.

Basically, **a while loop keeps repeating until a certain logical condition is met**. Unlike for loops, which run a set number of times, while loops could run an undefined amount of times while waiting for a condition to be met.


<img src="https://media.geeksforgeeks.org/wp-content/uploads/20191101170515/while-loop.jpg" width="500">


For example, we could have a while loop like this:

```python
count = 0
while (count < 5):
   print(count)
   count = count + 1

print('done')
```

So, we keep counting up , printint out `count`, then increasing `count` by one until it becomes 5. Then we stop, then print done:

```console
0
1
2
3
4
done
```

One thing to be wary about with while loops is that if we set them up incorrectly, they could just go on forever! Then we'd have to just shut down the script from running. For example (DON'T RUN THIS):

```python
count = 0
while (count >= 0):
   print(count)
   count = count + 1

print('done')
```

This would go on looping forever if we let it, because `count` will always be great than or equal to 0. It will never print `'done'`

### Why use a while loop versus for loop?

We'll get to this question more later on, but we can think of some circumstances where we would want a computer program to keep running until recieving a certain input:
* Asking a user for a password until it is entered correctly
* Any situation where we don't know exactly how many times we want code to run, we just know we want it to run until we get a certain signal
* Code that is 'optimizing' a certain problem and needs to run until a satisfactory solution has been reached

# Overview of what we learned today

We learned about **loops** today! This included


1. Using loops to iterate across lists and strings
2. Using loops with different operations inside of them
3. Using loops with the `range()` function
4. Using while vs. for loops

Loops are a **super important** programming concept, so we will be using them a lot the rest of the course. We're already starting to see here how useful they can be in solving a variety of problems, but more on this to come.
