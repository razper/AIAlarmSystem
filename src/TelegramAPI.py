import requests
import telegram


class BotHandler:
    def __init__(self, token, proxy=None):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)
            self.bot = telegram.Bot(token=token)
            self.proxy = proxy

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params, proxies=self.get_proxy())
        result_json = resp.json()['result']
        return result_json

    def send_message(self, text):
        # user_id = (self.get_updates()[-1])["message"]["chat"]["id"]
        user_id = "-281395035"
        # params = {'chat_id': user_id, 'text': text, 'parse_mode': 'HTML'}
        # method = 'sendMessage'
        # requests.post(self.api_url + method, params, proxies=self.get_proxy())
        self.bot.send_message(chat_id=user_id, text=text, timeout=500)#, proxies=self.get_proxy())

    def send_photo(self, img):
        user_id = "-281395035"  # (self.get_updates()[-1])["message"]["chat"]["id"]
        self.bot.send_photo(chat_id=user_id, photo=open(img, 'rb'), timeout=500)#, proxies=self.get_proxy())

    def get_proxy(self):
        if self.proxy is None:
            return None
        http_proxy = "http://" + self.proxy
        https_proxy = "https://" + self.proxy
        proxyDict = {
            "http": http_proxy,
            "https": https_proxy,
        }
        return proxyDict
