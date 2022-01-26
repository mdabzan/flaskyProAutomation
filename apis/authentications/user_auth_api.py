import configparser
import requests
import json

class AuthenticationsApi:

    @classmethod
    def setUpClass(cls):
        cls.JWT = 'JWT '

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read_file(open("/Users/mabzan/AtomProjects/flaskyProAutomation/test_auto.cfg"))
        self.baseurl = self.config.get('app','url')
        self.JWT = 'JWT '
        # self.admin_username = self.config.get('admin','username')
        # self.admin_password = self.config.get('admin','password')

    def get_admin_token(self, body):
        newHeaders = {'Content-type': 'application/json',
                        'Accept': 'text/plain'}
        url = self.baseurl + '/auth'
        resp = requests.post(url, json=body, headers= newHeaders)
        content = resp.json()
        access_token = str(self.JWT + content['access_token'])
        return access_token
