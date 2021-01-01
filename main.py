import praw
import config

message = '''/u/%s

Two years ago you posted what you wanted to achieve in 2019, and today I'm messaging you to see how you did over the past 24 months!

Your goal was:

> %s'''

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

post = reddit.submission(id="a9yzx0")
# post.comment_sort = 'new'

print(post.title)

post.comments.replace_more(limit=None)
comments = post.comments

print(len(comments))
count = 0
for comment in comments:
    if comment.author is None:
        continue
    if comment.author.name != 'ChrisMan174':
        continue
    
    print(comment.author.name)
    print(comment.body)
    indented_body = comment.body.replace('\n', '\n> ')

    print(message % (comment.author.name, indented_body))
    
    count += 1
    if count > 10:
        break
