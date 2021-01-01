import praw
import config

checkin_msg = '''%s

Two years ago you posted what you wanted to achieve in 2019, and today I'm messaging you to see how you did over the past 24 months!

Your goal was:

> %s'''

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

post = reddit.submission(id="a9yzx0")
print(post.title)

post.comments.replace_more(limit=0)
comments = list(post.comments)

count = 0
for comment in comments:
    if comment.author is None:
        continue
    print(comment.author.name)
    print(comment.body)
    count += 1
    if count > 10:
        break
