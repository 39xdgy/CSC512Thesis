import praw

reddit = praw.Reddit(client_id = 'nvLZT3XnES_fbQ',
client_secret = 'mvC2mW9qI_YDHsAW_vWXai8gMP0',  username = 'afcornell2021',
    password = 'Fhegix!00', useragent = 'praw512')

subreddit = Reddit.subreddit('popular')

hot_python = subreddit.hot(limit = 5)

for submission in hot_python:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited: {}'.
        format(submission.title, submission.ups, submission.downs,submission.visited))

        submission.comments.replace_more(limit = 0)

        for comment in submission.comments.list(): #PRAW functionality
            print(20*'-')
            print('Parent ID:', comment.parent())
            print('Comment ID:', comment.parent())
            print(comment.body)
