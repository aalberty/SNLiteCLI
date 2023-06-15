import sys
import json

from table_api import Table
from auth import load_config

if (len(sys.argv) <= 1):
    table = input('What table would you like a sample from? ')

else:
    table = sys.argv[1]

config = load_config('config.json')
t = Table(table, config)
res = t.get_sample_rec()
if (res.status_code == 200):
    print(json.dumps(res.json(), indent=4))
else:
    print(f"Error retrieving sample rec. {res.status_code} {res.reason} -- {res.text}")


