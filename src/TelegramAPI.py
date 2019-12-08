import requests
from src.UriDictionary import token


class BotHandler:
    def __init__(self, token=token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, text):
        user_id = self.get_updates()[-1].message.chat_id
        params = {'chat_id': user_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        # self.send_photo(chat_id=user_id, photo=open(img, 'rb'))
        requests.post(self.api_url + method, params)


if __name__ == '__main__':
    bot = BotHandler()
    bot.send_message("Person detected")
