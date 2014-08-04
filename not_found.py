import webapp2
import jinja2
import os
import cgi
import datetime
import urllib
import sys

from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api import users

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self):          
        self.response.out.write('Error 404')

app = webapp2.WSGIApplication([('/', MainPage), ],
                                debug=True)