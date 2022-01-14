## What is a function?

* Block of code that runs only when called
* Reduces need for copy-pasting code

Whiteboard to explain `input -> function -> output` using simple functions like `sum()`.

## 1. Built-in functions
  
 * Examples of built-in functions we have been using so far:
  
```python
print('This only shows up in console')

type('the type is a string')

float(54)

int('34.4')

str({})

range(100)
```

  * `func()` vs `object.func()`
    * If the function has a period before it, it's a method. For e.g. `text.upper()` is a string method.
    * We'll talk more about methods in a future class

## 2. Function syntax

```python
def say_hello():
    print('Hello World')

say_hello()
```

* Explain function definition and calling a function
* We can have function calls inside other python code (if statements, for loops, etc.)

## 3. Parameters

* We want our functions to be generalizable
* Example: separate functions for `say_hello_ash` and `say_hello_paul`
    * Use a parameter instead!

```python
def say_hello(name):
    print(f'Hello {name}')
    print('Good Morning')
    print('And Good Night')

say_hello('Ash')
say_hello('Paul')
```

* A parameter is ike a variable, contains reference to a value
* We can have multiple parameters
* Explain what an argument is - argument vs parameter
* Explain how default arguments work
* We can use `key = value` syntax so that the order of arguments doesn't matter
 
 ## 4. Return
 
```python
 def multiply(a, b):
    return a*b
```
 
 * We can break out of the function or return a value with `return`
 * `print` vs `return` - fundamentally different in their applications!
    
```python
num = multiply(2, 3)
num = multiply(multiply(2, 3), 4)
print(num)
```



