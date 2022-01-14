## 1. Introduce concept of lists in python
* Visual diagram -- 'grocery list' metaphor
* Multiple pieces of data
* Clarify concept of elements (items) vs indexes (positions)
    * Maybe even hint that indexing starts at 0 in python

<img src="https://railsware.com/blog/wp-content/uploads/2018/10/positive-indexes.png" width="800">


## 2. Making lists in python
* Make a grocery list in python
* Explain the hard brackets
* Show what happens when you print it

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)
```



## 3. Lists can have many different data types in them:

Show lists with different basic data types
```python
int_list = [1,-4,7]
float_list = [12.4,-199.22, 4.0, 84.3]
boolean_list = [True, False, False, True, True, True, False]
print(int_list)
print(float_list)
print(boolean_list)
```

## 4. Lists with variables inside them

Show a list with variables as elements

```python
var_a = 'apple'
var_b = 'pear'
var_c = 'milk'
groceries = [var_a, var_b, var_c]
print(groceries)
```

## 5. Making an empty list

Show how to start an empty list, and use `type()` to show it is still a list

```python
my_list = []
print(my_list)
print(type(my_list))
```


## 6. Show how to add items to a list with the `.append()` method

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)

# add another item
groceries.append('peanut butter')
print(groceries)
```

## 7. Show how to remove items a list with the `.remove()` method


```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries)

# remove the eggs
groceries.remove('eggs')
print(groceries)
```

Also show what happens when you try to remove an item by name that doesn't exist

## 8. Using `len()` to get the list length

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# print out the list length
print(len(groceries))
```

## 9. Introduce list indexing in python

Might help to refer back to pictures for this part!

Show how to pull data by the numeric index:

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[0])
print(groceries[2])
```

(optional) show that when you pull data from a list, the elements will be of their own type (not lists themselves)
```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(type(groceries[0]))
```

Show that you can also index from the end with negative numbers

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']
print(groceries[-1])
print(groceries[-2])
```



## 10. Out of range errors

* Show what happens when you try to use an index equal to the length of the list. Why doesn't this work?
* Explain out of range errors

## 11. (if there is time) multiple consecutive items

* Show that the colon can be used to pull items from a range of consecutive indices
* up to, but NOT including the index after the colon


```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# slice to get items 1-2 but NOT 3
my_items = groceries[1:3]
print(my_items)
```


## 12. Splitting strings into lists

* Demonstrate the `.split()` string method
* Show what happens when you split with different types of separators

```python
my_string = 'row, row, row, your boat, gently down the stream'
# split the string by commas
my_list = my_string.split(',')
print(my_list)
```


## 13. Joining list elements into a string

Show how to 'put the strin back together again' with `.join()`, and a few examples of how to join

```python
groceries = ['apples', 'eggs', 'pasta', 'carrots']

# join the list with no space in between
my_string1 = ''.join(groceries)
print(my_string1)

# join the list with 1 comma in between
my_string3 = ','.join(groceries)
print(my_string3)
```


