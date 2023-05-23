from .api import Api

class Table(Api):
    def __init__(self, table, config):
        Api.__init__(self, config)
        if table and table != '':
            self.endpoint = '/api/now/table/' + table
        else:
            return "no table provided"
        
    def get_sample_rec(self):
        url = self.base_url + self.endpoint
        return self.r.get(url, headers=self.headers)