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

      userAnswer[q1, q2, q3, q4, q5, q6]

      userans.count(a)
      userans.count(b)

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

class QuizAnswers(webapp2.RequestHandler):
    def post(self):
        counta=0
        countb=0
        countc=0
        countd=0
        counte=0
        countf=0
        q1 = self.request.get ('q1')
        if q1 == 'a':
            countb += 1
        if q1 == 'b':
            countb -= 1
            countc += 1
        if q1 == 'c':
            countc -= 1
            countd += 1
            counte += 1
        if q1 == 'd':
            countd -= 1
            countf += 1
        print('q1='+q1)
        q2 = self.request.get ('q2')
        if q2 == 'a':
            countb += 1
            countc += 1
        if q2 == 'b':
            countb -= 1
            countd += 1
            counte += 1
            countf += 1
        print('q2='+q2)
        q3 = self.request.get ('q3')
        print('q3='+q3)
        if q3 == 'a':
            countb += 1
            countc += 1
        if q3 == 'b':
            countb -= 1
            countd += 1
            counte += 1
            countf += 1
        if q3 == 'c':
            counta += 1
            countb += 1
            countd += 1
            counte += 1
            countf += 1

        q4 = self.request.get ('q4')
        if q4 == 'a':
            countb += 1
            countc += 1
        if q4 == 'b':
            countd += 1
            counte += 1
            countb -= 1
        if q4 == 'c':
            countf += 1
        print('q4='+q4)

        q5 = self.request.get ('q5')
        print('q5='+q5)
        q6 = self.request.get ('q6')
        if q3 == 'a':
            countb += 1
            countc += 1
        if q3 == 'b':
            countb -= 1
            countd += 1
            counte += 1
            countf += 1
        if q3 == 'c':
            counta += 1
            countb += 1
            countd += 1
            counte += 1
            countf += 1

        print('q6='+q6)

        userAnswer=[q1, q2, q3, q4, q5, q6]
        print(userAnswer)
        print (len(userAnswer))
        print(userAnswer.count('a'))
        print(userAnswer.count('b'))
        print(userAnswer.count('c'))
        print(userAnswer.count('d'))
        print(userAnswer.count('e'))
        print(userAnswer.count('f'))
        counta = counta + userAnswer.count('a')
        countb = countb + userAnswer.count('b')
        countc = countc + userAnswer.count('c')
        countd = countd + userAnswer.count('d')
        counte = counte + userAnswer.count('e')
        countf = countf + userAnswer.count('f')

        if counta > (countb or countc or countd or counte or countf):
            print('you have 3a hair')

        elif countb > (counta or countc or countd or counte or countf):
            print('You have 3b hair')

        elif countc > (counta or countb or countd or counte or countf):
            print('You have 3c hair')

        elif countd > (counta or countb or countc or counte or countf):
            print('You have 4a hair')

        elif counte > (counta or countb or countc or countd or countf):
            print('You have 4b hair')

        elif countf > (counta or countb or countc or countd or counte):
            print('You have 4c hair')


        elif counta == countb and counta > (countc or countd or counte or countf):
            print('You have 3a hair.')

        elif countb == countc and countb > (counta or countd or counte or countf):
            print('You have 3b hair.')

        elif countc == countd and countc > (counta or countb or counte or countf):
            print('You have 3c hair.')

        elif countd == counte and countd > (counta or countb or countc or countf):
            print('You have 4a hair.')

        elif counte == countf and counte > (counta or countb or countc or countd):
            print('You have 4b hair.')
        else:
            print('Error, Try Again!')

    def get(self):
        self.response.out.write('<doc><body>xxxxx</body></doc>')

class Guestbook(webapp2.RequestHandler):
    def post(self):
        print('Hello World')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Login', Guestbook),
    ('/quiz', QuizHandler),
    ('/results', QuizAnswers)

], debug=True)
