from sqlite3 import connect
from uuid import uuid4

from flask import Flask, request
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.datastructures import FileStorage

from src.back.lib import clean_text
from src.lib.config import DB_PATH

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False
api = Api(app)


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return 'Welcome to Clean Text service!'


text_post_parser = reqparse.RequestParser()
text_post_parser.add_argument('file', type=FileStorage, location='files')

run_model = api.model('run', {
    'id': fields.String,
    'input': fields.String,
    'output': fields.String,
    'state': fields.String,
})
run_list_model = api.model('run_list', {
    'runs': fields.List(fields.Nested(run_model)),
})

@api.route('/runs')
class AllRuns(Resource):
    @api.marshal_with(run_list_model)
    def get(self):
        with connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute((
                'SELECT r.id, r.state, r.input, r.output FROM runs AS r '
            ))
            runs = cursor.fetchall()
        return {'runs': [
            {
                'id': run[0],
                'state': run[1],
                'input': run[2],
                'output': run[3],
            } for run in runs
        ]}

    @api.expect(text_post_parser)
    @api.marshal_with(run_model)
    def post(self):
        args = text_post_parser.parse_args()
        uploaded = args['file']
        input_text = '' if uploaded is None else uploaded.stream.read().decode()
        run_id = str(uuid4())
        with connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute((
                'INSERT INTO runs (id, state, input, output) '
                'VALUES (?, ?, ?, ?)'
            ), (run_id, 'SUBMITTED', input_text, None))

        return {'id': run_id, 'state': 'SUBMITTED', 'input': input_text, 'output': None}


@api.route('/runs/<run_id>')
class RunResource(Resource):
    @api.marshal_with(run_model)
    def get(self, run_id: str):
        with connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute((
                'SELECT r.id, r.state, r.input, r.output FROM runs AS r '
                f'WHERE r.id = "{run_id}"'
            ))
            runs = cursor.fetchall()
        assert len(runs) == 1
        run = runs[0]
        return {
            'id': run[0],
            'state': run[1],
            'input': run[2],
            'output': run[3],
        }
