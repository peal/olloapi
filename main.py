# encoding: utf-8
#!/usr/bin/env python
#
import webapp2
import routes

app = webapp2.WSGIApplication([
        ('/auth/facebook', routes.Facebook),
        ('/dummy', routes.Dummy),
        ('/friends', routes.Friends),
        ('/locations', routes.Locations),
        ('/ping', routes.Pong),
        ('/get_all', routes.GetAll),
        ('/reset_all', routes.ResetAll),
], debug=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
