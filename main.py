#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
from google.appengine.ext import ndb

### HTML
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

### HTML end

#class MainHandler(webapp2.RequestHandler):
#def get(self):
#self.response.write('neat nimbus!')

class UserData(ndb.Model):
    u_name = ndb.StringProperty()
    u_date = ndb.TimeProperty(auto_now_add=True)

class SingerData(ndb.Model):
    s_name = ndb.StringProperty()
    s_date = ndb.TimeProperty(auto_now_add=True)

class MainHandler(BaseHandler):
    def get(self):
        users = UserData.query().order(-UserData.u_date).fetch(10)
        singers = SingerData.query().order(-SingerData.s_date).fetch(10)
        values = { 'users':users,'singers':singers}
        self.render('main.html',values)

class GetHandler(BaseHandler):
    def get(self):
        self.render('get.html')
    def post(self):
        name = self.request.get('name')
        if name is None:
            self.redirect('/')
        user = UserData()
        user.u_name = name
        user.put()
        self.redirect('/get')
 
class SongHandler(BaseHandler):
    def get(self):
        self.render('song.html')
    def post(self):
        name = self.request.get('name')
        if name is None:
            self.redirect('/')
        singer = SingerData()
        singer.s_name = name
        singer.put()
        self.redirect('/song')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/get',GetHandler),
    ('/song',SongHandler)
], debug=True)
