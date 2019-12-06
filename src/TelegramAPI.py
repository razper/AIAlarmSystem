import requests
import sys
from src.UriDictionary import token
whitelist = [sys.argv[1]]


class BotHandler:
    def __init__(self, token=token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def send_message(self, text):
        for user_id in whitelist:
            params = {'chat_id': user_id, 'text': text, 'parse_mode': 'HTML'}
            method = 'sendMessage'
            requests.post(self.api_url + method, params)


if __name__ == '__main__':
    bot = BotHandler()
    bot.send_message("Person detected")
