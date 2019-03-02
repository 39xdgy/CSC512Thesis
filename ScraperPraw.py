import praw
import re

reddit = praw.Reddit(client_id = 'nvLZT3XnES_fbQ',
client_secret = 'mvC2mW9qI_YDHsAW_vWXai8gMP0',  username = 'afcornell2021',
    password = 'Fhegix!00', user_agent = 'praw512')

subreddit = reddit.subreddit('DeepFriedMemes')

hot_python = subreddit.hot(limit = 5)

#def delete_emoji(String_input):

# from: https://www.reddit.com/r/learnpython/comments/8br5sz/removing_emojis_from_words_python3/
replace_emoji = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.
        format(submission.title, submission.ups, submission.downs,submission.visited))

        submission.comments.replace_more(limit = 0)

        for comment in submission.comments.list(): #PRAW functionality
            print(20*'-')
            #print('Parent ID:', comment.parent())
            #print('Comment ID:', comment.parent())
            #print(comment.body)
            print(replace_emoji.sub(r'', comment.body))
