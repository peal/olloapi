# encoding: utf-8
import webapp2
from webapp2_extras import json
import queries
import errors
import convert
import facebook

class Base(webapp2.RequestHandler):
    def add_headers(self):
        self.response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        self.response.headers['Access-Control-Allow-Origin'] = '*'

    def set_response_data(self):
        self.add_headers()
        self.response.content_type = 'application/json'

    def options(self):
        self.add_headers()
        self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, OPTIONS, DELETE'

    def get_user(self):
        try:
            access_token = self.request.GET['access_token']
            return queries.get_user_from_token(access_token)
        except errors.InconsistenState, e:
            print str(e)
            self.abort(500)
        except Exception, e:
            print str(e)
            self.abort(400)

class Facebook(Base):
    def post(self):
        self.set_response_data()
        params = json.decode(self.request.body)
        facebook_access_token = params.get('facebook_access_token')
        if not facebook_access_token:
            self.abort(code=400)
        facebook_user = facebook.get_user(facebook_access_token)
        user = queries.get_or_create_user(**facebook_user)
        token = queries.create_token(facebook_access_token=facebook_access_token, **facebook_user)
        self.response.write(json.encode(convert.user(token, user)))

class Friends(Base):
    def get(self):
        self.set_response_data()
        user = self.get_user()
        self.response.write(json.encode({
            'friends': user.friends
        }))

class Locations(Base):
    def post(self):
        self.set_response_data()
        user = self.get_user()
        try:
            location = convert.location(**json.decode(self.request.body))
        except Exception, e:
            print str(e)
            self.abort(400)
        queries.update_location(location, user)
        self.response.write(json.encode({}))

class Pong(Base):
    def get(self):
        self.set_response_data()
        self.response.write(json.encode('pong'))

class ResetAll(Base):

    def post(self):
        self.set_response_data()
        queries.reset_all()
        self.response.write(json.encode('ok'))

class GetAll(Base):

    def get(self):
        self.set_response_data()
        queries.get_all()
        self.response.write(json.encode('ok'))

class Dummy(Base):

    def get(self):
        print self.get_user()
        pass

    def post(self):
        queries.create_user(facebook_id='r@mm.com', name='p', photo='', friends='[]')
        t = queries.create_token(facebook_id='r@mm.com', facebook_access_token='fisk')
        print t.get().access_token

#     def post(self):
#         self.set_response_data()
#         d = json.decode(self.request.body)
#         book = models.Book(title=d.get('title'))
#         models.Library(books=book, id=int(d.get('id'))).put()
#         self.response.write(json.encode({}))

#     def get(self):
#         self.set_response_data()
#         ret = [(l.books,l.id) for l in models.Library.query()]
#         self.response.write(json.encode(str(ret)))

#     def delete(self):
#         self.set_response_data()
#         ret = models.ndb.delete_multi([l.key for l in models.Library.query()])
#         self.response.write(json.encode(str(ret)))
