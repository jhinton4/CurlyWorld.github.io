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
from google.appengine.api import users
import jinja2
import webapp2
import logging
import os
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class QuizHandler(webapp2.RequestHandler):
  def get(self):
      self.response.write('''
      Quiz''')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #user = users.get_current_user()
        #if user:
            #nickname = user.nickname()
            #logout_url = users.create_logout_url('/')
            #greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
                #nickname, logout_url)
        #else:
            #login_url = users.create_login_url('/')
            #greeting = '<a href="{}">Sign in</a>'.format(login_url)

        #self.response.write(
            #'<html><body>{}</body></html>'.format(greeting))
        user = 'Chloe'
        email = ''
        email2 = ''
        password = ''
        password2 = ''
        template_values = {
            'uname' : user,
            'email': email,
            'email2': email2,
            'psw': password,
            'psw2': password2,
        }
        template = jinja_environment.get_template('template/mainpage.html')
        self.response.out.write(template.render(template_values))

class QuizHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('template/quiz.html')
        self.response.out.write(template.render())

class Guestbook(webapp2.RequestHandler):
    def post(self):
        print('Hello World')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Login', Guestbook),
    ('/quiz', QuizHandler)
], debug=True)
