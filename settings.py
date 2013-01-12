# -*- coding: utf-8 -*-
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = "MY_VERY_SECRET_KEY"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    CSRF_ENABLED = True
    ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

    BLUEPRINTS = ['base.base']

    EXTENSIONS = ['ext.db',
                  'ext.assets',
                  'ext.toolbar',
                  ]


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
