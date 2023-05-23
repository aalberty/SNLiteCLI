import requests as r

class Api():
    def __init__(self, config):
        self.r = r
        self.headers = {
            "Content-Type":"application/json",
            "Accept":"application/json",
            "Authorization": "Bearer " + config['access_token']
        }
        self.base_url = config['base_url']

