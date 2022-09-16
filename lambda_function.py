import logging
from dotenv import dotenv_values
from datetime import datetime
from bot import TwitterBot

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    config = dotenv_values('.env')
    bot = TwitterBot(config)
    bot.tweet_todays_quote()

    logger.info(f'Tweeted today\'s quote at {datetime.now()}')
