# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddUser(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)

    def test_add_user(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.open_add_new_page(wd)
        self.create_user(wd)
        self.logout(wd)

    def open_add_new_page(self, wd):
        # open add new page
        wd.find_element_by_link_text("add new").click()

    def create_user(self, wd):
        # create user
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Vital")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Leonidovich")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Rakach")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("v1t_al")
        #wd.find_element_by_name("photo").click()
       # wd.find_element_by_name("photo").clear()
       # wd.find_element_by_name("photo").send_keys("C:\\fakepath\\photo1.jpg")
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("ZAO")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Adani")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Minsk_work")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("1234567")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("9876543")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("4394423")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("3487654")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("rakach1@mail.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("rakach2@mail.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("rakach3@mail.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("http://home.by")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("5")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[7]").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[44]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1985")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("15")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[17]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[44]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1999")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Minsk_secondary")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("My_home")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Some notes")
        # submit addind user
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def login(self, wd):
        # Lonin
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
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
