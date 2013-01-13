# -*- coding: utf-8 -*-
from base.models import CRUDMixin
from ext import db


class Entry(CRUDMixin, db.Model):
    __tablename__ = 'entries'

    title = db.Column(db.String(128))
    short_description = db.Column(db.Text())
    description = db.Column(db.Text())

    def __init__(self, title, short_description, description):
        self.title = title
        self.short_description = short_description
        self.description = description

    def __repr__(self):
        return u'<Entry %r>' % self.title
