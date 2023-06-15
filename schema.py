import sys
import json

from table_api import Table
from auth import load_config 
from api import handle_response

config = load_config('config.json')
t = Table('sys_dictionary', config)
q = {"sysparm_query": "nameINincident,task^internal_type!=collection^ORinternal_type=NULL"}
res = handle_response(t.get_records(q))

if (res != False):
    print(json.dumps(res, indent=4))


# TODO parse the schema
