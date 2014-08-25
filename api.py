from models.mood import Mood
from serializer import MoodSerializer

from flask import Flask, request, jsonify
from flask.ext.restful import reqparse, abort, Api, Resource

import datetime


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('level', type=str)


class RootHandler(Resource):

    def get(self):
        return 'Hello World.'


class MoodHandler(Resource):

    def get(self):
        args = parser.parse_args()
        if args['level']:
            moods = Mood.select().where(Mood.level == args['level'])
        else:
            moods = Mood.select()
        serialized = MoodSerializer(list(moods), many=True)
        return jsonify({"moods": serialized.data})

    def post(self):
        args = parser.parse_args()
        mood = Mood.create(level=args['level'])
        serialized = MoodSerializer(mood)
        return jsonify(serialized.data)


class MoodDateHandler(Resource):

    def get(self, year, month, day):
        moods = Mood.select().where(Mood.created.between(
            datetime.date(year, month, day),
            datetime.date(year, month, day) + datetime.timedelta(days=1)))
        serialized = MoodSerializer(list(moods), many=True)
        return jsonify({"moods": serialized.data})


api.add_resource(RootHandler, '/', '/docs')
api.add_resource(MoodDateHandler, '/api/v1/moods/<int:year>/<int:month>/<int:day>', '/api/v1/moods/<int:year>/<int:month>/<int:day>/')
api.add_resource(MoodHandler, '/api/v1/moods', '/api/v1/moods/')


if __name__ == '__main__':
    app.run(debug=True)
