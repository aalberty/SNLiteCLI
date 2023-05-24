from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text as pprint
from rich import print_json

import sys

from cli.debug_cmds import *
from api.table_api import Table
from api.auth import load_config

config = None

def exit_cli():
    sys.exit("terminating...")

def not_recognized(cmd):
    text = FormattedText([
            ('', "Sorry, I don't recognize the "),
            ('class:command_text', cmd),
            ('', " command")
        ])
    style = Style.from_dict({
        'command_text': 'lime'
    })
    print(text, style=style)

def search():
    pass

def _list():
    pass

def authenticate(path):
    global config
    config = load_config(path)

def sample(table_name):
    global config
    t = Table(table_name, config)
    res = t.get_sample_rec()
    if res.status_code == 200:
        data = res.json()['result'][0]
        print_json(data=data)
        return data
    else:
        print("There was a problem retrieving your sample record.")
        error_message = f"Status code: {res.status_code} - {res.reason}\nError message: {res.text}"
        print(error_message)
        return error_message
        
