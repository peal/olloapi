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
#import auth

class Base(webapp2.RequestHandler):
    def options(self):
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, OPTIONS, DELETE'
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

class Pong(Base):
    def get(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.content_type = 'application/json'
        self.response.write(json.encode('pong'))

app = webapp2.WSGIApplication([
        ('/ping', Pong),
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
