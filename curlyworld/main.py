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
<<<<<<< HEAD
import logging

class QuizHandler(webapp2.RequestHandler):
  def get(self):
      self.response.write('''
      Quiz''')

class MainHandler(webapp2.RequestHandler):
  def get(self):
      self.response.write('''
<!DOCTYPE html>
<html>

<head>
  <title> Curly World </title>
</head>


<h1><center> Curly World <center></h1>
=======
import os
>>>>>>> deedf5855d4bfce57ebe0e276ea7c1b815541fc9

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('template/mainpage.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler)
], debug=True)
