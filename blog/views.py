# -*- coding: utf-8 -*-
from flask.templating import render_template
from flask.views import MethodView
from blog import blog


class PostView(MethodView):

    def get(self):
        entries = [
              {'post_title': u'Вкуснятина', 'post_description': u'Ок'},
              {'post_title': u'Ещё одна', 'post_description': u'Ок'}
        ]

        context = {'entries': entries}

        return render_template('blog/post.html', **context)

blog.add_url_rule('/post', view_func=PostView.as_view('post_page'))
