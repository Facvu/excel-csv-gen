from flask import Flask, make_response, request
from flask_restful import Api
from excel import bp

app = Flask(__name__)
api = Api(app)
port = 99
host = "0.0.0.0"
app.register_blueprint(bp)

if __name__ == '__main__':
    try:
        print(port, host)
        app.run(host="0.0.0.0", debug=False, port=99)
    except Exception as ex:
        print(ex)
