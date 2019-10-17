# -*- coding: utf-8 -*-
from model.new_contact import New_contact


'''def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    new_contact_var = New_contact(firstname="NEW", middlename="NEW", lastname="Rakach", nickname="v1t_al", title="ZAO",
                    company="Adani", address="Minsk_work", home="1234567",
                    mobile="9876543", work="4394423", fax="3487654", email="rakach1@mail.com",
                    email2="rakach2@mail.com", email3="rakach3@mail.com",
                    hompage="", bday="1", bmonth="October", byear="1999", aday="5", amonth="January", ayear="2000",
                    address2="minsk", phone2="", notes="")
    app.contact.create(new_contact_var)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(new_contact_var)
    assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)

'''

def test_add_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    new_contact_var = New_contact(lastname="123", firstname="321")
    app.contact.create(new_contact_var)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
#    old_contacts.append(new_contact_var)
 #   assert sorted(old_contacts, key=New_contact.id_or_max) == sorted(new_contacts, key=New_contact.id_or_max)
