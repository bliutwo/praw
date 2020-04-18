# Learning PRAW

Inspired by [this post](https://www.reddit.com/r/redditdev/comments/cvisv8/how_do_i_get_the_markdown_source_of_a_post/) on getting the Markdown source of a comment (because I wanted to publish an article that quoted a reddit comment), I decided to learn some PRAW. Maybe I can make a useful reddit bot.

## TODO

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

## Useful links

- [PRAW Documentation](https://praw.readthedocs.io/en/latest/)
- [Comment Extraction and Parsing](https://praw.readthedocs.io/en/latest/tutorials/comments.html)
