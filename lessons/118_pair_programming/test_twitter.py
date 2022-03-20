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
