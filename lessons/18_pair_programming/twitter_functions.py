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
