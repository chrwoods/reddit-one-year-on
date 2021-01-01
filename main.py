import praw
import time
import config

MESSAGE = '''/u/%s

Two years ago you posted what you wanted to achieve in 2019, and today I'm messaging you to see how you did over both 2019 and 2020!

Your goal was:

> %s'''

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

old_post = reddit.submission(id='a9yzx0')
old_post.comment_sort = 'new'
old_post.comments.replace_more(limit=None)

new_post = reddit.submission(id='ko3jg5')

comments = old_post.comments

count = 0
for comment in comments:
    if comment.author is None:
        continue
    
    print(str(count) + ': ' + comment.author.name)
    indented_body = comment.body.replace('\n', '\n> ')

    new_comment = MESSAGE % (comment.author.name, indented_body)
    new_post.reply(new_comment)
    # print(new_comment)
    
    count += 1
    time.sleep(0.2)
