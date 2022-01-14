# Spotipy Challenges
#
# In this challenge, we'll access data from the Spotipy API to compare popularities for various artists

# Note: if you would like to play around more with the Spotify API, go fill out this form to sign up for a Spotify Developer account, https://developer.spotify.com/dashboard/, if you don't have a Spotify account, you can sign up for one here as well (it's free!). Once signed up, it will take you to a dashboard, and you can click 'Create A Client ID', to register a new 'project' (we are not actually making a new project, this is just what language Spotify uses so that you can generate multiple API keys). And then copy the client ID and client secret for your new project to use whenever! But this may not be necessary to complete the challenge.

# Before you get started: Installing and loading spotipy library
#
# For this challenge, we'll need to install a python library called 'spotipy', then load it, as well as the json library

# To get started with the spotipy API, we need to first install it, in your terminal, run this command:
# pip install spotipy --upgrade


print("Question 1")
# 1 Import the spotipy API to be able to use it in this challenge


# We'll need this to print the resulting data nicely
import json

# To access authorised Spotify data, do not edit these next few lines, they are just needed to make our function calls actually work
from spotipy.oauth2 import SpotifyClientCredentials

# Do not edit these unless you have your own Spotify Developer account
CLIENT_ID = '99b361927f674edfb28a342956235d47'
CLIENT_SECRET = '3657ba71ed0d480fb415e96b4cbef89c'

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# spotify object to access API
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# The results for the function calls we will be making are a little bit hard to parse, so formatting a string from the Python JSON object might help here. Here, we've provided a function called `jprint()` that you can call on the output of your search to try to look at the search result as a formatted string
# you do not have to edit this function at all!!!
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# IMPORTANT NOTE: FOR THIS CHALLENGE, EVERY FUNCTION YOU CALL WILL HAVE TO START WITH sp (i.e. sp.search() and whatever else), BECAUSE THAT IS THE NAME OF THE SPOTIPY OBJECT WE CREATED! WITHOUT THE sp, YOUR FUNCTION CALLS WILL NOT WORK!!!

print("Question 2")
# 2 Search for an artist!
#
# Using the spotipy documentation (https://spotipy.readthedocs.io/en/2.16.1/), figure out how to access the spotify search function to search for an artist with only their name, for example 'Beyonce'. (Hint: the query is the name)

# lets go get an artist! Does the spotipy function need any special parameters?

name = "Beyonce"  # chosen artist
# result =   # fill this in


# this is how we will print out our results of spotipy queries. What format is this output?
# jprint(result) # uncomment if you want to see the results


print("Question 3")
# Figure out how to choose the top artist from the search, and get that artist's id
#
# Each artist in spotify has a unique ID. The challenge is here that the we've basically done the equivalent of typing 'Beyonce' into the spotify search bar. However, for further use in looking up artist info we need the **id** for the artist -- there is a unique id for each artist that is a long string.
#
# So, we want to find the first artist returned by that search and get the id for that artist
#
# **Hint**: The result of the search is a nested data structure. How can you explore the nested *layers* of this structure to pull out the right information?

# this returns the first element of the list of 'items'
# each 'item' is a ditionary for an artist returned from the search
# we take item 0 here -- this is 'Beyonce'
# items after 0 are similar searches, but not Beyonce herself

#print(result['artists']['items'][0]['name']) # uncomment if you want to see the results
#print(result['artists']['items'][1]['name']) # uncomment if you want to see the results
#print(result['artists']['items'][2]['name']) # uncomment if you want to see the results


# lets get the artist id, so that we can look up more stuff for them
# each artist has a unique ID like this


#artist_id =   # fill this in
#print(artist_id) # uncomment if you want to see the results


print("Question 4")
# How popular is Beyoncé? Using her unique artist ID, now let's pull popularity and followers
#
# So now, since we have the artist ID for Beyonce, lets get the popularity and followers. Spotify has a 'popularity' metric for artists that goes from a minimum of 0 to a maximum of 100
#
# Again, the artist info is a **nested** data structure, so you'll need to figure out how to go through the nested objects to find the popularity and followers
#
# Figure out how to print how many followers Beyonce has and how popular she is in a variable called artist_info
#
# Hint: there is a function from spotipy that allows you look up an artist spcifically given the artist ID that may help https://spotipy.readthedocs.io/en/2.16.1/



# artist_info =   # fill this in
# jprint(artist_info) # uncomment if you want to see the results


# How do you to access key-value pairs for popularity?


# Followers is a dictionarity itself, with the value 'total' being the total followers. How can we access it?


print("Question 5")
# Pick 5 artists, and construct a pandas dataframe where each row represents a different artist. Include columns for artist name, id, popularity, and followers

# note: try to use artists that don't have special characters in their name (like no accent marks or whatever), that will make it harder to type in

# One way to do this:
#   - set up an empty list to hold your dictionaries for each artist
#   - loop through artist names and
#       - search that artist using sp.search(), then get artist id
#       - use sp.artist() to get artist info
#       - put artist name, id, popularity, and followers into a dictionary for that artist
#       - append that dictionary as a new item in the list


# define a list of 5 chosen artists
chosen_artists = []
popularities = []


print("Question 6")
# Get the most and least popular artists
#
# You can accomplish this by looking at your array and indexing the array to print the name of the artist matching the rows with highest & lowest popularity and follower counts


print(popularities)


print("Bonus!")
# Bonus! Get the most similar artists to the last artist in your popularities dataframe, do the popularities match up?
#
# Note, there is a function using the spotify api to get the 'related artists' given an artist id! Can you figure out how to use it?


#sim =   # fill this in
# jprint(sim['artists'][:3]) # uncomment this like to see what the top 3 similar artists are



# Print the artist name and popularity

