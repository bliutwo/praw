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

# print(reddit.user.me())
# print(reddit.read_only)
reddit.read_only = True
# print(reddit.read_only)

# submission = reddit.submission(url='https://www.reddit.com/r/Futurology/comments/g2se2i/legislation_proposes_paying_americans_2000_a_month/fnnq6vw/?context=1')

fp = open('comment.in', 'r')
comment_id = fp.readline().rstrip()

comment = reddit.comment(comment_id)
fp = open('comment.out', "w")
fp.write(comment.body)
fp.close()
