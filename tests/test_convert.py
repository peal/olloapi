# encoding: utf-8
import nose.tools as nt
import convert

class TestLocations(object):
    def test(self):
        actual = convert.location(**{
            'latitude': 40.689060,
            'longitude': 74.044636,
            'message': u'Hölla!',
            'age': 4
        })
        nt.assert_equals(actual, {
            'latitude': 40.689060,
            'longitude': 74.044636,
            'message': u'Hölla!',
            'age': 4
        })

