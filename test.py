import praw
import config

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

test_post = reddit.submission(id='agi5zf')
test_post.reply('test (UA)')
