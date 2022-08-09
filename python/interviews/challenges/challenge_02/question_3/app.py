import json
import logging
import os

from flask import Flask, request
from flask import jsonify, make_response
from flask_restx import Api, Resource, fields

from utils.model_tools import get_prediction
logging.basicConfig()
logger = logging.getLogger(__name__)

app = Flask(__name__)

api = Api(app, version='1.0', title='Technical Challenge',
          description='This is a Flask-Restx data service that allows a client to consume APIs related to the Technical Challenge.',
          )

metadata_model = api.model("metadata", [])

input_fields = api.model('input_fields', {
    'data': fields.List(fields.Integer(), description='enter data, comma separated numbers', required=True),
})

with open('utils/artifacts/regression_model_v1.json', 'r') as _f:
    loaded_model = json.load(_f)


@api.route('/<string:querystring>', methods=['POST'])
class Prediction(Resource):
    # NOTE: Asked about authentication error.
    @api.response(200, 'SUCCESSFUL: Predictions successfully loaded.')
    @api.doc(description='Conducting predictions for the data input.')
    @api.expect(input_fields)
    def post(self, querystring):
        try:
            data = request.get_json()['data']
            if not isinstance(data, list) or len(data) == 0:
                return_values = {'status': f'Error: Bad data request.'}
                return make_response(jsonify(return_values), 400)
            # TODO: could be improved by using the if argument in a function for better dynamic
            if querystring == 'stream' and len(data) == 1:
                predictions = get_prediction(model=loaded_model, input_data=data)
            elif querystring == 'batch' and len(data) > 1:
                predictions = get_prediction(model=loaded_model, input_data=data)
            else:
                return_values = {'status': f'Error: Bad url path request or data size.'}
                return make_response(jsonify(return_values), 400)
            return_values = predictions
            return make_response(jsonify(return_values), 200)
        except Exception as e:
            logger.error(f'Error with service: {e}')
            return_values = {
                'status': 'Error with service',
                'error': str(e)
            }
            return make_response(jsonify(return_values), 500)


if __name__ == "__main__":
    port = int(os.getenv('PORT', default=8080))
    app.run(debug=False, host='0.0.0.0', port=port, threaded=True)
