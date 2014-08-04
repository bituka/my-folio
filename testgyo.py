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

import paging.paging

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Aso(db.Model):
    lakis = db.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):          
      
      lakis = db.GqlQuery("SELECT * FROM Aso")

      template_values = {
        'lakis' = lakis
      }

      template = jinja_environment.get_template('test.html')
      self.response.out.write(template.render(template_values))


        
app = webapp2.WSGIApplication([('/testgyo', MainPage), 
                               ],
                                debug=True)