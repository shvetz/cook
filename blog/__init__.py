# -*- coding: utf-8 -*-
from flask import Blueprint


blog = Blueprint(
    'blog', __name__,
    template_folder='templates',
    url_prefix='/blog'
)


from views import *
