import asyncio
from uuid import UUID
from flask import Flask, jsonify
import json
from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

app = Flask(__name__)

ibeacon_format = Struct(
    "type_length" / Const(b"\x02\x15"),
    "uuid" / Array(16, Byte),
    "major" / Int16ub,
    "minor" / Int16ub,
    "power" / Int8sl,
)


class UUIDEncoder(json.JSONEncoder):
    def default(self, uuid):
        if isinstance(uuid, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return uuid.hex
        return json.JSONEncoder.default(self, uuid)


@app.route("/beacons")
def index():
    beacons = []
    # Scan for devices
    scanner = BleakScanner()
    devices = asyncio.run(scanner.discover(timeout=5))
    for device in devices:
        try:
            macadress = device.address
            name = device.name
            if not name:
                continue
            apple_data = device.metadata["manufacturer_data"][0x004C]
            ibeacon = ibeacon_format.parse(apple_data)
            uuid = UUID(bytes=bytes(ibeacon.uuid))
            minor = ibeacon.minor
            major = ibeacon.major
            power = ibeacon.power
            rssi = device.rssi
            rssi = int(rssi)
            beacons.append(
                {
                    "Mac Adress": macadress,
                    "Local Name": name,
                    "UUID": uuid,
                    "Major": major,
                    "Minor": minor,
                    "TX Power": power,
                    "RSSI": rssi,
                }
            )
        except KeyError:
            # Apple company ID (0x004c) not found
            pass
        except ConstError:
            # No iBeacon (type 0x02 and length 0x15)
            pass

    return jsonify(beacons)



if __name__ == "__main__":
    app.run()
