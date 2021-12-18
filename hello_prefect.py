import prefect
from prefect import task, Flow
import tweepy

credentials = {"api_key": "",
               "api_secret": "",
               "access_token": "",
               "access_token_secret": ""}

@task
def hello_task():
    logger = prefect.context.get("logger")
    logger.info("Hello world!")

@task
def get_twitter_replies():
    auth = tweepy.OAuthHandler(credentials["api_key"], credentials["api_secret"])
    auth.set_access_token(
        credentials["access_token"], credentials["access_token_secret"]
    )

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    return [tweet.text for tweet in public_tweets[:10]]

@task
def show_replies(replies):
    print(replies)

with Flow("hello-flow") as flow:
    hello_task()
    show_replies(get_twitter_replies())

flow.run()
