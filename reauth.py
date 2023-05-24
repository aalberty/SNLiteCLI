from datetime import datetime
import json

from api.auth import *

file = open('config.json', 'r')
config = json.loads(file.read())
file.close()

res = refresh_token(config)
now = datetime.now()
if res.status_code == 200:
    config['access_token'] = json.loads(res.text)['access_token']
    config['expires'] = calc_new_expiry(now, json.loads(res.text)['expires_in'])
    update_config(config, 'config.json')
else:
    print ("Error refreshing token: " + res.error_message)

