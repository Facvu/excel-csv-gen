from flask import Flask, make_response, request
from flask_restful import Api
from excel import bp

from test import *

app = Flask(__name__)
api = Api(app)

app.register_blueprint(bp)

if __name__ == '__main__':
    try:
        app.run(debug=False)
    except Exception as ex:
        print(ex)
