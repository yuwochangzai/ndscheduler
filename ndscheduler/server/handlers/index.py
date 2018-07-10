"""Serves the single page app web ui."""

import json

from ndscheduler import settings
from ndscheduler import utils
from ndscheduler.server.handlers import base


class Handler(base.BaseHandler):
    """Index page request handler."""

    def get(self):
        """Serve up the single page app for scheduler dashboard."""
        if not self.current_user:
            self.redirect("/login")
            return
        meta_info = utils.get_all_available_jobs()
        self.render(settings.APP_INDEX_PAGE, jobs_meta_info=json.dumps(meta_info))

class LoginHandler(base.BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   'Password: <input type="password" name="pwd">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        if (self.get_argument("name") == settings.USER_AUTH_CONFIG['user']) and (self.get_argument("pwd") == settings.USER_AUTH_CONFIG['pwd']):
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")
        else:
            self.redirect('/login')