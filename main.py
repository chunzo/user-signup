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
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASSWORD_RE = re.compile(r'^.{3,20}$')
def valid_password(password):
    return password and PASSWORD_RE.match(password)

EMAIL_RE = re.compile(r'^.{3,20}$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = '''
        <h2>User Signup</h2>
        <form method='post'>
        '''
        username_row = '''
        <p>Username <input type='text' name='username' value=''>
        '''
        password_row = '''
        </p>
        <p>Password <input type='password' name='password' value=''>
        '''
        verify_row = '''
        </p>
        <p>Verify password <input type='password' name='verify' value=''>
        '''
        email_row = '''
        </p>
        <p>Email (optional) <input type='text' name='email' value=''>
        '''
        footer = '''
        </p>
        <input type='submit'>
        </form>
        '''
        content = header + username_row + password_row + verify_row +\
                email_row + footer

        self.response.write(content)

    def post(self):
        header = '''
        <h2>User Signup</h2>
        <form method='post'>
        '''
        username_row = '''
        <p>Username <input type='text' name='username' value=''>
        '''
        password_row = '''
        </p>
        <p>Password <input type='password' name='password' value=''>
        '''
        verify_row = '''
        </p>
        <p>Verify password <input type='password' name='verify' value=''>
        '''
        email_row = '''
        </p>
        <p>Email (optional) <input type='text' name='email' value=''>
        '''
        footer = '''
        </p>
        <input type='submit'>
        </form>
        '''
        username_error = 'That\'s not a valid username'
        password_error = 'That\'s not a valid password'
        verify_error = 'Passwords don\'t match'
        email_error = 'That\'s not a valid email'

        error = 0
        check_username = self.request.get('username')
        check_password = self.request.get('password')
        check_verify = self.request.get('verify')
        check_email = self.request.get('email')
        if not valid_username(check_username):
            username_row += username_error
            error += 1
        else:
            username_row = '''
            <p>Username <input type='text' name='username' value=''' + check_username + '''>
            '''
        if not valid_password(check_password):
            password_row += password_error
            error += 1
        if check_verify != check_password:
            verify_row += verify_error
            error += 1
        if not valid_email(check_email):
            email_row += email_error
            error += 1

        content = header + username_row + password_row + verify_row +\
                email_row + footer
        if error != 0:
            self.response.write(content)
        else:
            self.redirect('/welcome?username=' + check_username)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            content = '''
            <h1>Welcome, ''' + username + '''!</h1>
            '''
            self.response.write(content)
        else:
            self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', Welcome)
], debug=True)
