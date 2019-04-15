# -*- coding: utf-8 -*-

#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import Select
import unittest
from group import Group
from application import Application

class test_add_group(unittest.TestCase):

    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="new_group", header="new_group", footer="wow"))
        self.app.logout()

    def test_add_group_empty(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
