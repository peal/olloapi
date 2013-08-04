from google.appengine.ext import ndb

class Token(ndb.Model):
    facebook_id = ndb.IntegerProperty()
    facebook_access_token = ndb.StringProperty()
    access_token = ndb.StringProperty()

class Location(ndb.Model):
    longitude = ndb.FloatProperty()
    latitude = ndb.FloatProperty()
    message = ndb.TextProperty()
    create_time = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    facebook_id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    photo = ndb.StringProperty()
    location = ndb.StructuredProperty(Location)
    friends = ndb.JsonProperty()
