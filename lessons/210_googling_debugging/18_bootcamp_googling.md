# Bootcamp class 16 - Googling 

<img src="https://images.ctfassets.net/k428n7s2pxlu/1aJnbCcUvAa4qiIg4kMeI/9c93dd78ff2c7c5ffbff3e14f5878a87/6-reasons-for-pair-programming.jpg" width="400">

# Is it okay to google code?

In almost every setting, the answer is **yes**! 
* Most experienced programmers [google a lot](https://codeahoy.com/2016/04/30/do-experienced-programmers-use-google-frequently/) to find code solutions
* The key is making sure that if you search code out online written by someone else, you **document** where you've gotten it from, and **make sure you understand how it works for your own usage**


# How to search for code solutions

As you might have experienced, searching online for solutions for coding is a skill that can be built up. Here are some general principles that will help.

* Be specific! 
    * Searches like 'how to make a website in python' might give you good resources, but they might not solve your specific use case
* But, don't be *too specific* to a situation other users would be unlikely to encounter
    * Searching something like 'make a python function to add a song to my music library module' might not be that helpful, since not a lot of other people will have done exactly this
* Keep it brief, and don't use extra words
    * This might help refine your search to useful entries. For example, 'for loop python' might get you what you need more specifically than 'how to make a for loop using python programming'

Check out [this page](https://knightlab.northwestern.edu/2014/03/13/googling-for-code-solutions-can-be-tricky-heres-how-to-get-started/) for some more tips on effective searches

# Once you find a code solution

The MOST important thing to do if you see a code solution is to **make sure you understand how to use it** if you try to use it for your own code. You can copy a snippet of code from the internet into your script to try it out, but in the long run if you don't understand how it works, you won't be able to work with it effectively in the future.

So, when you look for a code solution on the internet, make sure you can **convince yourself how it works** before moving on

# Demo 1. Formatting numbers to display as money in python

Let's say we're working on a tip calculator function, and we want to make sure the output always prints out as currency (with a dollar sign, two decimal points). What could we google to figure this out?

* Something like 'python display number as money' or python 'display number as currency'
    * Some good answers on [stack overflow](https://stackoverflow.com/search?q=python+list+sort&s=695ba0f2-0d1c-44e4-b8a9-3fa92e7f1105) and [kite](https://www.kite.com/python/answers/how-to-format-a-float-as-currency-in-python#:~:text=format()%20to%20format%20a,format%20the%20float%20as%20currency.) come up
    
```python
def calculate_tip(bill, num_people, tip_percentage=20):
	# calculate the total each person should pay
	amount_per_person = bill/num_people
	tip_per_person = amount_per_person * tip_percentage/100
	total_per_person = amount_per_person + tip_per_person

	# format as currency
	total_per_person = "${:,.2f}".format(total_per_person)

	# display how much each person should pay
	print(f'Each person should pay {total_per_person}')



calculate_tip(10000, 12, 20.22)
```



# Demo 2. Reverse the order of a list in python

Let's say we have a list, and we want to flip it into reverse order.

```python
grocery_list = ['apple', 'banana', 'mango', 'guava']
```


Here we could google something like:
* 'python flip order of list'
* 'python reverse list order'
* 'python list reverse'


And get some useful links like [this one](https://www.programiz.com/python-programming/methods/list/reverse) or [this one from W3schools](https://www.w3schools.com/python/ref_list_reverse.asp) (w3schools is usually really helpful)

So now we can try:

```python
grocery_list.reverse()
print(grocery_list)
```

And we get:
```console
['guava', 'mango', 'banana', 'apple']
```

# Demo 3. Delete a variable in python

Maybe we're making user Twitter accounts and we want to be able to delete an entire account

```python
account = {'username':'@paul_b', 'password':'python3.7'}
```

How can we delete this account?

Maybe we can search:
* 'python delete variable'
* 'python remove variable'
* 'python delete dictionary'

We might come to a few different solutions

## Solution 1: Deleting the entire account variable:

This one erases the entire variable `account` from memory

```python
del account
```

In this case if we run `print(account)` we get:

```console
Traceback (most recent call last):
  File "googling_lesson.py", line 27, in <module>
    print(account)
NameError: name 'account' is not defined
```

Because the variable `account` is completely gone!


## Solution 2: Emptying the dictionary

We might find [a solution](https://www.askpython.com/python/dictionary/delete-a-dictionary-in-python) for clearing out the dictionary to make it empty instead:

```python
account.clear()
```

In this case if we run `print(account)`, we get:

```console
{}
```


# Overview

Searching for code solutions on the internet can be hard, especially if you're stuck on something. However, some web resources are super helpful, and it is often super helpful to spend a little time browsing resources and other people's solutions to your questions. Often, we can learn a lot of new pieces of syntax and possibilities when searching about code! 

As the course goes on, you'll want to build up your online code searching skills. This way, you'll be able to figure out solutions to a wide variety of problems, and more effectively debug your code when you get stuck. 
