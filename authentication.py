import tweepy

def authFunc():
    auth = tweepy.OAuthHandler("BM6bJfC4L9OdXc2NWsXGblPPB", "OKQ9bHd8yKvVFp2GzxI5fAdFYOwYgpCNSNlO2EYwBaoIB3PsIc")
    auth.set_access_token("1601079695314980866-wQLrb9xl3gK4V1CELzVLA6DVSkMhZ7", "XBfTREGEL3SFndVyrfJ6gHOuXjFqrUQ9FGcN2YXCF4LcN")
    tweepy.API(auth)