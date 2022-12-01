from flask import Flask
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
app = Flask(__name__)
class UUIDEncoder(json.JSONEncoder):
    def default(self, uuid):
        if isinstance(uuid, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return uuid.hex
        return json.JSONEncoder.default(self, uuid)
ibeacon_format = Struct(
        "type_length" / Const(b"\x02\x15"),
        "uuid" / Array(16, Byte),
        "major" / Int16ub,
        "minor" / Int16ub,
        "power" / Int8sl,
    )
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/beacons")
# async def main():

#     devices = await BleakScanner.discover(return_adv=True)
#     devices = list(devices)
#     # for d, a in devices.values():
#     return devices
@app.route("/beacons")

async def device_found(device: BLEDevice, advertisement_data: AdvertisementData
):
    try:
        name = advertisement_data.local_name
        macadress = device.address
        apple_data = advertisement_data.manufacturer_data[0x004C]
        ibeacon = ibeacon_format.parse(apple_data)
        uuid = UUID(bytes=bytes(ibeacon.uuid))
        minor = ibeacon.minor 
        major = ibeacon.major 
        power = ibeacon.power
        rssi = device.rssi
        rssi = int(rssi)

        beacons = { 
            "Mac Adress" : macadress,
            "Local Name" : name ,
            "UUID":uuid,
            "Major":major,
            "Minor":minor,
            "TX Power":power,
            "RSSI":rssi
        } 
        
        if(beacons["Local Name"]== "POI" and beacons["RSSI"] <= -40 and beacons["RSSI"] >= -80):
            return beacons
            # with open("data.json","a") as file:
            #     json.dump(beacons,file,sort_keys=True,indent=4,skipkeys=True,cls=UUIDEncoder,separators=(",",":"))
        else:
            pass 

    except KeyError:
        # Apple company ID (0x004c) not found
        pass
    except ConstError:
        # No iBeacon (type 0x02 and length 0x15)
        pass
        scanner = BleakScanner()
        scanner.register_detection_callback(device_found)
        async def main():
            """Scan for devices."""
            scanner = BleakScanner()
            scanner.register_detection_callback(device_found)

    
    while (True):
        await scanner.start()
        await asyncio.sleep(0.5)
        await scanner.stop()
        
        asyncio.run(main())
    # while (True):
    #     await scanner.start()
    #     await asyncio.sleep(0.5)
    #     await scanner.stop()


if __name__ == '__main__':
    app.run(host="193.140.27.106", port=5000, debug=True)
