import webapp2
import jinja2
import os
import cgi
import datetime
import urllib
import sys
import random, string

from google.appengine.ext import db
from google.appengine.api import images
from google.appengine.api import users

import paging.paging

from paging.paging import *

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Aso(db.Model):
    laki = db.StringProperty()

#TODO paging implem
class MainPage(webapp2.RequestHandler):
  
    def get(self):          
      
      page_num = str(self.request.get('page_num'))
      nextpage = self.request.get('nextpage')
      previouspage = self.request.get('previouspage')
      
      if (not page_num) or (page_num == ' '): 
        page_num = 1
      
      if nextpage: 
        page_num = int(page_num) 
        page_num += 1
      
      if previouspage: 
        page_num = int(page_num)
        page_num -= 1

      myPagedQuery = PagedQuery(Aso.all(), 10)

      nextPageExists = myPagedQuery.has_page(page_num + 1)
      previousPageExists = myPagedQuery.has_page(page_num - 1)
      
      num_pages = myPagedQuery.page_count()
      
      asos = myPagedQuery.fetch_page(page_num)
      

     # asos = db.GqlQuery("SELECT * FROM Aso")

      template_values = {
        'asos' : asos,
        'nextPageExists' : nextPageExists,
        'previousPageExists' : previousPageExists,
        'page_num' : page_num
      }

      template = jinja_environment.get_template('test.html')
      self.response.out.write(template.render(template_values))

    def post(self):          
    
      for x in range(20):
        aso = Aso()
        aso.laki = ''.join(random.choice(string.lowercase) for i in range(20))
        aso.put()
        self.redirect('/testpaginggyo')

    #  self.response.out.write('test')
      
    #  template = jinja_environment.get_template('test.html')
    #  self.response.out.write(template.render(template_values))
        
app = webapp2.WSGIApplication([('/testpaginggyo', MainPage), 
                               ],
                                debug=True)