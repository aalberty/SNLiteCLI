from ..api.table_api import Table
from ..api.auth import load_config
import requests

config = load_config("../config.json")

def instantiate_table(table_name):
    global config
    return Table(table_name, config)

def get_sample_record(table_name):
    t = instantiate_table(table_name)
    rec = t.get_sample_rec()
    print ("code: " + str(rec.status_code) + ", text: " + rec.text[:200]) 
    return rec

def test_instantiation():
    assert type(instantiate_table('incident')) == Table

def test_sample_record_retrieval():
    assert get_sample_record('incident').status_code == 200
    
