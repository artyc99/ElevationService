from flask import Flask, request
import rasterio


app = Flask(__name__)


@app.route('/elevation', methods=['GET'])
def wkt_adding():
    elevetion_file = 'srtm_N55E160.tif'

    with rasterio.open(elevetion_file) as src:
        band1 = src.read(1)
        x, y = (160.002430, 55.000042)
        row, col = src.index(x, y)
        return str(y) + ' ' + str(x) + ' '+ str(band1[row, col])



