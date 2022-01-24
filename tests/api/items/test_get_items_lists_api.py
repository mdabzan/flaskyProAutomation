import requests
from nose.tools import assert_equal

auth_token = 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDMwMDY5NTgsImlhdCI6MTY0MzAwNjY1OCwibmJmIjoxNjQzMDA2NjU4LCJpZGVudGl0eSI6MX0.xpvJuTLODKju-2u0DnO1X3cJXDvsqYz2UYOPGJqfGDQ'

def test_get_all_items_list_200():
    response = requests.get("http://127.0.0.1:5002/items", headers={'Authorization': auth_token})
    print(response.json())
    print(response.status_code)
    assert_equal(response.status_code, 200)
