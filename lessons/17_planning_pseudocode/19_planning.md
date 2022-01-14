# Pseudocode & Planning

![title](https://memegenerator.net/img/instances/68471051.jpg)

### A game plan for your code

Sooner or later, we're all stumped by complex problems that require some thought and careful planning to solve by coding. We can think of coding as three steps:

- Pseudocoding or a rough plan of the code we will write,
- Writing actual code
- And finally, optimizing or cleaning up the code we wrote.

### What is pseudocode?

It is not a new language. **Pseudocode** is a way of expressing your code in your own words without worrying too much about language syntax. It is tempting to jump into writing code and figuring things out on the way, but pseudocoding helps us:

- Break down a large task into smaller tasks, described in our own words
- Create a blueprint for our code implementation
- Identify steps that might need further research (looking up code solutions on stackoverflow, etc)

Pseudocoding helps us understand the requirements of the program before we spend our efforts in writing complex code.

# Demo 1

Let's take a simple function that calculates the average of numbers in a list

```python
def average(nums):
    pass
```

The keyword `pass` is a placeholder you can use when you have nothing written inside the body of your function. If you run the function as is, nothing happens, which is what we want until we write actual code

### Pseudocoding

```python
def average(nums):
    # sum of nums list
    # divide sum by the number of values in nums list
    # return output
    pass
```

### Writing actual code

```python
def average(nums):
    # sum of nums
    total = sum(nums)
    # divide sum by the number of values in nums list
    average = total/len(nums)
    # return output
    return average
```

# Planning with nested data

Often, nested data structures make planning ahead a little tricky! Today, we'll practice planning ahead to make some nested data structures and functions to work with them

# Demo 1. Planning ahead with a 'shopping cart' -- List vs. Dictionary

I want to make a data structure here that sets up an online shopping cart so that we can keep track of:
* the items in my cart
* the price of each item
* the quantity of each item

## Outlining 

If I were to make an online of the data structure, it might look something like this:


* item1
    * item1 name
    * item1 price
    * item1 quantity
* item2
    * item2 name
    * item2 price
    * item2 quantity    
    

## Outline -- > code

Okay so now that we have the outline we can start to see what the nested data structure would look like. Let's try filling this in with some sample code. We could imagine our cart as either being a *list with nested dictionaries inside* or a *dictionary with nested dictionaries inside*

### List version

```python
cart1 = [{'name':'banana bunch', 'price': 0.80, 'quantity':2},
        {'name':'salmon steak', 'price': 6.89, 'quantity':3}]
```

### Dictionary version

```python
cart2 = {'banana bunch':{'price': 0.80, 'quantity':2},
        'salmon steak':{'price': 6.89, 'quantity':3}}
```

So, with these we store much of the same data, but in slightly different ways. Either way, our planning of how we want the data to be organized beforehand helps us set this up!

# Demo 2. Planning ahead with a shopping cart function

## Getting the total price -- list version

Let's make a function to get the total price of our shopping cart. For the list version, we could write out pseudocode like this

```python
# function takes 1 argument -- a shopping cart
def get_total(cart):
    pass
	# initialize total price to 0

	# loop through the list of items (for each item in the cart)
		# multiply the price of the item by the quantity and add to the total price

	# return the total price
```

Then we can add in the python code to match our pseudocode:

```python
# function takes 1 argument -- a shopping cart
def get_total(cart):
	# initialize total price to 0
	total_price = 0
	# loop through the list of items (for each item in the cart)
	for item in cart:
		# multiply the price of the item by the quantity and add to the total price
		total_price+= item['price']*item['quantity']
	# return the total price
	return total_price

# call the function on our cart
print(get_total(cart1))
```

Great! Now we can get the total price of our shopping cart


```console
22.27
```

## Getting the total price -- dictionary version

Let's say we had set up the dictionary version of our cart though. How could we get the total price there?
* It might be a little more tricky, but it is possible too! Let's plan out this function with pseudocode

```python
# function takes 1 argument -- a shopping cart (dictionary)
def get_total(cart):
	pass
	# initialize total price to 0

	# get the keys of all items in the dictionary

	# convert the keys to a list

	# loop through the list of keys (for each item in the cart)
		# multiply the price of the item by the quantity and add to the total price

	# return the total price
```

This one is a bit longer because we are basically getting all the keys in the dictionary and converting them to a list so we can iterate through the dictionary items. Now we can fill in the python code.

```python
# function takes 1 argument -- a shopping cart (dictionary)
def get_total(cart):
	# initialize total price to 0
	total_price = 0

	# get the keys of all items in the dictionary
	all_items = cart.keys()

	# convert the keys to a list
	item_list = list(all_items)

	# loop through the list of keys (for each item in the cart)
	for item in item_list:
		# multiply the price of the item by the quantity and add to the total price
		total_price+= cart[item]['price']*cart[item]['quantity']

	# return the total price
	return total_price


print(get_total(cart2))
```

We can see that we get the same answer here too

```console
22.27
```

# Overview

Pseudocode and planning are hard! But, taking a step back from the code/syntax to _think about what you want to do and how to do it_ first can help you get a long way, and save a lot of confusion when it comes time to start coding. Especially when we have complex and nested data to deal with!

This type of planning will really help us figure out how to 'put together the pieces' and take on projects that are larger in scope.
