import requests as r
import json

file = open('config.json', 'r')
global config
config = json.loads(file.read())

#TODO: test refresh_token
def refresh_token(config):
    url = config.base_url + "/oauth_token.do"
    
    data = {
        "grant_type": "refresh_token",
        "refresh_token": config.refresh_token,
        "redirect_uri": config.base_url + "/oauth_redirect.do",
        "client_id": config.client_id,
        "client_secret": config.client_secret
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = r.post(url, headers=headers, data=data)
