# -*- coding: utf-8 -*-


def test_delete_contact(app):
        app.contact.delete_all()
        app.session.logout()