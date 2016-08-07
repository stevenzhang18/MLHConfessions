
import logging

log = logging.getLogger(__name__)
from base import *
from google.appengine.ext import ndb


class TweetModel(ndb.Model):
    message=ndb.StringProperty()
    person=ndb.StringProperty()

# class PlotSentiment(ndb.Model):
#     sentiment=ndb.FloatProperty(repeat=true)
#     date=ndb.StringProperty(repeat=true)
class MainHandler(BaseHandler):
    def get(self):
        # self.response.out.write("Sorry we're down. You guys are too immature.")
        self.render_template('index.template')


class ResultHandler(BaseHandler):
    def get(self):
        self.redirect(self.uri_for('home'))
    def post(self):
        message=self.request.get('message')
        try:
            new_tweet=TweetModel(message=message, person = self.request.get('person'))
            new_tweet.put()
            # api.update_status(status=message+" "+self.request.get('person'))
            # self.redirect("https://twitter.com/MLH_Confessions")
        except:
            self.redirect(self.uri_for('home'))
class TrendsHandler(BaseHandler):
    def get(self):
        self.redirect(self.uri_for('home'))
class AdminHandler(BaseHandler):
    def get(self):
        results = TweetModel.query().fetch()
        messages= []
        user=[]
        approvals= {}
        i=0
        for result in results:
            approvals[i]=result.message+ " " + result.person
            i= i+1
        template_values={}
        template_values[''] = key.get().cities
        self.render_template('admin.template')

# class AccessHandler(BaseHandler):
#     def get(self):
#         logging.info('access requested')
#         template = jinja_environment.get_template('access.template')
#         self.response.out.write(template.render())
#
#     def post(self):
#       username = self.request.get('u').lower()
#       password = self.request.get('p')
#       try:
#         u = self.auth.get_user_by_password(username, password, remember=True,
#           save_session=True)
#         self.redirect(self.uri_for('admin'))
#       except (InvalidAuthIdError, InvalidPasswordError) as e:
#         logging.info('Login failed for user %s because of %s', username, type(e))
#         self._serve_page(True)
#
#     def _serve_page(self, failed=False):
#       username = self.request.get('username')
#       params = {
#         'username': username,
#         'failed': failed
#       }
#       template = jinja_environment.get_template('access.template')
#       self.response.out.write(template.render(params))
#
#
# class SignupHandler(BaseHandler):
#     def get(self):
#         self.redirect(self.uri_for('access'))
#
#     def post(self):
#         email = self.request.get('email').lower()
#         company=self.request.get('company').lower()
#         user_name =email
#         password = self.request.get('password').lower()
#         confirmpassword = self.request.get('confirmPassword').lower()
#
#         unique_properties = ['email_address']
#
#         user_data = self.user_model.create_user(user_name,
#           unique_properties,
#           email_address=email, name="", password_raw=password,
#           last_name="",admin =True, verified=False, company=company)
#         if not user_data[0]: #user_data is a tuple
#             self.display_message('Unable to create user for email %s because of \
#             duplicate keys %s' % (user_name, user_data[1]))
#             self.redirect(self.uri_for('access'))
#             return
#
#         user = user_data[1]
#         user_id = user.get_id()
#
#
#         CName=company
#         CEmail=email
#         CreateOrg(CName,CEmail)
#
#
#         token = self.user_model.create_signup_token(user_id)
#
#         verification_url = self.uri_for('verification', type='v', user_id=user_id,
#           signup_token=token, _full=True)
#
#         msg = 'Send an email to user in order to verify their address. \
#               They will be able to do so by visiting <a href="{url}">{url}</a>'
#
#         self.display_message(msg.format(url=verification_url))
