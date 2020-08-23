import tweepy
from keys import TWITTER_APP_KEY,TWITTER_APP_SECRET,TWITTER_KEY,TWITTER_SECRET
import os, json
import time
import logging
from tqdm import  tqdm
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

## tweepy configure
auth = tweepy.OAuthHandler(TWITTER_APP_KEY, TWITTER_APP_SECRET)
auth.set_access_token(TWITTER_KEY, TWITTER_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser(), wait_on_rate_limit=True)

class OnlineListener(tweepy.StreamListener):
    def __init__(self, config):
        self.config = config
        self.write_path = config["write_path"] if config != None and "write_path" in config else None
        if self.write_path != None:
            if not os.path.isdir(os.sep.join(self.write_path.split(os.sep)[:-1])):
                os.makedirs(os.sep.join(self.write_path.split(os.sep)[:-1]))
        self.writer = open(self.write_path, "w+") if self.write_path != None else None
        self.count = 0
        super(OnlineListener, self).__init__()

    def on_status(self, status):
        if status.retweeted:
            return
        if self.writer != None:
            self.writer.write(json.dumps(status._json) + "\n")
            self.count += 1
            if self.count % 500 == 0:
                logger.info(f'{self.count} tweets have been retrieved and saved to {self.write_path}')

    def on_error(self, status_code):
        if status_code == 420:
            logger.error("error")
            return False


def acquire_from_twitter_api(ids):
    tweets_success = []
    tweets_fail = []
    for idx, id in enumerate(ids):
        if idx % 500 == 0:
            logger.info(f'[I] number of ids processed: {idx}')
        try:
            tweets_success.append(api.get_status(id, tweet_mode='extended'))
        except tweepy.TweepError as e:
            tweets_fail.append([id, e])
    return tweets_success, tweets_fail


def search_tweets(query,max_tweets=300):
    results = []
    api = tweepy.API(auth)
    for status in tqdm(tweepy.Cursor(api.search, q=query).items(max_tweets)):
        results.append(status._json)
    return results

def write2file(status_list,path):
    if not os.path.isdir(os.sep.join(path.split(os.sep)[:-1])):
        os.makedirs(os.sep.join(path.split(os.sep)[:-1]))
    with open(path,"w+") as f:
        for status in status_list:
            f.write(json.dumps(status)+"\n")

def get_followers(screen_name):
    users = []
    for i, selection in enumerate(tweepy.Cursor(api.followers, screen_name=screen_name, count=200).pages()):
        logger.info('Getting page {} for user {} followers'.format(i, screen_name))
        users += selection["users"]
    return users


def get_following(screen_name):
    following = []
    for i, selection in enumerate(tweepy.Cursor(api.friends, screen_name=screen_name, count=200).pages()):
        logger.info('Getting page {} for user {} following users'.format(i, screen_name))
        following += selection["users"]
    return following


def get_user_timeline(screen_name):
    timeline = []
    api = tweepy.API(auth)
    for i, selection in enumerate(tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=200).pages()):
        logger.info('Getting page {} for user {} timeline'.format(i, screen_name))
        timeline.extend([status._json for status in selection])
    return timeline


def get_replies(tweet_id="xxxx", user_name="@wangcongcongcc"):
    api = tweepy.API(auth, wait_on_rate_limit=True)

    replies = tweepy.Cursor(api.search, q='to:{}'.format(user_name), since_id=tweet_id, tweet_mode='extended').items()
    while True:
        try:
            reply = replies.next()
            if not hasattr(reply, 'in_reply_to_status_id_str'):
                continue
            if reply.in_reply_to_status_id == tweet_id:
                logger.info("reply of tweet:{}".format(reply.full_text))

        except tweepy.RateLimitError as e:
            logger.error("Twitter api rate limit reached".format(e))
            time.sleep(60)
            continue

        except tweepy.TweepError as e:
            logger.error("Tweepy error occured:{}".format(e))
            break

        except StopIteration:
            break

        except Exception as e:
            logger.error("Failed while fetching replies {}".format(e))
            break

