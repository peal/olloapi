# encoding: utf-8
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
from webapp2_extras import json

class Base(webapp2.RequestHandler):

    def options(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, OPTIONS, DELETE'

class Pong(Base):
    def get(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.content_type = 'application/json'
        self.response.write(json.encode('pong'))

class Facebook(Base):
    def post(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.content_type = 'application/json'
        self.response.write(json.encode({
            'access_token': 'FISK123',
            'user': {
                'id': '42',
                'name': u'Öl La',
                'photo': 'http://i.imgur.com/hrjGuN3.png',
                'location': {
                    'latitude': 40.689060,
                    'longitude': 74.044636,
                    'message': u'Hölla!',
                    'age': 4
                }
            }
        }))

class Friends(Base):
    def get(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.content_type = 'application/json'
        self.response.write(json.encode({
            'friends': [{
                'user': {
                    'id': '43',
                    'name': u'Ål La',
                    'photo': 'http://i.imgur.com/hrjGuN3.png',
                    'location': {
                        'latitude': 40.689068,
                        'longitude': 74.044625,
                        'message': u'Hollå!',
                        'age': 1
                    }
                }
            }]
        }))

class Locations(Base):
    def post(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.content_type = 'application/json'
        self.response.write(json.encode({}))

app = webapp2.WSGIApplication([
        ('/auth/facebook', Facebook),
        ('/friends', Friends),
        ('/locations', Locations),
        ('/ping', Pong),
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
