from main import app

class Test(object):
    def test(self):
        response = app.get_response('/ping')
        assert response.status_int == 200
        assert response.body == '"pong"'
