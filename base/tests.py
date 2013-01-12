# -*- coding: utf-8 -*-
from flask import url_for
from testing import KitTestCase


class TestFrontBlueprint(KitTestCase):

    def test_front(self):
        response = self.client.get(url_for('base.front_page'))
        self.assert200(response)
