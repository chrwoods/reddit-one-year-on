import praw
import time
import config

MESSAGE = '''/u/%s

A year or so ago you posted what you wanted to achieve in 2023, and today I'm pinging you to see how you did!

Your goal was:

> %s'''

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

old_post = reddit.submission(id='100ddut')
old_post.comment_sort = 'new'
old_post.comments.replace_more(limit=None)

new_post = reddit.submission(id='18vqmal')

comments = old_post.comments

for count, comment in enumerate(comments):
    if comment.author is None or comment.removed:
        continue
    
    print(str(count) + ': ' + comment.author.name)
    indented_body = comment.body.replace('\n', '\n> ')

    new_comment = MESSAGE % (comment.author.name, indented_body)
    new_post.reply(new_comment)
    # print(new_comment)
    
    time.sleep(0.2)
