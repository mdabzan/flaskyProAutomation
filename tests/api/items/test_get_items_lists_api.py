import requests
from nose.tools import assert_equal

from apis.authentications.user_auth_api import AuthenticationsApi


class TestRequest:

    @classmethod
    def setUpClass(cls):
        cls.JWT = 'JWT '
        cls.auth = AuthenticationsApi()
        cls.admin_username = cls.auth.config.get('admin','username')
        cls.admin_password = cls.auth.config.get('admin','password')

    def test_get_all_items_list_200(self):
        body = {"username": self.admin_username, "password": self.admin_password}
        response = requests.get("http://127.0.0.1:5002/items",
                                headers={'Authorization': self.auth.get_admin_token(body)})
        print(response.json())
        assert_equal(response.status_code, 200)

    def test_get_all_items_list_401(self):
        response = requests.get("http://127.0.0.1:5002/items",
                                headers={'Authorization': 'INVALID'})
        print(response.json())
        assert_equal(response.status_code, 401)
