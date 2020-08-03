from flask import Flask, request, make_response
from flask_cors import CORS
import json
from utils import BAD_REQUEST_ERROR, ZERO_VALUE_ERROR

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Welcome, API server working fine."


@app.route("/calculate_bmi", methods=['POST'])
def calculate_bmi():
    request_data = request.get_json()
    if 'weight' not in request_data or 'height' not in request_data:
        return json_response({'message': BAD_REQUEST_ERROR}, 400)
    try:
        height: float = float(request_data['height'])
        weight: float = float(request_data['weight'])
    except ValueError as e:
        return json_response({'message': str(e)}, 400)
    if height <= 0:
        return json_response({'message': ZERO_VALUE_ERROR}, 400)
    bmi_value: float = round(weight/(height*height), 5)
    return json_response({'bmi': str(bmi_value)}, 200)


def json_response(data, status_code):
    response = make_response(json.dumps(data), status_code)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
