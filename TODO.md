# Twitter Bot Reddit Highlights TODO List

- [x] Write script that outputs a single day's publishable markdown.
  - [x] Format the reddit stuff
  - [x] Implement SMMRY to get actual summary using [SMMRY API Wrapper for Python](https://github.com/dsynkov/smmryAPI).

But what to do when I get the following output?

```
λ Py -3 get_hot_day_posts_from_subreddit.py
Tuesday, June 09, 2020, 03:21
Traceback (most recent call last):
  File "get_hot_day_posts_from_subreddit.py", line 94, in <module>
    summary = get_smmry_of_article.get_summary(url, api_key, smmry)
  File "C:\Users\bliut\Dropbox\praw\get_smmry_of_article.py", line 4, in get_summary
    s = smrry.summarize(url,sm_length=3)
  File "C:\Users\bliut\Dropbox\praw\smmryapi.py", line 73, in summarize
    raise SmmryAPIException("%s: %s" % (smmry_dict['sm_api_error'], smmry_dict['sm_api_message']))
smmryapi.SmmryAPIException: 3: THE PAGE IS IN AN UNRECOGNISABLE FORMAT
```

- [x] Modify `get_hot_day_posts_from_subreddit.py` and/or `get_smmry_of_article.py` to handle this exception.

All exceptions are handled now.

- [ ] Write script that commits to repo automatically
  - [ ] Ensure that `get_hot_day_posts_from_subreddit.py` outputs proper `[date].md` filename formatting.
- [ ] Write Twitter bot.
- [ ] Write script `publish_to_twitter.py`.
