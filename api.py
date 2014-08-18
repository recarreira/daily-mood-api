from models.mood import Mood

import cherrypy
import json

class DailyMood(object):
    exposed = True

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return "Hello World"

    def POST(self, level):
        mood = Mood.create(level=level)

    #@todo: list all moods, filter with params.
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json')],
        }
    }
    cherrypy.quickstart(DailyMood(), '/', conf)
