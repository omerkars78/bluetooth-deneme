import asyncio
from uuid import UUID
import json 
from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData


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
def device_found(
    device: BLEDevice, advertisement_data: AdvertisementData
):
    """Decode iBeacon."""
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
        rssi = int(rssi)

        # beacons = { 
        #     "Mac Adress" : macadress,
        #     "Local Name" : name ,
        #     "UUID":uuid,
        #     "Major":major,
        #     "Minor":minor,
        #     "TX Power":power,
        #     "RSSI":rssi
        # } 

        print(f"Mac Adress : {macadress}")
        print(f"Local Name : {name}")
        print(f"UUID     : {uuid}")
        print(f"Major    : {major}")
        print(f"Minor    : {minor}")
        print(f"TX power : {power} dBm")
        print(f"RSSI     : {rssi} dBm")
        print(47 * "-") 
                
    except KeyError:
        pass
    except ConstError:
        pass

async def main():
    """Scan for devices."""
    scanner = BleakScanner()
    scanner.register_detection_callback(device_found)

    
    while (True):
        await scanner.start()
        await asyncio.sleep(0.5)
        await scanner.stop()
        
asyncio.run(main())
