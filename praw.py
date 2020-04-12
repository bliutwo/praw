import praw

fp = open('pass.password', 'r')
client_id = fp.readline()
client_secret = fp.readline()
password = fp.readline()

fp.close()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='test script for /u/bliutwo_bot',)
