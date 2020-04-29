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

my_keywords = ['forced', 'study', 'pandemics']

fp = open('comments.out', "w", encoding="utf-8")

i = 0

for comment in reddit.subreddit('askreddit').stream.comments():
     cbody = comment.body
     # print(cbody)
     print(i)
     i += 1
     if any(keyword in cbody for keyword in my_keywords):
         fp.write(cbody)
         fp.write("\n")
         fp.write(comment.permalink)
         fp.write("\n---\n")
