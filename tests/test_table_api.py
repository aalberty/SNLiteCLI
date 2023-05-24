from ..api.table_api import Table
from ..api.auth import load_config
import requests, json

t = None
config = load_config("../config.json")
test_sysid = ""

def print_partial_response(res):
    print ("code: " + str(res.status_code) + ", text: " + res.text[0:200]) 

def instantiate_table(table_name):
    global config
    global t
    t = Table(table_name, config)
    return t

def get_sample_record():
    global t
    rec = t.get_sample_rec()
    print_partial_response(rec)
    return rec

def get_rec_list():
    global t
    global test_sysid
    recs = t.get_records()
    if recs.status_code == 200:
        recs_obj = recs.json()['result']
        test_sysid = recs_obj[0]['sys_id']
    return recs

def get_rec():
    global test_sysid
    res = t.get_record(test_sysid)
    print_partial_response(res)
    return res

def test_instantiation():
    assert type(instantiate_table('incident')) == Table

def test_sample_record_retrieval():
    rec = get_sample_record()
    rec_obj = rec.json()
    assert rec.status_code == 200
    assert len(rec_obj['result']) == 1

def test_get_rec_list():
    assert get_rec_list().status_code == 200

def test_get_rec():
    global test_sysid
    res = get_rec()
    assert res.status_code == 200
    assert res.json()['result']['sys_id'] == test_sysid