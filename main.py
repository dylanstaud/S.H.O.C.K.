#self.response.write("Is this working yet?!?!?!")

import jinja2
import webapp2
import os

jinja_current_directory =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Greeting(webapp2.RequestHandler):
    def get(self):
        greet = "hi"
        index_template =jinja_current_directory.get_template("templates/index.html")
        self.response.write(index_template.render())

app = webapp2.WSGIApplication([
    ('/', Greeting),
], debug=True)
