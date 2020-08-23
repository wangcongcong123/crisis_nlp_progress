#### Guide to use TweepyCalls

This implements core functions that can be used to call the Twitter API using Python-based tool - [Tweepy](https://www.tweepy.org/). The functions include:

##### Before that, always remember to put Twitter Keys in the `keys.py` file and enter the command `pip install -r requirements.txt` to install required dependencies.

** Go to [Twitter Developer Site](https://developer.twitter.com/en) to apply if you have not got these in hand.
```
TWITTER_APP_KEY="<YOURS>"
TWITTER_APP_SECRET="<YOURS>"
TWITTER_KEY="<YOURS>"
TWITTER_SECRET="<YOURS>"
```

#### 1. Get posts by ids
```python
from tweepy_calls import *
tweets_success, tweets_fail=acquire_from_twitter_api(["1248552109240283136"]) # here one tweet id is used for example
print(tweets_success)
```

#### 2. Search tweets by keywords

```python
from tweepy_calls import *
results=search_tweets(query="Beirut AND explosion",max_tweets=1000)
write2file(results,path=os.path.join("searched_tweets","beirut2020.json"))
```
** The searched results will be written to `searched_tweets/beirut2020.json`


#### 3. Get replies of a tweet

```python
from tweepy_calls import *
replies=get_replies(tweet_id="1244719763147968514", user_name="@WangcongcongCC")
print(len(replies))
```
** This will get all replies to [this tweet](https://twitter.com/WangcongcongCC/status/1244719763147968514) that is posted by the user [@WangcongcongCC](https://twitter.com/WangcongcongCC)


#### 4. Online listening
```python
from tweepy_calls import *

stream_listener = OnlineListener(config={"write_path":os.path.join("streammed_tweets","beirut_explosion_en.json")})
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["Beirut","explosion"]) # filter by keywords
stream.filter(languages=["en"]) # filter by language
stream.sample(languages=["en"]) 
```
** The streams will be written to `streammed_tweets/beirut_explosion_en.json`

#### 5. Other functions

```python
print(len(get_followers(screen_name="WangcongcongCC"))) # get the users who follows @WangcongcongCC 
print(len(get_following(screen_name="WangcongcongCC"))) # get the users who @WangcongcongCC follows 
print(len(get_user_timeline(screen_name="WangcongcongCC"))) # get the timeline of @WangcongcongCC 

# get the information of user @WangcongcongCC and @ThoughtsNlp
users = api.lookup_users(screen_names=["WangcongcongCC","ThoughtsNlp"])
for user in users:
    print(user)
```