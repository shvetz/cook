# -*- coding: utf-8 -*-
from flask.templating import render_template
from flask.views import MethodView
from base import base


class FrontView(MethodView):

    def get(self):
        return render_template('base/main.html')

base.add_url_rule('', view_func=FrontView.as_view('front_page'))
