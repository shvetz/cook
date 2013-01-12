# -*- coding: utf-8 -*-
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.assets import Environment


db = SQLAlchemy()
assets = Environment()
toolbar = lambda app: DebugToolbarExtension(app)  # has no init_app()
