# Algorithmic Thinking

## Outline

Algorithms are just a sequence of steps that are followed to achieve a particular result. Almost all the code we have been writing has been algorithmic, from looping through a deli menu to calculating tips.

As the problems we try to solve become more complex, we want to develop some tools and ways of thinking that will help you reason about algorithms and potentially make them faster.

In this lesson, we'll cover:

- Time Complexity (Big O Notation)
- Comparing complexities
- Writing optimal code
- Space complexity


## Time Complexity (Big O Notation)

Time complexity describes the amount of computer time it takes to run an algorithm

- We usually estimate this by roughly counting the number of basic operations performed by the algorithm
- An algorithm's running time may vary greatly depending on the input, so we consider the **worst-case time complexity**
- Running time may also change as the input grows larger, we describe this complexity using **Big O Notation**

Some examples of time complexities:
O(1): No matter the size of your collection, the time to perform an operation is constant
O(n): As the size of the input increases, the time increases linearly
O(n^2): The time to perform an operation is proportional to the square of the items in the input 


Let's demonstrate these by doing different manipulations on a list:

### Constant time - O(1)

```python
def print_first_element(my_list):
    print(my_list[0])

print_first_element([1, 2, 3])
print_first_element([1, 2, 3, 4, 5, 6])
```

Accessing an element from a list is always a constant operation no matter how long the list is, so we can describe the time complexity of our algorithm as O(1). Even though the second list is twice as long, we only perform one operation no matter what, hence constant time.


### Linear Time - O(n)

```python
def print_elements_in_list(my_list):
    for item in my_list:
        print(item)

linear_algorithm([1, 2, 3])
linear_algorithm([1, 2, 3, 4, 5, 6])
```

Since we iterate through every element in the list, the second list requires twice as many operations as the first. As the list gets bigger, the number of operations grows linearly with it.


### Quadratic - O(n^2)

```python
def print_pairs(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i], my_list[j])

print_pairs([1, 2])
print_pairs([1, 2, 3])
print_pairs([1, 2, 3, 4])
```

Looking at the algorithm, we see the outer loop iterates through all the elements in the list, and the inner does the same as well. The total number of steps is then n * n, where n is the number of items in the input list.

For the first list, we need 2 * 2 = 4 operations. For the second and third, we need 3 * 3 = 9 and 4 * 4 = 16 operations. Thus, the number of operations required grows quadratically and the list grows, thus O(n^2).


## Comparing complexities

Why is Big O useful? It lets us talk about roughly how long an algorithm will take.

Here's how the various complexities compare:

<img src="https://miro.medium.com/max/2544/1*yiyfZodqXNwMouC0-B0Wlg.png" width="500">

## Writing optimal code

Brute force algorithm - A straightforward method of computing a problem that uses raw computational power rather than trying to improve efficiency

Brute force algorithms might be ok for a first try at a solution, but we want to try and optimize our code whenever possible, since not doing so might result in code that runs orders of magnitude slower.

Let's walk through a problem that has a simple brute force solution, and a much faster optimized solution:

```
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Explanation: Because nums[1] + nums[2] == 6, we return [1, 2].
```

Brute force solution:
```python
def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```
Since we have a nested for loop and check all the possible pairs of the list, the runtime complexity of this algorithm is O(n^2).


Optimized solution:
```python
def two_sum_optimized(nums, target):
    complements = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in complements:
            return [complements[complement], i]
        else:
            complements[nums[i]] = i
            
    return "No solution"
```
In this solution, we iterate through the list only once. For each element, we compute the complement needed to get to the target. If we've seen it before in the list, then we can return the pair, otherwise we note the current element and index in a dictionary. Since we have a single loop and dictionary lookups are constant, the total runtime is O(n).

Comparing the two solutions, while the first is easier to implement, it will run considerably slower than the second when we introduce large inputs.

## Space Complexity

While we want to consider how time complex an algorithm might be, we might also have to consider how much extra space our algorithm uses. We can also use Big O notation to describe how the space an algorithm uses increases as the input grows.

Consider the following problem:
```
Given a string s, determine if it is a palindrome.

Example 1:
Input: s = "tacocat"
Output: true
Explanation: "tacocat" is a palindrome

Example 2:
Input: s = "helloworld"
Output: false
Explanation: "helloworld" is not a palindrome
```

Solution 1:
```python
def valid_palindrome(s):
    reversed_input = s[::-1]
    if s == reversed_input:
        return True
    else:
        return False
```
For this solution, we construct a whole new reversed string in memory and compare it to the original string to see if they match. As the input string gets longer, the amount of space we need to store the reversed string grows linearly with it, so space complexity is O(n).


Solution 2:
```python
def valid_palindrome(s):
    front = 0
        back = len(s) - 1
        
        while front <= back:
            if s[front] != s[back]:
                return False
            else:
                front += 1
                back -= 1
        
        return True
```
Here we have two pointers that start at either end of the string. We work our way inwards and check that each pair of letters match. If they don't, we can return false. In this solution, we only maintain two pointers no matter how large the input is, so the space complexity remains constant no matter the size of the input, thus giving us O(1).
