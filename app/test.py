import unittest
from app import app
from models.model import *
import requests

class TestStringMethods(unittest.TestCase):



    def setUp(self):
        app.config['MYSQL_HOST'] = 'host.docker.internal'
        app.config['MYSQL_USER'] = 'mahdi'
        app.config['MYSQL_PASSWORD'] = '1234'
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        app.config.setdefault("MYSQL_PORT", 3306)
        app.config.setdefault("MYSQL_UNIX_SOCKET", None)
        app.config.setdefault("MYSQL_CONNECT_TIMEOUT", 10)
        app.config.setdefault("MYSQL_READ_DEFAULT_FILE", None)
        app.config.setdefault("MYSQL_USE_UNICODE", True)
        app.config.setdefault("MYSQL_CHARSET", "utf8")
        app.config.setdefault("MYSQL_SQL_MODE", None)
        app.config.setdefault("MYSQL_CURSORCLASS", None)
        app.config.setdefault("MYSQL_AUTOCOMMIT", False)
        app.config.setdefault("MYSQL_CUSTOM_OPTIONS", None)

        self.app = app.test_client()
        self.base_url = 'http://localhost:4000'    
 
    def test_add_book_invalid(self):
        endpoint = "/add_book"
        try:
            data=dict(title="Divanegi" , numPages=-1 , author="jamal yousef")
            response = requests.post(self.base_url+endpoint , data=data) # gives error because numPages cannot be negative 
            response.raise_for_status()
        except Exception as e:
            # print(response.text)
            if "Error" in response.text:
                print("Error in adding books..." , str(e))


    def test_add_member_invalid(self):
        endpoint = "/add_member"
        try:
            data = dict(name="ali",lastname="kasraei",username="aliksr",password="12345678",phonenumber="9136888458",address="Isfahan")
            response = requests.post(self.base_url+endpoint , data=data) # no error
            response.raise_for_status()
        except Exception as e:
            if "Error" in response.text:
                print("Error in adding members..." , str(e))    


    def test_edit_member_invalid(self):
        endpoint = "/edit_member/1"
        try:
            data = dict(name="mohammad",lastname="jamali",username="mahdijml",password="1234567",phonenumber="9137777777",address="Isfahan")
            response = requests.post(self.base_url+endpoint , data=data) # gives error because password must be at least 8 characters ...
            response.raise_for_status()
        except Exception as e:
            if "Error" in response.text:
                print("Error in editting members..." , str(e))


if __name__ == '__main__':
    unittest.main()