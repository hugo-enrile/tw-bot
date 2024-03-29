import os, sys, time, json, random
import tempfile, requests
import urllib.request
import logging
import tweepy

logging.basicConfig(filename='bot.log', filemode='a', format='%(asctime)s - %(levelname)s: %(message)s', level=logging.INFO)

def lambda_handler(event, context):
    
    logging.info("Getting credentials")

    BEARER_TOKEN = os.getenv("BEARER_TOKEN")
    API_KEY = os.getenv("API_KEY")
    API_KEY_SECRET = os.getenv("API_KEY_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
        
        
    logging.info("OK - Credentials")
    
    logging.info("Authenticating")
    
    client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    
    if api is None:
        logging.error("FAIL - Something went wrong during authentication")
        return
        
    logging.info("OK - Authentication")
    
    logging.info("Generating tweet")
    tweet = "This is a test"
    if tweet is None:
        logging.error("FAIL - Tweet was not correctly generated")
        return
    
    logging.info(f"OK - Generation. Tweet: {tweet}")

    logging.info(f"Post tweet")
    client.create_tweet(text=tweet)

    return {
        'statusCode': 200,
        'tweet': tweet
    }
    

    
    
    
