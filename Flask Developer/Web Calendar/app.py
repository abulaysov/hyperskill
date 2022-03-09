from flask import Flask, jsonify, request, abort
import sys
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal_with
import re
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calendar.db'


class Calendar(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


resource_fields = {
    'id': fields.Integer,
    'event': fields.String,
    'date': fields.DateTime(dt_format='iso8601')}


parser.add_argument('event', type=str, help='The event name is required!', required=True)
parser.add_argument('date', type=inputs.date,
                    help='The event date with the correct format is required! The correct format is YYYY-MM-DD!',
                    required=True)


class Event(Resource):
    def post(self):
        args = parser.parse_args()
        if not args.get('date', False) or not re.match(r'\d\d\d\d-\d\d-\d\d', str(args['date'])):
            return None
        if not args.get('event', False):
            return None
        db.session.add(Calendar(event=args['event'], date=args['date']))
        db.session.commit()
        args['message'] = 'The event has been added!'
        args['date'] = str(args['date'])[:10]
        return jsonify(args)

    @marshal_with(resource_fields)
    def get(self):
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')
        if start_time and end_time:
            return Calendar.query.filter(Calendar.date.between(start_time, end_time)).all()
        return Calendar.query.all()


class EventToday(Resource):
    @marshal_with(resource_fields)
    def get(self):
        return Calendar.query.filter(Calendar.date == datetime.date.today()).all()


class EventByID(Resource):
    @marshal_with(resource_fields)
    def get(self, event_id):
        e = Calendar.query.filter(Calendar.id == event_id).first()
        if e:
            return e
        return abort(404, "The event doesn't exist!")

    def delete(self, event_id):
        event = Calendar.query.filter(Calendar.id == event_id).first()
        if event:
            db.session.delete(event)
            db.session.commit()
            return jsonify({"message": "The event has been deleted!"})
        return abort(404, "The event doesn't exist!")


api.add_resource(Event, '/event')
api.add_resource(EventToday, '/event/today')
api.add_resource(EventByID, '/event/<int:event_id>')
db.create_all()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
