# -*- coding: utf-8 -*-
from model.new_contact import New_contact

def test_delete_all_contacts(app):
        if app.contact.count() == 0:
                app.contact.create(
                        New_contact(firstname="NEW", middlename="NEW", lastname="Rakach", nickname="v1t_al",
                                    title="ZAO",
                                    company="Adani", address="Minsk_work", home="1234567",
                                    mobile="9876543", work="4394423", fax="3487654", email="rakach1@mail.com",
                                    email2="rakach2@mail.com", email3="rakach3@mail.com",
                                    hompage="", bday="1", bmonth="October", byear="1999", aday="5", amonth="January",
                                    ayear="2000",
                                    address2="minsk", phone2="", notes=""))
        app.contact.delete_all()
#        contact_list = app.contact.get_contact_list()
        assert app.contact.count() == 0