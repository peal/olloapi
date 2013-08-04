import errors
import models
import random
import string

def get_user_from_token(token):
    facebook_ids = [t.facebook_id for t in models.Token.query(models.Token.access_token == token).fetch(2)]
    if not facebook_ids:
        raise errors.AuthNeeded
    if len(facebook_ids) > 1:
        raise errors.InconsistenState('Found facebook_ids={}'.format(str(facebook_ids)))
    return get_user_from_facebook_id(facebook_ids[0])

def get_user_from_facebook_id(facebook_id):
    users = models.User.query(models.User.facebook_id == facebook_id).fetch(2)
    if not users or len(users) > 1:
        raise errors.InconsistenState('Found users={}'.format(str([u.facebook_id for u in users])))
    return users[0]

def get_users_from_facebook_ids(facebook_ids):
    return [u for u in models.User.query(models.User.facebook_id.IN(facebook_ids))]

def create_token(facebook_id, facebook_access_token, **kwargs):
    access_token = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(64))
    token = models.Token(facebook_id=facebook_id, facebook_access_token=facebook_access_token, access_token=access_token).put()
    return token.get()

def add_friend_to_user(user, friend_id):
    user.friends.append(friend_id)
    #print 'adding friend={} to user={}'.format(friend_id, user.facebook_id)
    user.put()

def get_or_create_user(facebook_id, name, photo, friends):
    try:
        user = get_user_from_facebook_id(facebook_id)
    except (errors.AuthNeeded, errors.InconsistenState):
        users = get_users_from_facebook_ids(friends)
        user_ids = [u.facebook_id for u in users]
        user_key = models.User(facebook_id=facebook_id, name=name, photo=photo, friends=user_ids).put()
        user = user_key.get()
        [add_friend_to_user(u, facebook_id) for u in users]
    return user

def _create_location(latitude, longitude, message=None):
    return models.Location(latitude=latitude, longitude=longitude, message=message)

def update_location(location, user):
    user.location = _create_location(**location)
    user.put()

def reset_all():
    models.ndb.delete_multi([t.key for t in models.Token.query()])
    models.ndb.delete_multi([t.key for t in models.Location.query()])
    models.ndb.delete_multi([t.key for t in models.User.query()])

def get_all():
    print models.ndb.get_multi([t.key for t in models.Token.query()])
    print models.ndb.get_multi([t.key for t in models.Location.query()])
    print models.ndb.get_multi([t.key for t in models.User.query()])
