import praw
import config

reddit = praw.Reddit(client_id=config.CLIENT_ID,
                     client_secret=config.CLIENT_SECRET,
                     user_agent=config.USER_AGENT,
                     username=config.USERNAME,
                     password=config.PASSWORD)

resolutions_post = reddit.submission(id="a9yzx0")
print(resolutions_post.title)

resolution_comments = list(resolutions_post.comments)
print(len(resolution_comments))
print(resolution_comments[0].body)
