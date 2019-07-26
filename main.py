<<<<<<< HEAD
import webapp2
import os


jinja_current_directory =  jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        random_fortune = "hi"
        results_template =jinja_current_directory.get_template("index.html")
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        self.response.write(results_template.render(random_fortune))


app = webapp2.WSGIApplication([
    # This line routes the main url ('/')  - also know as
    # The root route - to the Fortune Handler
    ('/', FortuneHandler),
 #maps '/predict' to the FortuneHandler
], debug=True)
=======
print("Hello World")
>>>>>>> 1f55868dd0298b9f0b5506f6cf7ee2ca195abb99
