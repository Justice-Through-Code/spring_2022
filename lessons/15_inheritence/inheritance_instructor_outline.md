# 1. Refresh students on OOP
* Classes
* In particular, we're learning how *to create our own custom classes*

# 2. What is inheritance?

* Introduce concepts of **parent class** and **child class** 
* Children "inherit" attributes and methods from parents, but can have their own unique features
    * Parent class `Vehicle` with children `Car` and `Motorcycle`


# 3. Making a parent & child class

* A parent class isn't anything special, any class can *become* a parent class if it is used for child classes

## Instruments as an example

* Parent class `Instrument` with children `Guitar` and `Drums`


First make the `Instrument` parent class
```python
class Instrument():
    def __init__(self, volume):
        self.volume = volume

    def display_info(self):
        print(f'Instrument set to volume {self.volume}')
```


Now, make the `Guitar` child class, even with no additional attributes. Explain how `Guitar` "inherits" from `Instrument`


```python
class Guitar(Instrument):
  pass
```

# 4. Show students that the parent/child can be used identically so far:

```python
instrument1 = Instrument('11')
instrument2 = Guitar('11')
instrument1.display_info()
instrument2.display_info()
```

We get the same output

```console
Instrument set to volume 11
Instrument set to volume 11
```

# 5. Adding the `__init__()` function to the child class

* Explain that if the child class has its own `__init__()` function, it will no longer *inherit* the parent's version of this. 
* Explain that to be able to have **new attributes**, a child class must have a new init function

## Add an `__init__()` function for the `Guitar` class

* Here, we add a new attribute `electric` for the child `Guitar` class
* Emphasize that we still need to create the `volume` attribute in this case (or demonstrate that the `Guitar` class will not have `volume` if we don't include it here)

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        self.volume = volume
        self.electric = electric
```

* Show students that only a `Guitar` has the `electric` attribute, but not `Instrument` more generally
* Emphasize that parent/child classes can have different attributes, may need to be instantiated differently

```python
instrument1 = Instrument(volume = '11')
instrument2 = Guitar(volume = '11', electric = False)
print(instrument2.electric)
print(instrument1.electric)
```

Output

```console
False
Traceback (most recent call last):
  File "inheritance_demo.py", line 30, in <module>
    print(instrument1.electric)
AttributeError: 'Instrument' object has no attribute 'electric'
```

## 6. Inheriting the `__init__()` function from the parent class

* Explain that the drawback to the previous example is that we had to repeat things again already created in the parent class. 
* If we *inherit* the `__init__()` function, that gives a better place to work from

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        Instrument.__init__(self, volume)
        self.electric = electric
```

## 7. Generalized inheritance using the `super()`

* Show students that for any child class, we can inherit using the `super()` function to implicitly inherit the parent class' attributes and methods without naming it again

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric
```


## 8. Adding methods specific to a child class

* We add a new `tune()` method for the `Guitar` child class, but note that it does not apply to the `Instrument` class more broadly
* Note that the method name is *not the same* as any method in the parent class

```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric

    def tune(self):
        print('Guitar is in tune now!')
```

## 9. Overriding a method from the parent class

* Explain that we can make a *different version* of the same method in the child class by "overriding" the method from the parent class
* Here, we override the `display_info()` method to display guitar-specific information


```python
class Guitar(Instrument):
    def __init__(self, volume, electric):
        super().__init__(volume)
        self.electric = electric

    def display_info(self):
        print(f'Guitar set to volume {self.volume}')
        if self.electric:
            print('Guitar is electric!')
        else:
            print('Guitar is acoustic!')
```

Instantiate them

```python
instrument1 = Instrument(volume = '11')
instrument2 = Guitar(volume ='11', electric=True)

instrument1.display_info()
instrument2.display_info()
```

We get different outputs for the `display_info()` method for the `Instrument` vs. `Guitar`

```console
Instrument set to volume 11
Guitar set to volume 11
Guitar is electric!
```

# 10. Multiple children with the same parent

* Explain parent can have multiple child classes
* Make a new class `Drums` that also inherits `Instrument`

```python
class Drums(Instrument):
    def __init__(self, volume):
        super().__init__(volume)

    def play(self):
        print('boom boom bap!')
```

Neither `Guitar` nor `Instrument` have the `play()` method yet


# Multiple inheritance

* Demonstrate that one class can inherit from *multiple* other parent classes
* `Guitar` inherits from `Instrument` and `Luggage`

```python
class Luggage():
    item_type = 'luggage'
    def __init__(self, weight):
        self.weight = weight

class Guitar(Instrument, Luggage):
    def __init__(self, volume, electric, weight):
        Instrument.__init__(self, volume)
        Luggage.__init__(self, weight)
        self.electric = electric

    def display_info(self):
        print(f'Guitar set to volume {self.volume}')
        if self.electric:
            print('Guitar is electric!')
        else:
            print('Guitar is acoustic!')
            
g = Guitar(volume = 11, electric = False, weight = 20)

print(g.electric, g.volume, g.weight, g.item_type)
```

## Why is this relevant?
* Inheritance is a key part of a lot of software, particularly when the software needs custom data structures to keep track of info
* We are later going to use inheritance when working with ["Class-based views in Django"](https://docs.djangoproject.com/en/3.2/topics/class-based-views/)
