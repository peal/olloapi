# encoding: utf-8
from urllib2 import urlopen
from webapp2_extras import json

def get_user(facebook_access_token):
    g = Graph(facebook_access_token)
    user_data = g._get_user()
    profile_picture_data = g._get_profile_picture()
    friends = g._get_friends()
    return {
        'name': user_data['name'],
        'facebook_id': long(user_data['id']),
        'photo': profile_picture_data['data']['url'],
        'friends': [long(f['id']) for f in friends.get('data', [])],
    }

def _try_to_get_result(URL, token):
    try:
        return urlopen(URL.format(token)).read()
    except:
        return None

class Graph(object):

    def __init__(self, facebook_access_token):
        self.token = facebook_access_token

    def _get_result(self, URL, MAX_RETRIES=5):
        result = None
        retries = 0
        while not result and retries <= MAX_RETRIES:
            result = _try_to_get_result(URL, self.token)
            retries += 1
        return json.decode(result)

    def _get_user(self):
        URL = 'https://graph.facebook.com/me?access_token={}'
        return self._get_result(URL)

    def _get_profile_picture(self):
        URL = 'https://graph.facebook.com/me/picture?access_token={}&redirect=false'
        return self._get_result(URL)

    def _get_friends(self):
        URL = 'https://graph.facebook.com/me/friends?access_token={}'
        return self._get_result(URL)

