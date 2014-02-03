import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):          
        self.response.out.write('test')

app = webapp2.WSGIApplication([('/test', MainPage), ],
                                debug=True)