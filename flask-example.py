# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import asyncio
from uuid import UUID

from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.



def device_found(
    device: BLEDevice, advertisement_data: AdvertisementData
):
    """Decode iBeacon."""
    ibeacon_format = Struct(
    "type_length" / Const(b"\x02\x15"),
    "uuid" / Array(16, Byte),
    "major" / Int16ub,
    "minor" / Int16ub,
    "power" / Int8sl,
)
    try:
        macadress = device.address
        name = advertisement_data.local_name
        apple_data = advertisement_data.manufacturer_data[0x004C]
        ibeacon = ibeacon_format.parse(apple_data)
        uuid = UUID(bytes=bytes(ibeacon.uuid))
        minor = ibeacon.minor 
        major = ibeacon.major 
        power = ibeacon.power
        rssi = device.rssi
        print(47 * "-")
        list_1 = [macadress,name,uuid,major,minor,power,rssi]
        print(list_1)
    except KeyError:
        # Apple company ID (0x004c) not found
        pass
    except ConstError:
        # No iBeacon (type 0x02 and length 0x15)
        pass



async def main():
    """Scan for devices."""
    scanner = BleakScanner()
    scanner.register_detection_callback(device_found)


    while True:
        await scanner.start()
        await asyncio.sleep(0.1)
        await scanner.stop()
        
asyncio.run(main())
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()