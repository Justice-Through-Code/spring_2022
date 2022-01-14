## 1 Visual Diagram of Dictionaries
* Why? if we want to look things up by **name**
* Introduce **keys** versus **values**
* Show dictionary syntax, map onto 'real-world' dictionary
* Labeled, but not ordered



## 2. Set up blank dictionary, talk about `{}`

```python
blank_dict = {}
print(blank_dict)
print(type(blank_dict))
```


## 3. Make some key-value pairs


String example

```python
user_account = {'username':'pbloom'}
```

Float example

```python
user_account = {'username':'pbloom', 'balance':270.26}
```

## 4.  Printing the contents of a dictionary

```python
user_account = {'username':'pbloom', 
                'balance':270.26}
print(user_account)
```

## 5. Retrieving data from a dictionary using `[]`

Explain that dictionaries use `{}`, but we can reference data with `dict[<key>]`

```python
user_account = {'username':'pbloom', 
                'balance':270.26}
my_money = user_account['balance']
print(my_money)
```


## 6. Dictionaries can have lists as values

So far we've seen strings and floats in a dictionary, but the *values* can be almost any kind of data. To demonstrate this, let's add some extra information to `user_account`. 

```python
user_account = {'username':'pbloom', 
                'balance':270.26,
                'deposits':[100.00, 21.34, 2.31, 8.06],
                'withdrawals':[-2.31, -21.43, -78.00],
                'email_notifications': True}
print(user_account)
```

## 7. Adding items to a dictionary

```python
user_account = {'username':'pbloom', 
                'balance':270.26}

# add a new value of '9/15/2020' using the key 'last_transaction'
user_account['last_transaction_date'] = '9/15/2020'
```

## 8. Updating dictionary items

* Show how to update a regular dictionary item first
* Make sure to demonstrate how to update a LIST inside a dictionary here

```python
user_account = {'username':'pbloom', 
                'balance':270.26,
                'withdrawals':[-2.31, -21.43, -78.00]}

# update the balance
user_account['balance'] = -500.00

print(user_account)
```

## 9. Removing items from a dictionary with `.pop()`

```python
user_account = {'username':'pbloom', 
                'balance':270.26}

# we remove 'balance'
user_account.pop('balance')

print(user_account)
```

## 10. Why would you use a list versus a dictionary?

* Do you want your data ordered, or labeled? Why?
* We'll talk more once we discuss **loops** about this