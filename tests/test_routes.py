# encoding: utf-8
import webapp2
from main import app
from webapp2_extras import json

class TestPing(object):
    def test(self):
        request = webapp2.Request.blank('/ping')
        response = request.get_response(app)
        assert response.status_int == 200
        assert response.body == '"pong"'

class TestAuth(object):
    def test_facebook(self):
        request = webapp2.Request.blank('/auth/facebook')
        request.body = '{"facebook_access_token": "FISK123"}'
        request.method = 'POST'
        response = request.get_response(app)
        assert response.status_int == 200
        assert json.decode(response.body) == {
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
        }

class TestFriends(object):
    def test(self):
        request = webapp2.Request.blank('/friends')
        response = request.get_response(app)
        assert response.status_int == 200
        assert json.decode(response.body) == {
            'friends': [{
                'id': '43',
                'name': u'Ål La',
                'photo': 'http://i.imgur.com/hrjGuN3.png',
                'location': {
                    'latitude': 40.689068,
                    'longitude': 74.044625,
                    'message': u'Hollå!',
                    'age': 1
                }
            }]
        }

class TestLocations(object):
    def test(self):
        request = webapp2.Request.blank('/locations')
        request.body = '{"latitude": 40.689068, "longitude": 74.044625, "message": u"Hollå!", "age": 1 }'
        request.method = 'POST'
        response = request.get_response(app)
        assert response.status_int == 200
        assert json.decode(response.body) == {}

