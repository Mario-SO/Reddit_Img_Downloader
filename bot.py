import os
import praw
from configuration.yml_reader import data

# Credentials
client_id = data['credentials']['client_id']
secret_key = data['credentials']['secret_key']
user_agent = data['credentials']['user_agent']
username = data['credentials']['username']
password = data['credentials']['password']

# Custom values
sub = data['custom_values']['sub']
img_limit = data['custom_values']['img_limit']
sort_by = data['custom_values']['sort_by']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=secret_key,
                     user_agent=user_agent,
                     username=username,
                     password=password)

subreddit = reddit.subreddit(sub)

if sort_by == "hot":

    try:
        for i in subreddit.hot(limit=img_limit):
            link = i.url
            if "jpg" or "png" in link:
                os.system('wget ' + link)

    except Exception as e:
        print(e)

elif sort_by == "new":
    try:
        for i in subreddit.new(limit=img_limit):
            link = i.url
            if "jpg" or "png" in link:
                os.system('wget ' + link)

    except Exception as e:
        print(e)

else:
    try:
        for i in subreddit.new(limit=img_limit):
            link = i.url
            if "jpg" or "png" in link:
                os.system('wget ' + link)

    except Exception as e:
        print(e)
