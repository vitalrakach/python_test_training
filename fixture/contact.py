from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def open_add_contact_page(self):
        # open add new page
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, new_contact):
        # create contact
        wd = self.app.wd
        self.open_add_contact_page()
        # fill contact form
        self.fill_contact_form(new_contact)
        #submit adding user
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        self.app.open_home_page()

    def fill_contact_form(self, new_contact):
        wd = self.app.wd
        self.change_field_value("firstname", new_contact.firstname)
        self.change_field_value("middlename", new_contact.middlename)
        self.change_field_value("lastname", new_contact.lastname)
        self.change_field_value("nickname", new_contact.nickname)
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys("D:\\fakepath\\Kovrik_Ferma-01.jpg")
        self.change_field_value("title", new_contact.title)
        self.change_field_value("company", new_contact.company)
        self.change_field_value("address", new_contact.address)
        self.change_field_value("home", new_contact.home)
        self.change_field_value("mobile", new_contact.mobile)
        self.change_field_value("work", new_contact.work)
        self.change_field_value("fax", new_contact.fax)
        self.change_field_value("email", new_contact.email)
        self.change_field_value("email2", new_contact.email2)
        self.change_field_value("email3", new_contact.email3)
        self.change_field_value("homepage", new_contact.hompage)
        self.change_listbox_value("bday", new_contact.bday)
        #wd.find_element_by_name("theform").click()
        self.change_listbox_value("bmonth", new_contact.bmonth)
        self.change_field_value("byear", new_contact.byear)
        self.change_listbox_value("aday", new_contact.aday)
        self.change_listbox_value("amonth", new_contact.amonth)
        self.change_field_value("ayear", new_contact.ayear)
        self.change_field_value("address2", new_contact.address2)
        self.change_field_value("phone2", new_contact.phone2)
        self.change_field_value("notes", new_contact.notes)

    def change_listbox_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[7]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # summit deletion
        wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.app.open_home_page()


    def delete_all(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select checkbox "Select all"
        wd.find_element_by_id('MassCB').click()
        # summit deletion for all contacts
        wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")

        self.app.open_home_page()


    def edit_first_contact(self, new_contact):
        wd = self.app.wd
        #open hompage
        self.app.open_home_page()
        # find and click first icon by title
        wd.find_element_by_xpath('//*[@title="Edit"]').click()
        self.fill_contact_form(new_contact)
        #submit updating user
        wd.find_element_by_name("update").click()
        # open home page
        self.app.open_home_page()


    def add_contact_to_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # summit deletion
        wd.find_element_by_name("add").click()
        self.app.open_home_page()


    def open_home_page(self):
        # open home page
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") or (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0)):
            wd.get("http://localhost/addressbook/")

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath('//*[@title="Edit"]'))