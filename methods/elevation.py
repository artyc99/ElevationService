import re
import rasterio

import config


def add_elevation(inner_string: str):

    out_index = 0

    out_string = ''

    coordinate_flag = False

    x = []
    y = []

    coordinates = re.findall(r'[0-9]+\.*[0-9]*', inner_string)

    for coordinate in coordinates:
        if coordinate_flag:
            coordinate_flag = False
            y.append([float(coordinate), len(coordinate)])
        else:
            coordinate_flag = True
            x.append([float(coordinate), len(coordinate)])

    for i in range(len(x)):
        in_index = inner_string[out_index:].index(str(int(x[i][0]))) + out_index
        out_string += inner_string[out_index:in_index] \
                      + repr(x[i][0]) \
                      + ' ' \
                      + repr(y[i][0]) \
                      + ' ' \
                      + repr(getting_elevation(x[i][0], y[i][0]))
        out_index = in_index + x[i][1] + y[i][1] +1
    out_string += inner_string[out_index:]

    return out_string


def getting_elevation(x: float, y: float) -> int:

    with rasterio.open(config.Files.MAP.value) as src:
        band1 = src.read(1)
        row, col = src.index(x, y)

    return int(band1[row, col])
