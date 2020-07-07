from flask import Flask, render_template, request

from methods import elevation, terrain

app = Flask(__name__)


@app.route('/elevation', methods=['GET'])
def wkt_elevation():
    return elevation.add_elevation(request.args['wkt'])


@app.route('/terrain', methods=['GET'])
def wkt_terrain():
    if request.method == 'GET':
        return terrain.get_pic()
    return 'Error'


@app.route('/')
@app.route('/about')
@app.route('/ReadMe')
def read_me():
    return render_template("ReadMe.html")


if __name__ == "__main__":
    app.run(debug=True)

