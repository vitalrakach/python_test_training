# -*- coding: utf-8 -*-


def test_add_contact_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact_to_group()
    app.session.logout()