from flask import Flask
import asyncio
from uuid import UUID
import json 
from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/beacons")

def devices():
    device: BLEDevice
    advertisement_data: AdvertisementData
    macadress = device.address
    name = advertisement_data.local_name
    apple_data = advertisement_data.manufacturer_data[0x004C]
    rssi = device.rssi
    rssi = int(rssi)
    
    beacons = { 
            "Mac Adress" : macadress,
            "Local Name" : name ,
            "RSSI":rssi
            } 
    return "<p>{beacons}</p>" 
     

if __name__ == "__main__":
    app.run()