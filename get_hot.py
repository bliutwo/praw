import praw
import get_smmry_of_article
import datetime
import calendar
from smmryapi import SmmryAPI

def get_hot(subreddit_name: str):
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

    # use subreddit.in as input if None argument given
    if (subreddit_name == None):
        fp = open('subreddit.in', 'r')
        subreddit_name = fp.readline().rstrip()
        fp.close()

    # open api key
    fp = open('api_key.in', 'r')
    api_key = fp.readline().rstrip()
    fp.close()

    # datetime object containing current date and time
    now = datetime.datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%B %d, %Y, %H:%M")
    # day of the week
    my_date = datetime.date.today()
    day_of_week = calendar.day_name[my_date.weekday()]
    dt_string = day_of_week + ", " + dt_string
    print(dt_string)

    year = datetime.date.today().year

    # construct filename
    output_filename = subreddit_name
    output_filename += "_highlights/"
    output_filename += now.strftime("%Y-%m-%d-")
    output_filename += day_of_week[0:3]
    output_filename += "-"
    output_filename += dt_string[-5:-3]
    output_filename += dt_string[-2:]
    output_filename += ".md"

    # open output file
    fp = open(output_filename, "w", encoding='utf-8')

    # add title and description
    title = "# Today's Highlights from /r/"
    title += subreddit_name
    title += "\n\n"
    description = "Date and time of publication of these highlights: **"
    description += dt_string
    description += "**."
    description += "\n\n"

    # add motivation link

    # add SMMRY API credit

    # add PRAW API credit

    # write title and description to file
    fp.write(title)
    fp.write(description)

    submissions = reddit.subreddit(subreddit_name).hot(limit=8)

    # initialize SMMRY API
    smmry = SmmryAPI(api_key)

    for submission in submissions:
        title = submission.title
        if "Daily Discussion" not in title and "Looking For Participants" not in title and "Join our Official Discord" not in title and "For US Patients Diagnosed" not in title and "Clinical study in Austin, TX" not in title and "Join our official Coronavirus" not in title and "Personal Thread" not in title and "Discussion Thread" not in title:
            submission.comment_sort = "top"
            top_level_comments = list(submission.comments)
            top_comment = None
            top_comment_author = None
            if top_level_comments and top_level_comments[0].author:
                top_comment = top_level_comments[0].body
                top_comment = top_comment.replace('\n', '\n> ').replace('\r', '')
                top_comment_author = top_level_comments[0].author.name
            if top_comment and "As a reminder, this subreddit" in top_comment:
                top_comment = top_level_comments[1].body
                top_comment = top_comment.replace('\n', '\n> ').replace('\r', '')
                top_comment_author = top_level_comments[1].author.name
            output_string = ""
            output_string += "## "
            output_string += title
            output_string += "\n\n"
            url = submission.url
            output_string += "Summary of [original article]("
            output_string += url
            output_string += "):\n\n"
            summary = get_smmry_of_article.get_summary(url, api_key, smmry)
            if "ERROR:" in summary:
                summary = "Sorry, we were unable to get the summary of this article."
            output_string += "> "
            output_string += summary
            output_string += "\n\n"
            if top_comment and top_comment_author:
                username = "`/u/"
                username += top_comment_author
                username += "`"
                output_string += username
                output_string += " "
            output_string += "[comments]("
            reddit_url = "https://www.reddit.com" + submission.permalink
            output_string += reddit_url
            output_string += ")"
            if top_comment:
                output_string += ":\n\n"
                output_string += "> "
                output_string += top_comment
            output_string += "\n\n"
            output_string += "[Why am I seeing this on Google Docs?](https://docs.google.com/document/d/1Dc6We63vOXIZsc0op-Bt4abqkYjXzOigalQqFxmvvbM/edit?usp=sharing)\n\n"
            fp.write(output_string)

    fp.close()

def main():
    get_hot(None)

if __name__ == "__main__":
    main()
