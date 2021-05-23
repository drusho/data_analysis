import praw
import pandas as pd

# from config import cid, csec, ua

cid = "t4MWafN7valKRA"
csec = "_nmp3CGP9gSviRzk7r8L0rU2uFLXLA"
ua = "googlenoob"


# create a reddit connection
reddit = praw.Reddit(client_id=cid, client_secret=csec, user_agent=ua)


# single subreddit new 5
subreddit = reddit.subreddit("news").new(limit=5)  # multiple subreddits top 5
subreddit = reddit.subreddit("news" + "datascience").top(limit=5)

subreddit = reddit.subreddit("news").new(limit=1)
for post in subreddit:
    print(vars(post))