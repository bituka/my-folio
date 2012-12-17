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

#from google.appengine.api import users

class Portfolio(db.Model):
    image = db.BlobProperty()
    title = db.StringProperty()
    description = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self):       
        portfolios = db.GqlQuery("SELECT * FROM Portfolio")
            
        template_values = {
            'portfolios': portfolios,
        }
        
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class AdminPage(webapp2.RequestHandler):
    def get(self):       
        
        user = users.get_current_user()
        if (user and user.nickname() == 'goryo.webdev'):

            portfolios = db.GqlQuery("SELECT * FROM Portfolio")
            
            template_values = {
                'portfolios': portfolios,
            }
            
            template = jinja_environment.get_template('admin.html')
            self.response.out.write(template.render(template_values))	
        else:
            
            self.redirect(users.create_login_url(self.request.uri))

        
    def post(self):   
        portfolio = Portfolio()
        portfolio.title = self.request.get('title')		
        portfolio.description = self.request.get('description')
        image = self.request.get('img')
        portfolio.image = db.Blob(image)
        portfolio.put()
        self.redirect('/admin')


class EditPortfolio(webapp2.RequestHandler):
    def get(self):
    
        portfolio = db.get(self.request.get('id'))
        template_values = {
            'portfolio': portfolio,
        }
        
        template = jinja_environment.get_template('admin_editp.html')
        self.response.out.write(template.render(template_values))    

    def post(self):

        portfolio = db.get(self.request.get('id'))

        portfolio.title = self.request.get('title')        
        portfolio.description = self.request.get('description')
        image = self.request.get('img')
        if image:
            portfolio.image = db.Blob(image)
        portfolio.put()
        self.redirect('/admin')		
        
class DeletePortfolio(webapp2.RequestHandler):
    def post(self):
        portfolio = db.get(self.request.get('id'))
        portfolio.delete()
        self.redirect('/admin')         
       
class Image(webapp2.RequestHandler):
    def get(self):
        portfolio = db.get(self.request.get('img_id'))
        
        if portfolio.image:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(portfolio.image)
        else:
            self.error(404)   
            
        
app = webapp2.WSGIApplication([('/', MainPage),
                                ('/img', Image),
                                ('/editportfolio', EditPortfolio),
                                ('/deleteportfolio', DeletePortfolio),
                                ('/admin', AdminPage), ],
                                debug=True)
                              
                              
