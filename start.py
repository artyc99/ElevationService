from flask import Flask
from flask import request

from methods import elevation

app = Flask(__name__)


@app.route('/elevation', methods=['GET'])
def wkt_adding():

    return elevation.add_elevation(request.args['wkt'])




