# Bootcamp Class 11 - Nested Data

*(nesting with lists and dictionaries)*

<img src="https://i1.faceprep.in/Companies-1/python-nested-dictionaries.png" width="500">

^^An example of dictionary with dictionaries nested inside

# Before class

* Make sure you feel comfortable working with both [lists](https://www.programiz.com/python-programming/list) and [dictionaries](https://www.programiz.com/python-programming/dictionary#:~:text=Python%20dictionary%20is%20an%20unordered,when%20the%20key%20is%20known.) in python

# Outline of class agenda

Today we'll learn about [**nested data**](https://holypython.com/intermediate-python-lessons/lesson-6-nested-data-in-python/) in python. By the end of the lesson, you'll be able to:

1. Work with lists inside dictionaries
2. Work with [dictionaries inside dictionaries](https://www.geeksforgeeks.org/python-nested-dictionary/)
3. Work with dictionaries inside lists
4. Work with lists inside lists


## Nesting, revisited...

Last time we talked about nesting with loops and logic -- now we'll be dealing with situations where the **data** are nested! We'll be going through examples of this with both lists and dictionaries. 


# 1. Lists inside dictionaries

You've actually seen this one before in the [restaurants challenge](https://github.com/Justice-Through-Code/fall_2020/blob/master/challenges/08_bootcamp_dictionaries/restaurants_challenge_solutions.py), although we didn't talk about it too much! 

Lists can be stored as **values** inside dictionaries, and referenced using **keys** just as with ever piece of data in a dictionary. 

For example, we could have a shopping cart with lists for different categories of foods:

```python
cart = {'fruits': ['mangos', 'apples', 'oranges'],
        'vegetables': ['spinach', 'peas'],
        'grains': ['rice'],
        'other': ['olive oil', 'black pepper'],
        'total': 24.76}
```

So in this example, every value in this dictionary is a list, except for `total`, which is a float. Lists that are *inside* the dictionary are still formatted as lists.

## Accessing lists within dictionaries

If we want to pull out a list item within the dictionary, we reference it by the **key** the same way we'd do it for an item that was a primitive data type. For example:

```python
veggies = cart['vegetables']
print(veggies)
print(type(veggies))
```

So if we pull the value for `veggies`, save it to a variable, then print and inspect the type, we can see that it is a list:

```console
['spinach', 'peas']
<class 'list'>
```

### Adding to the list

Let's say we want to add another vegetable to our cart here. We can do the following:

```python
cart['vegetables'].append('bell pepper')
print(cart)
```

So, we add 'bell pepper' to the `vegetables` value list in our cart using `append()`, then print out the whole cart.

```console
{'fruits': ['mangos', 'apples', 'oranges'], 'vegetables': ['spinach', 'peas', 'bell pepper'], 'grains': ['rice'], 'other': ['olive oil', 'black pepper'], 'total': 24.76}
```

So we can see that 'bell pepper' has been added to the `vegetables` list in our grocery cart


### Specific list indices from a list nested in a dictionary

Great! But what if we wanted just a *specific* element from this list inside the dictionary? We could add further bracket indexing to do this!

So, if we wanted to get the first item in `fruits` inside our cart

```python
print(cart['fruits'][0])
```
This gives us: 
```console
mangos
```

This second set of hard brackets might be confusing, but let's break it down:
* `cart['fruits']` is a list
* Since `cart['fruits']` is a list, we can then do  `cart['fruits'][0]` to get the first element of said list

We can also update the item in the same way by **reassigning** this variable -- we put this on the left and save in the item we want

```python
cart['fruits'][0] = 'papayas'
print(cart['fruits'])
```

Now we can see that `mango` has been replaced by `papayas`

```console
['papayas', 'apples', 'oranges']
```

## Looping through lists inside dictionaries

We can also design a loop to iterate through a list that is nested within a dictionary. In general, this loop works the same way any loop would to iterate through the list, only the list this case is a value inside a dictionary!

So, let's loop through and print out the vegetables in the shopping cart:

```python
for food in cart['vegetables']:
    print(food)
```

Remembering that `cart['vegetables']` is itself a list, we loop through to print each vegetable:

```console
spinach
peas
bell pepper
```

# 2. Dictionaries inside dictionaries

When we nest dictionaries inside other dictionaries, **the dictionaries on the inside are values**, referenced by keys just like other key-value pairs. Let's see an example of some restaurants as a nested dictionary:

```python
restaurants = {'El Basurero': {'address': '32-17 Steinway St, Queens, NY 11103',
                              'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'},
              'SriPraPhai': {'address': '64-13 39th Ave, Woodside, NY 11377',
                             'menu_url': 'https://sripraphai.com/menu.html'}
}
```

So, we have an outer-level dictionary here called `restaurants`, which has dictionaries for individual restaurants inside of it. The **keys referrring to each restaurant dictionary are the names of that restaurant**. Each restaurant name key refers to a dictionary with the address and link to the menu of that restaurant. 

So, if we wanted to add one more restaurant to this dictionary of restaurants, we could do something like this:

```python
restaurants['Joes Pizza'] = {'address': '7 Carmine St, New York, NY 10014',
                             'phone': '212-366-1182'}
print(restaurants)
```

Notice, the key-value pairs in this dictionary can be different from the inside dictionaries for other restaurants here. For 'Joes Pizza', we have `phone`, but no `menu_url` like with the other restaurants. If we print our `restaurants`, we can see that this has been added:

```console
{'El Basurero': {'address': '32-17 Steinway St, Queens, NY 11103', 'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'}, 'SriPraPhai': {'address': '64-13 39th Ave, Woodside, NY 11377', 'menu_url': 'https://sripraphai.com/menu.html'}, 'Joes Pizza': {'address': '7 Carmine St, New York, NY 10014', 'phone': '212-366-1182'}}
```

### Adding key-value pairs to an inner dictionary

Let's say now we do have the menu link for 'Joes Pizza'! We can add that by adding a new key-value pair **specifically to this inner dictionary**

```python
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com'
print(restaurants['Joes Pizza'])
```

Why 2 sets of hard brackets here? 
* The first set tells us we want to get just specific restaurant 'Joes Pizza' from the dictionary of several restaurants
* The second set tells us we want to create a new key-value pair (since there is no existing `menu_url` pair for Joes Pizza) called `menu_url`

So when we print the inner dictionary for 'Joes Pizza', we get the output:

```console
{'address': '7 Carmine St, New York, NY 10014', 'phone': '212-366-1182', 'menu_url': 'http://www.joespizzanyc.com'}
```

### Updating / removing inner dictionary key-value pairs

By now you might have guessed that changing / removing inner key-value pairs works in basically the same way as any other dictionary -- only we have to be careful to make sure we're referencing the correct dictionary. 

So here, let's update the menu url for 'Joes Pizza' to make it a little bit more specific. Let's also remove the `phone` key-value pair for this restaurant. 

```python
# update the menu_url
restaurants['Joes Pizza']['menu_url'] = 'http://www.joespizzanyc.com/menu.php'

# remove phone number
restaurants['Joes Pizza'].pop('phone')

print(restaurants)
```

We get:
```console
{'El Basurero': {'address': '32-17 Steinway St, Queens, NY 11103', 'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'}, 'SriPraPhai': {'address': '64-13 39th Ave, Woodside, NY 11377', 'menu_url': 'https://sripraphai.com/menu.html'}, 'Joes Pizza': {'address': '7 Carmine St, New York, NY 10014', 'menu_url': 'http://www.joespizzanyc.com/menu.php'}}
```

* Updating the menu url is almost identical to adding it in the first place (this is because `restaurants['Joes Pizza']['menu_url']` already exists now)
* We can remove dictionary items with `pop()`, so we remove `phone` from the inner `Joes Pizzz` dictionary here.


# 3. Dictionaries inside lists

Okay! We've seen how to nest things inside of dictionaries, so now we'll see how to nest data in lists. First up, we can put multiple dictionaries in a list. Here, each dictionary is an item in a list. At the most basic level, here is a list made of empty dictionaries.

```python
a = [{}, {}, {}]
print(a)
```

This gives us:
```console
[{}, {}, {}]
```

Okay, maybe not the most helpful, but you can see that it is perfectly acceptable to put dictionaries as list items. Let's see this in action when we make a list of dictionaries containing user accounts for a website:

```python
users = [{'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'},
         {'username': 'aryn', 'password': 'ilovedictionaries'},
         {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'},
         {'username': 'paul', 'password': 'ilovegit'}]

print(users)
```

So, we've created a list that contains 4 dictionaries, one for each user!
* Notice, not every dictionary has the same keys. Some have `last_login` and some don't, that's okay!
* The dictionaries, like other data types, are separated by commas within the list

So when we print out `users`, we see:

```console
[{'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'}, {'username': 'aryn', 'password': 'ilovedictionaries'}, {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'}, {'username': 'paul', 'password': 'ilovegit'}]
```

### Acccesing items in dictionaries inside a list


#### Getting a whole dictionary
If we want to pull out a dictionary from a list of dictionaries, we would use **numeric indexing** to get the list item of the correct index. For example:

```python
# to print out the dictionary where `username` is 'yusuf'
print(users[2])
```

This gives us:
```console
{'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'}
```

This is because the third item in `users` was a dictionary -- that's why we see all this information.

#### Adding another dictionary to the list

We can add more dictionaries to this list using the `append()` command -- we can put the whole dictionary inside the append command

```python
users.append({'username': 'aeshna', 'password': 'ilovesublimetxt'})
```

Now we have:
```console
[{'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'}, {'username': 'aryn', 'password': 'ilovedictionaries'}, {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'}, {'username': 'paul', 'password': 'ilovegit'}, {'username': 'aeshna', 'password': 'ilovesublimetxt'}]
```

#### Accessing key-value pairs from a dictionary inside a list

If we want a specific key-value pair from a dictionary inside a list, however, we can **reference the key inside that dictionary**:

So, if we want the `'username'` associated with the second item in `users`, we can do:

```python
print(users[2]['username'])
```

This gives us:

```console
yusuf
```

We can also add, update, and remove these key-value pairs from the dictionary within the list:

```python
#add a new key-value pair
users[2]['verified_account'] = True

# update a key-value pair
users[2]['password'] = 'iloveprogramming'


# remove a key-value pair
users[2].pop('last_login')

# print users[2] to check the changes
print(users[2])
```

As before, the only difference between adding vs. updating a key-value pair is whether anything existed with that same key before we assign it. We can use the `.pop()` method again to remove a key-value pair (by referencing the key) from the dictionary. 

```console
{'username': 'yusuf', 'password': 'iloveprogramming', 'verified_account': True}
```

### Looping through a list of dictionaries

This part is pretty cool. This is a BIG advantage for putting items in a list -- they are in order now, unlike a dictionary, so we can loop through them. Because we have a list full of users, we can **loop** through each user:

For example, we can print each user out one by one (this is printing each dictionary in the list out one by one):

```python
for user in users:
    print(user)
```

So, we get each dictionary on a separate line, because the variable `user` here stands for one of the dictionaries on each iteration of the loop:

```console
{'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'}
{'username': 'aryn', 'password': 'ilovedictionaries'}
{'username': 'yusuf', 'password': 'iloveprogramming', 'verified_account': True}
{'username': 'paul', 'password': 'ilovegit'}
{'username': 'aeshna', 'password': 'ilovesublimetxt'}
```

#### Accessing data within each dictionary in a loop

Even more than this, we can loop through the dictionaries and access a **specific key-value pair** from each one, as long as each dictionary has data for the corresponding key. So, let's say we wanted to loop through our `users` list and pull out *just the usernames*:

```python
for user in users:
    print(user['username'])
```

So here in the loop, `user['username']` indicates that we want the **value** stored at the **key** `username` for **each dictionary** as we iterate through them. This prints out:

```console
ash
aryn
yusuf
paul
aeshna
```

In fact, if we wanted to do something like turn all the usernames to uppercase, we could do this:

```python
for user in users:
    user['username'] = user['username'].upper()
    print(user)
```

So we're reassigning each username to be uppercase

```console
{'username': 'ASH', 'password': 'ilovepython', 'last_login': '9/28/2020'}
{'username': 'ARYN', 'password': 'ilovedictionaries'}
{'username': 'YUSUF', 'password': 'iloveprogramming', 'verified_account': True}
{'username': 'PAUL', 'password': 'ilovegit'}
{'username': 'AESHNA', 'password': 'ilovesublimetxt'}
```

#### If not all dictionaries have the same keys

Let's way we were trying to access the `last_login` of each user. It turns out only the first user (ASH) has this information now, so let's see what happens if we try to print this out for everyone:


```python
for user in users:
    print(user['last_login'])
```

We get:

```console
9/28/2020
Traceback (most recent call last):
  File "temp.py", line 93, in <module>
    print(user['last_login'])
KeyError: 'last_login'
```

This gives an error, because after the first dictionary, there is no key `last_login` in the following dictionaries.

# 4. Lists inside lists

Last for today, but not least, we can put lists as items inside other lists. Let's redo our shopping cart using this data structure:

```python
shopping_list = [['mangos', 'apples', 'oranges'], ['carrots', 'broccoli', 'lettuce'], ['corn flakes', 'oatmeal']]
```

So, we have hard brackets within hard brackets to indicate that each list is inside another list. 


### Accessing inner lists & sublists

To access the items inside this nested list, the **first set of brackets** indicate the index for the outer list, and the **second set of brackets** are for the inner ones.

For example:

```python
print(shopping_list[0][1])
```

This gives us the 2nd item of the 1st list:

```console
apples
```

As we've seen before, we can add new items, reassign, or remove items from the sublists:

```python
# add an item to the first inside list
shopping_list[0].append('grapes')

# add an item to the last inside list
shopping_list[-1].append('eggs')

# update an item in the 2nd inside list
shopping_list[1][0] = 'baby carrots'

# remove an item from the 2nd inside list
shopping_list[1].remove('broccoli')

print(shopping_list)
```

So, after these changes, we have:

```console
[['mangos', 'apples', 'oranges', 'grapes'], ['baby carrots', 'lettuce'], ['corn flakes', 'oatmeal', 'eggs']]
```

### Nested loops with nested lists

Since we can loop through any list, we can set up **nested loops** to iterate through *each item in each inner list*


```python
for food_group in shopping_list:
    for food in food_group:
        print(f'I plan to buy some {food}')
```

So, in the outer loop we loop through lists, and the `food_group` variable stands for one of the inner lists each iteration. Then, in the inner list, the `food` variable stands for each item (strings) in `food_group`. This gets repeated for each value of `food_group`.

```console
I plan to buy some mangos
I plan to buy some apples
I plan to buy some oranges
I plan to buy some grapes
I plan to buy some baby carrots
I plan to buy some lettuce
I plan to buy some corn flakes
I plan to buy some oatmeal
I plan to buy some eggs
```

#### Adding a counter

Great! So we can see all of the foods across all the nested lists. Now, maybe we want to add a counter to see how many different items we are buying total, or to number our items. Here's one way to do this:

```python
counter = 1
for food_group in shopping_list:
    for food in food_group:
        print(f'Item #{counter}: {food}')
        # this line means to add 1 to the counter variable
        counter+=1
```

We've used a nice operation here, the `+=` symbol. What this does is adds 1 here to counter.
* `+1` with any number would add that number to the varible at hand


So as a result we get: 
```
Item #1: mangos
Item #2: apples
Item #3: oranges
Item #4: grapes
Item #5: baby carrots
Item #6: lettuce
Item #7: corn flakes
Item #8: oatmeal
Item #9: eggs
```


#### Looping through nested lists + logic

We can add logical statements in here too. Let's say we only want to add the foods to our list if they contain the letter 'o'.

```python
counter = 1
for food_group in shopping_list:
    for food in food_group:
        # Only print and advance the counter if food contains an o
        if 'o' in food:
            print(f'Item #{counter}: {food}')
            # this line means to add 1 to the counter variable
            counter+=1
```

We use the `if 'o' in food:` piece to test whether the character `o` is in the string `food`. So, we get:

```console
Item #1: mangos
Item #2: oranges
Item #3: baby carrots
Item #4: corn flakes
Item #5: oatmeal
```

Great! Just the foods with the letter 'o'.

### Why stop here? Nesting to the *extreme*

Technically we could nest things with as many levels as we want. Just as an example, here is some extreme nesting

```python
nest_a_lot = [[[1,2,3], ['a', 'b', 'c']], [[TRUE, FALSE, TRUE], [{'name':'paul'}, 2.7, 'apples']]]

# loop through the 3 levels of nested lists and print out each individual item!
for i in nest_a_lot:
    for j in i:
        for k in j:
            print(k)
```

So, here we go throuth three levels of nested lists (plus one of the lists has dictionaries in it!) and print out the items:

```console
1
2
3
a
b
c
True
False
{'name': 'aedan'}
{'name': 'yusuf'}
```

Wow! So we can go quite far with nesting....it does get tricky to stay organized the more nesting there is though. 
              

# Overview of what we learned today

Wow! We've gone over some very complex data structures with nested data today. Lots of stuff, but this will allow for a ton of useful applications moving forward. We're really putting pieces together now -- we will be taking plenty of time to review this stuff, and apply it in many settings.

We learned about:
* Dictionaries with nested lists inside
* Dictionaries with nested dictionaries inside
* Lists with nested dictionaries inside
* Lists with nested lists inside

Great! We will be getting tons of practice with these, then soon adding [functions](https://www.w3schools.com/python/python_functions.asp) into the mix. 
