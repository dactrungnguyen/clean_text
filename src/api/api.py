import sqlite3
from uuid import uuid4

from flask import Flask, request
from flask_restplus import Api, Resource, fields, reqparse
from werkzeug.datastructures import FileStorage

from src.back.worker import clean_text
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

run_post_response_model = api.model('run_post_response', {
    'id': fields.String,
    'status': fields.String,
})

@api.route('/runs')
@api.expect(text_post_parser)
class RunsResource(Resource):
    @api.marshal_with(run_post_response_model)
    def post(self):
        args = text_post_parser.parse_args()
        uploaded = args['file']
        input_text = '' if uploaded is None else uploaded.stream.read().decode()
        run_id = str(uuid4())
        with sqlite3.connect(DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute((
                'INSERT INTO runs (id, input, output) '
                'VALUES (?, ?, ?)'
            ), (run_id, input_text, None))

        return {'id': run_id, 'status': 'SUBMITTED'}
