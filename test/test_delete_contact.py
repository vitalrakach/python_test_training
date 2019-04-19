# -*- coding: utf-8 -*-

from model.new_contact import New_contact





def test_delete_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.delete_first()
        app.session.logout()
