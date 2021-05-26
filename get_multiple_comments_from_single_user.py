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

fp = open('username.in', 'r')
username = fp.readline().rstrip()
fp.close()

with open('comments.out', "w", encoding="utf-8") as f:
    for id in reddit.redditor(username).comments.new(limit=None):
        comment = reddit.comment(id)
        f.write(comment.body)
        f.write("\n\n")
        f.write(comment.permalink)
        f.write("\n----\n")
