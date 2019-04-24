# -*- coding: utf-8 -*-


def test_add_contact_to_group(app):
    app.contact.add_contact_to_group()
    app.session.logout()