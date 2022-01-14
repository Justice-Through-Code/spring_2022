## 1. Show nested loops example to refresh
* Coin flipping!


## 2. What are nested data structures?

Use visual diagrams to help students understand
* A list of dictionaries
* A list of lists
* A dictionary with lists as values
* A dictionary with dictionaries as values

Discuss with students why these nested data structures might be helpful!

## 3. Lists as dictionary values

Shopping cart example

```python
cart = {'fruits': ['mangos', 'apples', 'oranges'],
        'vegetables': ['spinach', 'peas'],
        'grains': ['rice'],
        'other': ['olive oil', 'black pepper'],
        'total': 24.76}
```

* Show how to retrieve one element from one of the lists in the dict
    * `cart['vegetables'][0]`
* Show how to add to one of the lists in the dictionary
    * using `.append()`
* Show how to update one of the elements in one of the lists
* Show how to loop through one of the lists in the dictionary

```python
for food in cart['fruits']:
    print(food)
```


## 4. Dictionaries inside dictionaries

Restaurants example! If you wanted to look up restaurants by name this would be useful

```python
restaurants = {'El Basurero': {'address': '32-17 Steinway St, Queens, NY 11103',
                              'menu_url': 'https://www.allmenus.com/ny/astoria/366154-el-basurero/menu/'},
              'SriPraPhai': {'address': '64-13 39th Ave, Woodside, NY 11377',
                             'menu_url': 'https://sripraphai.com/menu.html'}
}
```

* Show how to add an additional restaurant
* Show how to add a new key-value pair to a nested inner dictionary
    * Add hours to one of the restaurants
* Show how to remove a key-value pair from a nested inner dictionary with `.pop()`
    * `restaurants['SriPraPhai'].pop('menu_url')`


## 5. Dictionaries inside lists

Example could be a list of users, where each user is a dictionary with keys for username, password, last_login

```python
users = [{'username': 'ash', 'password': 'ilovepython', 'last_login': '9/28/2020'},
         {'username': 'aryn', 'password': 'ilovedictionaries'},
         {'username': 'yusuf', 'password': 'ilovejavascript', 'last_login': '9/26/2020'},
         {'username': 'paul', 'password': 'ilovegit'}]
```

* Show how to print out the entire dictionary for one of the users
* Show how to print the password for the 2nd user
    * Talk about the pros and cons of users being numerically indexed in the list here
* Show how to loop through and print out everyone's usernames
    * If time, show how to make everyone's usernames uppercase with `.upper()`

## 6. Lists inside lists

Another shopping list here

```python
shopping_list = [['mangos', 'apples', 'oranges'], ['carrots', 'broccoli', 'lettuce'], ['corn flakes', 'oatmeal']]
```

* Show how to acccess one of the entire inner lists
* Show how to access 1 element of one of the inner lists
    * `print(shopping_list[0][1])`

## 7. Nested loops with nested lists

Show how a nested loop can be written to loop through each of the inner lists

```python
for food_group in shopping_list:
    for food in food_group:
        print(f'I plan to buy some {food}')
```
