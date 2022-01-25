## 1. Why loops?

* What if we want to apply the same operations to many pieces of data (i.e. items in a list)
* Loops are a way to do this!

## 2. Draw loop diagram

* Diagram to walk students through a loop
* Visually show walking though iteration


## 3. Make a for loop with integers

* Emphasize syntax!
* Show that the name of the iterator (looping) variable doesn't matter

```python
# make a list of integers
numbers = [12, 8, 41]

# loop through and print them
for number in numbers:
    print(number)
```


## 4. What is 'in' versus 'out' of the loop?

* Show that any indented code in the loop is run each iteration
* Show how indents matter here again!


## 5. Using `range()` with loops

Show how to loop through numbers 0-n

```python
for i in range(8):
    print(i)
```

What is range?
* Won't include the number you enter as an argument
* But you will get that many elements


## 6. Printing out indices verus items

Printing out the indices:
* First show combining `range()` with `len()`

```python
grocery_list = ['apple', 'banana', 'milk', 'eggs', 'carrots']
for i in range(len(grocery_list)):
    print(i)
```

Now, use the iterator variable to index the list and get the **items**
* Remind people about list indexing here!


```python
grocery_list = ['apple', 'banana', 'milk', 'eggs', 'carrots']
for i in range(len(grocery_list)):
    print(grocery_list[i])
```

Or

```python
grocery_list = ['apple', 'banana', 'milk', 'eggs', 'carrots']
for i in range(len(grocery_list)):
    print(f'the index is {i} and the element is: {grocery_list[i]}')
```

## 7. Show how to print out a list of strings as upper case

```python
grocery_list = ['apple', 'banana', 'milk', 'eggs', 'carrots']
for food in grocery_list:
    print(food.upper())
```

What if we want to make a new list using the upper case versions?
* We can set up a blank list and append in a loop

```python
# make blank list
upper_case_list = []
grocery_list = ['apple', 'banana', 'milk', 'eggs', 'carrots']
for food in grocery_list:
    # append in loop
   upper_case_list.append(food.upper())
```

## For loops vs. while loops

* While loop if you want to do something until a specific thing happens
* For loop if you want a specific number of times

```python
count = 0
while (count < 5):
   print(count)
   count = count + 1

print('done')
```

## Looping through a string

Explain that can loop over individual characters in a string

```python
my_string = 'ice cream'
for letter in my_string:
    print(letter)
```
