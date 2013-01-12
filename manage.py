#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
from flask.ext.script import Shell, Manager
from app import app
from ext import db


manager = Manager(app)


@manager.command
def clean_pyc():
    """Removes all *.pyc files from the project folder"""
    clean_command = "find . -name *.pyc -delete".split()
    subprocess.call(clean_command)


@manager.command
def init_data():
    """Fish data for project"""
    db.drop_all()
    db.create_all()


manager.add_command('shell', Shell(make_context=lambda: {'app': app, 'db': db}))


if __name__ == '__main__':
    manager.run()
