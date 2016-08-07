
import logging

log = logging.getLogger(__name__)
from base import *

from google.appengine.ext import ndb

class DataPoints(ndb.Model):
    data=ndb.StringProperty(repeated=True)
    created = ndb.DateTimeProperty(default=datetime.now())

# class PlotSentiment(ndb.Model):
#     sentiment=ndb.FloatProperty(repeat=true)
#     date=ndb.StringProperty(repeat=true)
class MainHandler(BaseHandler):
    def get(self):
        self.render_template('index.template')


class ResultHandler(BaseHandler):
    def get(self):
        self.redirect(self.uri_for('home'))
    def post(self):
        api.update_status(status=self.request.get('message')+" "+self.request.get('person'))
        self.redirect("https://twitter.com/MLH_Confessions")
class TrendsHandler(BaseHandler):
    def get(self):
        self.redirect(self.uri_for('home'))
class CronTask(BaseHandler):
    def get(self):
        tweets= ['hi','how']
        data=DataPoints(data=tweets)
        data.put
        # for status in tweepy.Cursor(api.user_timeline).items():
        #     # process status here
        #     tweets.append(status._json['text'])
        #     if len(tweets)>10:
        #         tweets.pop()

#
# class Sentiment(BaseHandler):
#     data = PlotSentiment.query().fetch()
