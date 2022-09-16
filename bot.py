import tweepy
from dotenv import dotenv_values

class TwitterBot:
    def __init__(self, config):
        self.client = tweepy.Client(**config)
    
    def tweet(self, message):
        self.client.create_tweet(text=message)

def main():
    config = dotenv_values('.env')
    bot = TwitterBot(config)
    message = 'hello world'
    bot.tweet(message)

if __name__ == '__main__':
    main()
