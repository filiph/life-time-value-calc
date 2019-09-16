from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class AllHandler(webapp.RequestHandler):
    def get(self):
        self.redirect("https://github.com/googlearchive/life-time-value-calc", permanent=True)

app = webapp.WSGIApplication([('/.*', AllHandler)])
