# Learning PRAW

Inspired by [this post](https://www.reddit.com/r/redditdev/comments/cvisv8/how_do_i_get_the_markdown_source_of_a_post/) on getting the Markdown source of a comment (because I wanted to publish an article that quoted a reddit comment), I decided to learn some PRAW. Maybe I can make a useful reddit bot.

## TODO

### Latest

- [ ] Extract posts using [pushshift.io](https://pushshift.io/) according to [this post](https://stackoverflow.com/questions/53988619/praw-6-get-all-submission-of-a-subreddit).

### History

So according to that comment I linked above, the best way to get the markdown from a post is this:

```python
submission.selftext
```

OR

```python
comment.body
```

Let's see how I can fit this into my script.

- [x] extract comments from submissions

Looks like I'll need to use [pushshift.io](https://pushshift.io/) to extract posts from a certain time period, according to [this StackOverflow answer](https://stackoverflow.com/questions/53988619/praw-6-get-all-submission-of-a-subreddit).

- [ ] Extract posts using [pushshift.io](https://pushshift.io/) according to [this post](https://stackoverflow.com/questions/53988619/praw-6-get-all-submission-of-a-subreddit).

## Useful links

- [PRAW Documentation](https://praw.readthedocs.io/en/latest/)
- [Comment Extraction and Parsing](https://praw.readthedocs.io/en/latest/tutorials/comments.html)
- [Pushshift GitHub with helpful README](https://github.com/pushshift/api)
- [Medium article about using Pushshift](https://medium.com/@RareLoot/using-pushshifts-api-to-extract-reddit-submissions-fb517b286563)
