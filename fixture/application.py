from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import time


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(executable_path="C:\\Projects\\chromedriver.exe")
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost1/addressbook/")


    def destroy(self):
        self.wd.quit()

