from datetime import datetime
def location(latitude, longitude, message):
    return {
        'latitude': float(latitude),
        'longitude': float(longitude),
        'message': message,
    }

def location_out(l):
    location_dict = location(latitude=l.latitude, longitude=l.longitude, message=l.message)
    age = (datetime.now() - l.create_time).seconds
    location_dict.update({'age': age})
    return location_dict

def user(token, user):
    location = location_out(user.location) if user.location else None
    return {
        'access_token': token.access_token,
        'user': {
            'id': user.facebook_id,
            'name': user.name,
            'photo': user.photo,
            'location': location,
            'friends': user.friends,
        }
    }
