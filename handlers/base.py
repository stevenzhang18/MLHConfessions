
import os
import webapp2
import jinja2
import json
import sys
import os.path

from google.appengine.ext.webapp import template

from api_key import *
import logging
from datetime import *
import tweepy


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

log = logging.getLogger(__name__)
#
# jinja_environment = jinja2.Environment(
#     loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
#     extensions=['jinja2.ext.autoescape'],
#     autoescape=True)

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader('views'))

class BaseHandler(webapp2.RequestHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
	def render_template(self, view_filename, params=None):
		if not params:
			params = {}
		# user = self.user_info
		# params['user'] = user
		path = os.path.join(os.path.dirname(__file__), 'views', view_filename)
		self.response.out.write(template.render(path, params))
