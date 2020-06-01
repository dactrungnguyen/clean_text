from flask import Flask, request
from flask_restplus import Api, fields, reqparse, Resource

from src.back.worker import clean_text

app = Flask(__name__)
api = Api(app)

todos = {1: 'Begin'}


@api.route('/hello')
class Hello(Resource):
    def get(self):
        return 'Welcome to Clean Text service!'


parser = reqparse.RequestParser()
parser.add_argument('input_text', type=str)

input_model = api.model('Input', {
    'clean_text': fields.String,
})

@api.route('/clean')
@api.expect(parser)
class Clean(Resource):
    @api.marshal_with(input_model)
    def post(self):
        args = parser.parse_args()
        input_text = args['input_text']
        clean_text = '' if input_text is None else clean_text(input_text)
        return {'clean_text': clean_text}
