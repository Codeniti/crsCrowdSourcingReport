#oggpnosn
#hkhr
import webapp2
from google.appengine.ext import ndb
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Task(ndb.Model):
    problemStatement=ndb.StringProperty(indexed=False)
    fund=ndb.FloatProperty()
    contributor=ndb.JsonProperty(indexed=True)
    status=ndb.BooleanProperty()
    projectName=ndb.StringProperty(indexed=False)
class Project(ndb.Model):
    taskList=ndb.JsonProperty()
    projectManager=ndb.StringProperty(indexed=False)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("homePage.html")
        self.response.write(template.render({}))

class ProjectPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("projectPage.html")
        self.response.write(template.render({}))

class SignIn(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("signInPage.html")
        self.response.write(template.render({}))

class ServicePage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("servicePage.html")
        self.response.write(template.render({}))
     
class AboutPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("aboutPage.html")
        self.response.write(template.render({}))

class ContactPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template("contactPage.html")
        self.response.write(template.render({}))
       

application = webapp2.WSGIApplication([
    ('/', MainPage),('/signIn',SignIn),('/projects',ProjectPage),('/services',ServicePage),('/about',AboutPage),('/contact',ContactPage)
], debug=True)
