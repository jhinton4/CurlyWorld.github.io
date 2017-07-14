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



<div class="container">
    <center><label><b>Username</b></label><center>
    <center><input type="text" placeholder="Enter Username" name="uname" required><center>

    <center><label><b>Email</b></label><center>
    <center><input type="text" placeholder="Enter Email" name="email" required><center>
      <center><label><b>Confirm Email</b></label><center>
      <center><input type="text" placeholder="Confirm Email" name="email" required><center>

    <center><label><b>Password</b></label><center>
    <center><input type="password" placeholder="Enter Password" name="psw" required><center>
      <center><label><b>Confirm Password</b></label><center>
      <center><input type="password" placeholder="Confirm Password" name="psw" required><center>

    <center><button type="submit">Login</button><center>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <center><button type="button" class="cancelbtn">Cancel</button><center>
    </div>
</form>
</html>

''')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/quiz', QuizHandler)
], debug=True)
