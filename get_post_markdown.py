import praw

# Take in a file called "password.pass" and get three strings from it:
# - client_id
# - client_secret
#   (more info here: https://praw.readthedocs.io/en/latest/getting_started/authentication.html#)
# - username (reddit username)
# - password (reddit password)
# - user_agent (<platform>:<app ID>:<version string> (by /u/<reddit username>))
fp = open('password.pass', 'r')
client_id = fp.readline().rstrip()
client_secret = fp.readline().rstrip()
username = fp.readline().rstrip()
password = fp.readline().rstrip()
user_agent = fp.readline().rstrip()
fp.close()

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

reddit.read_only = True

fp = open('post.in', 'r')
post_id = fp.readline().rstrip()

post = reddit.submission(post_id)
fp = open('post.out', "w")
fp.write(post.selftext)
fp.close()
