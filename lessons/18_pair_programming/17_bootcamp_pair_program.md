# Bootcamp class 16 - Pair Programming

<img src="https://images.ctfassets.net/k428n7s2pxlu/1aJnbCcUvAa4qiIg4kMeI/9c93dd78ff2c7c5ffbff3e14f5878a87/6-reasons-for-pair-programming.jpg" width="400">

# What is pair programming?

[Pair programming](https://www.codementor.io/pair-programming) is coding technique where two programmers work together at one computer.
* One person writes the code 
* The other person reviews the code as it is typed and make suggestions
* The two people switch roles whenever they want



# Why pair program?

* Programming 'out loud' means that all people involved must communicate and have a good understanding of the code
* Programmers can learn from each other! Everyone knows different tools
* Programmers can help correct mistakes (2 pairs of eyes better than 1)

# Pair Programming Demo

Two of the instructors will now do a demo of some pair programming for setting up some functions for making a script to make a 'twitter account'. 

### `twitter_functions.py`

This script defines some functions for working with a 'twitter' account:

```python
# function to initialize a twitter account
def create_account():
    username = input('Please enter username: ')
    password = input('Please enter password: ')
    account = {'username': username, 'password': password, 'tweets': []}
    return(account)

# function to 'post' a tweet
def post_tweet(account, tweet):
    account['tweets'].append(tweet)
    print(f'{account["username"]} posted a new tweet, "{tweet}"')

# function to count tweets
def count_tweets(account):
    return(len(account['tweets']))

# function to diplay a twitter profile
def display_profile(account):
    print(f'Account Name: @{account["username"]}')
    for tweet in account['tweets']:
        print(tweet)
```

### `demo_twitter.py`

This script tests out the functions defined in `twitter_functions.py` to work with a demo 'twitter' account

```python
# import twitter_functions
from twitter_functions import *

# create twitter account called my_twitter
my_twitter = create_account()

# post three tweets to this account
post_tweet(my_twitter, 'hi internet, how is it going?')
post_tweet(my_twitter, 'welcome to my twitter feed')
post_tweet(my_twitter, 'this is my third post')

# count the number of tweets posted
number_of_tweets = count_tweets(my_twitter)
print(number_of_tweets)

# display the user profile
display_profile(my_twitter)
```
And then finally run:
```
python demo_twitter.py
```
