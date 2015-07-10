import sys
import webapp2
from google.appengine.api import mail
# from google.appengine.api import users

#TODO
# for smtp_host
#dev_appserver.py --smtp_host=smtp.gmail.com --smtp_port=25 --smtp_user=goryo.webdev@gmail.com --smtp_password= myapp


class MessageMe(webapp2.RequestHandler):

    def get(self):     
        pass

    def post(self):
        
        #TODO validation
        #if not mail.is_email_valid(to_addr):
        
        name = self.request.get('name')
        fromemail = self.request.get('fromemail')
        subject = self.request.get('subject')
        massage = self.request.get('message')
        
        
        #validation
        if (not name) or (not fromemail) or (not subject) or (not massage):
            self.response.out.write("All fields are required.")
        
        elif not mail.is_email_valid(fromemail):
            self.response.out.write("Please enter a valid email.")
        
        else: #process email
            message = mail.EmailMessage()
            message.sender = "goryo.webdev@gmail.com"
            message.subject = "Email from Goryofolio Site - " + subject
            message.to = "goryo.webdev@gmail.com"
            message.body = """

From: %s
From Email: %s
 
Message: %s

        """ % (name, fromemail, massage)
            
            try:
                message.send() 
                #self.response.out.write(name)
                self.response.out.write("Message sent!")
            except:
                e = sys.exc_info()[0]
                self.response.out.write("Error sending the message " + e)
                
app = webapp2.WSGIApplication([('/messageme', MessageMe), ],
                                debug=True)