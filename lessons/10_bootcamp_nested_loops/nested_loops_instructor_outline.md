## 1: Review loops
    * What is 'inside' versus 'outside' of the loop

## 2: Introduce nesting (visual diagrams)
    * Explain that this means putting more things inside a loop -- like logic, or another loop
    * More nesting = more indents
    * Each indent is a 'level'

## 3: Nested Logic first

```python
a = 0
if a > 1:
    print('above 1')
    if a > 2:
        print('above 2!')
    else:
        print('not above 2')
```

## 4: For loop with logic

* Make a for loop through a list of integers that prints out whether each is negative or positive
* Demonstrate `break()` that you can have the loop pause when it hits a negative number


## 5. While loops with logic (if time)

Example with numbers

```python
positive = True
while positive == True:
        resp = input('type a number!')
        if int(resp) >= 0:
                positive = True
        elif int(resp) < 0:
                positive = False
```


## 6. Nested loops

Now show a nested for loop, looping through days and mealls

```python
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday']

meals = ['breakfast', 'lunch', 'dinner']

for day in days:
    for meal in meals:
        print(f'{day}, {meal}')
```

Show what happens if we switch inner/outer:


```python
for meal in meals:
    for day in days:
        print(f'{day}, {meal}')
```

Show what happens if we make an indentation error:

```python
for meal in meals:
for day in days:
        print(f'{day}, {meal}')
```


## 7. Outer & inner loops (if needed)

Another example with outer & inner loops with `range()`

```python
# outer variable loops through range(3)
for outer_var in range(3):
    # inner variable loops through range(3)
    for inner_var in range(3):
        # print values of both variables
        print(f'outer is {outer_var}, inner is {inner_var}')
```

## 8. Show 'Extreme Nesting' to demonstrate that that we can keep nesting, but it gets confusing!

```python
for i in range(2):
    for j in range(2):
        for k in range(2):
            # print out a list with the values of each variable
            print([i, j, k])
```