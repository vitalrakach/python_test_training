from selenium import webdriver
from selenium.webdriver.support.ui import Select
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)


    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def login(self, username, password):
        # login
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):     # init group creation
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self,):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def open_add_new_page(self):
        # open add new page
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_user(self, new_user):
        # create user
        wd = self.wd
        self.open_add_new_page()
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
        self.open_home_page()


    def destroy(self):
        self.wd.quit()

