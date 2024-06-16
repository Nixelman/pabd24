"""House price prediction service"""
import os
from dotenv import dotenv_values
from flask import Flask, request, url_for
from flask_cors import CORS
from joblib import load
from flask_httpauth import HTTPTokenAuth
from flask import send_from_directory
import time
import numpy as np

# MODEL_SAVE_PATH = 'models/linear_regression_v01.joblib'
MODEL_SAVE_PATH = 'models/GBR.joblib'

app = Flask(__name__)
CORS(app)

config = dotenv_values(".env")
auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    config['APP_TOKEN']: "user20",
}

model = load(MODEL_SAVE_PATH)


# def predict_io_bounded(area):
#     """Emulate io delay"""
#     time.sleep(1)
#     avg_price = 50_000                 # RUB / m2
#     return int(area * avg_price)
#
#
# def predict_cpu_bounded(area, n=10_000_000):
#     """Emulate single thread computation"""
#     avg_price = sum([x for x in range(n)]) / n
#     return int(area * avg_price)
#
#
# def predict_cpu_multithread(area, n=400_000_000):
#     """Emulate multi thread computation"""
#     avg_price = np.mean(np.arange(n))
#     return int(area * avg_price)


@auth.verify_token
def verify_token(token):
    if token in tokens:
        return tokens[token]


def predict(in_data: dict) -> int:
    """ Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    area = float(in_data['total_meters'])
    floor = float(in_data['floor'])
    floors_count = float(in_data['floors_count'])
    rooms_count = float(in_data['rooms_count'])
    price = model.predict([[area, floor, floors_count, rooms_count]])
    # price = predict_cpu_multithread(area)
    return int(price)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route("/")
def home():
    return """
    <html>
    <head>
    <link rel="shortcut icon" href="/favicon.ico">
    </head>
    <body>
    <h1>Housing price service.</h1> Use /predict endpoint
    </body>
    </html>
    """


@app.route("/predict", methods=['POST'])
@auth.login_required
def predict_web_serve():
    """Dummy service"""
    in_data = request.get_json()
    price = predict(in_data)
    return {'price': price}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)