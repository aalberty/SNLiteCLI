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


def handle_response (res):
        if (res.status_code and res.ok == False):
            print(f"Error retrieving sample rec. {res.status_code} {res.reason} -- {res.text}")
            return False 
        else:
            return res.json()
