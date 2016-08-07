#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *

#This is the place where all of your URL mapping goes
route_list = [
    webapp2.Route('/', MainHandler, name='home'),
    webapp2.Route('/tweet', ResultHandler, name='results'),
    webapp2.Route('/trends', TrendsHandler, name='trend'),
    webapp2.Route('/admin21183030782147', AdminHandler, name='admin'),
    # webapp2.Route('/sentiment', Sentiment)
]
