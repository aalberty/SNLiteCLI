import requests as r
import json
from datetime import datetime, timedelta

def refresh_token(config):
    url = config['base_url'] + "/oauth_token.do"
    
    data = {
        "grant_type": "refresh_token",
        "refresh_token": config['refresh_token'],
        "redirect_uri": config['base_url'] + "/oauth_redirect.do",
        "client_id": config['client_id'],
        "client_secret": config['client_secret']
    }
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    res = r.post(url, headers=headers, data=data)
    return res

def update_config(config, file_path):
    file = open(file_path, 'w')
    file.write(json.dumps(config))

def load_config(file_path):
    file = open(file_path, 'r')
    config = json.loads(file.read())
    file.close()
    return config
    
def calc_new_expiry(response_time, expires_in):
    fstr = "%Y-%m-%d %H:%M:%S"
    expiry = response_time + timedelta(seconds=expires_in)
    return expiry.strftime(fstr)