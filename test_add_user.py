# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from new_user import New_user

class AddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_user(self):
        wd = self.wd
        self.login(wd, username="admin", password="secret")
        self.create_user(wd, New_user(firstname="Vital", middlename="Leonidovich", lastname="Rakach", nickname="v1t_al", title="ZAO", company="Adani", address="Minsk_work", home="1234567",
                         mobile="9876543", work="4394423", fax="3487654", email="rakach1@mail.com", email2="rakach2@mail.com", email3="rakach3@mail.com",
                         hompage="http://home.by", bday="5", bmonth="October", byear="1985", aday="15", amonth="October", ayear="1999", address2="Minsk_secondary",
                         phone2="My_home", notes="Some notes"))
        self.logout(wd)

    def open_add_new_page(self, wd):
        # open add new page
        wd.find_element_by_link_text("add new").click()

    def create_user(self, wd, new_user):
        # create user
        self.open_add_new_page(wd)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(new_user.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(new_user.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(new_user.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(new_user.nickname)
        #wd.find_element_by_name("photo").click()
        #wd.find_element_by_name("photo").clear()
        #wd.find_element_by_name("photo").send_keys("D:\\fakepath\\Kovrik_Ferma-01.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(new_user.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(new_user.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(new_user.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(new_user.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(new_user.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(new_user.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(new_user.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(new_user.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(new_user.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(new_user.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(new_user.hompage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(new_user.bday)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[7]").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(new_user.bmonth)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[44]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(new_user.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(new_user.aday)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[17]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(new_user.amonth)
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[44]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(new_user.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(new_user.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(new_user.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(new_user.notes)
        #submit adding user
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.open_home_page(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd, username, password):
        # Lonin
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        # Open homepage
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
