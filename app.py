from flask import Flask,jsonify
import asyncio
from bleak import BleakScanner
import asyncio
from uuid import UUID
import json
from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
from data2 import beacons

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(beacons)


if __name__ == '__main__':
    app.run()
