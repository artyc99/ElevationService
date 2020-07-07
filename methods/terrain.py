import os
from random import choices
from string import ascii_letters, digits

import gdal
from rio_rgbify.scripts.cli import rgbify

import config


def random_file_name(file_name_length: int, format: str) -> str:

    while True:
        file_name = config.Directoris.BUFFERING_MAPS.value + format + '_' + ''.join(
            choices(ascii_letters + digits, k=file_name_length)) + '.' + format
        if not os.path.isfile(file_name):
            return file_name


def get_gdal_warp(entering_file: str, existing_file: str) -> bool:
    srcNodata = 0

    gdal.Warp(existing_file, entering_file, srcNodata=srcNodata)

    return os.path.isfile(existing_file)


def get_rgbify(entering_file: str, existing_file: str) -> bool:
    interval = 0.1
    base_val = -10000

    rgbify([entering_file,
            existing_file,
            '--interval', interval,
            '--base-val', base_val])

    return os.path.isfile(existing_file)


def get_png(entering_file: str, existing_file: str) -> bool:
    format = 'PNG'

    gdal.Translate(existing_file, entering_file, format=format)

    return os.path.isfile(existing_file)


def deleting_file(path: str) -> bool:

    if os.path.isfile(path):
        os.remove(path)
        return True
    else:
        return False


def get_pic() -> str:

    entering_file = config.Files.MAP.value

    gdal_warp_file = random_file_name(10, 'tif')
    get_gdal_warp(entering_file, gdal_warp_file)

    rgbify_file = random_file_name(10, 'tif')
    try:
        get_rgbify(gdal_warp_file, rgbify_file)
    except:
        pass
    if not deleting_file(gdal_warp_file):
        return 'Error(could not delete ./' + gdal_warp_file + ' )'

    png_file = random_file_name(10, 'png')
    get_png(rgbify_file, png_file)
    if not deleting_file(rgbify_file):
        return 'Error(could not delete ./' + rgbify_file + ' )'
    if not deleting_file(png_file + '.aux.xml'):
        return 'Error(could not delete ./' + png_file + '.aux.xml' + ' )'

    return png_file

