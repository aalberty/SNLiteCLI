from .api import Api

class Table(Api):
    def __init__(self, table, config):
        Api.__init__(self, config)
        if table and table != '':
            self.endpoint = '/api/now/table/' + table
        else:
            return "no table provided"
        
    def get_sample_rec(self):
        q_params = dict()
        url = self.base_url + self.endpoint
        q_params.update({
            "sysparm_limit": 1
        })
        return self.get_records(q_params)

    def get_records(self, params=dict()):
        url = self.base_url + self.endpoint
        return self.r.get(url, headers=self.headers, params=params)

    def get_record(self, sysid):
        url = self.base_url + self.endpoint + "/" + sysid
        return self.r.get(url, headers=self.headers)