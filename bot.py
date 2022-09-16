import tweepy
from dotenv import dotenv_values
from datetime import datetime
import json

class TwitterBot:
    def __init__(self, config):
        self.client = tweepy.Client(**config)
    
    def tweet(self, message):
        self.client.create_tweet(text=message)

    def get_todays_quote(self):
        with open('quotes.json') as f:
            quotes_list = json.load(f)['quotes']
        now = datetime.now()
        day_num = now.strftime('%j')
        index = int(day_num) % len(quotes_list)
        return quotes_list[index]

    def tweet_todays_quote(self):
        quote = self.get_todays_quote()
        self.tweet(quote)

def main():
    config = dotenv_values('.env')
    bot = TwitterBot(config)
    bot.tweet_todays_quote()

if __name__ == '__main__':
    main()
