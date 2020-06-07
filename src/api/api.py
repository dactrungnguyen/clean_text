from flask import Flask, request
from flask_restplus import Api, fields, reqparse, Resource
from werkzeug.datastructures import FileStorage

from src.back.worker import clean_text

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return 'Welcome to Clean Text service!'


parser = reqparse.RequestParser()
parser.add_argument('file', type=FileStorage, location='files')

output_model = api.model('Output', {
    'clean_text': fields.String,
})

@api.route('/clean')
@api.expect(parser)
class Clean(Resource):
    @api.marshal_with(output_model)
    def post(self):
        args = parser.parse_args()
        uploaded = args['file']
        input_text = '' if uploaded is None else uploaded.stream.read().decode()
        return {'clean_text': clean_text(input_text)}
