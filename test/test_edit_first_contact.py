# -*- coding: utf-8 -*-
from model.new_contact import New_contact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(New_contact(firstname="Edited", middlename="Leonidovich", lastname="Rakach", nickname="v1t_al", title="ZAO", company="Adani", address="Minsk_work", home="1234567",
                               mobile="9876543", work="4394423", fax="3487654", email="rakach1@mail.com", email2="rakach2@mail.com", email3="rakach3@mail.com",
                               hompage="", bday="1", bmonth="September", byear="1998", aday="6", amonth="February", ayear="2001", address2="Minsk", phone2="", notes="Edited"))
    app.session.logout()



