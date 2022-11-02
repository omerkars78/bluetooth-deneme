# import bluetooth

# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print("Found {} devices.".format(len(nearby_devices)))

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name)) 

import asyncio
from bleak import BleakScanner
from bleak import BleakClient

from uuid import UUID

from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError


from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
import asyncio

from bleak import BleakScanner
format = Struct(
    "type_length" / Const(b"\x02\x15"),
    "uuid" / Array(16, Byte),
    "major" / Int16ub,
    "minor" / Int16ub,
    "power" / Int8sl,)

def device_found(
    device: BLEDevice, advertisement_data: AdvertisementData
):
    """Decode iBeacon."""
    try:
        macadress = device.address
        name = advertisement_data.local_name
        apple_data = advertisement_data.manufacturer_data[0x004C]
        ibeacon = format.parse(apple_data)
        uuid = UUID(bytes=bytes(ibeacon.uuid))
        minor = ibeacon.minor 
        major = ibeacon.major 
        power = ibeacon.power
        rssi = device.rssi
        print(f"Mac Adress : {macadress}")
        print(f"Local Name : {name}")
        print(f"UUID     : {uuid}")
        print(f"Major    : {major}")
        print(f"Minor    : {minor}")
        print(f"TX power : {power} dBm")
        print(f"RSSI     : {rssi} dBm")
        print(47 * "-")
        # list_1 = [macadress,name,uuid,major,minor,power,rssi]
        # print(list_1)
    except KeyError:
        # Apple company ID (0x004c) not found
        pass
    except ConstError:
        # No iBeacon (type 0x02 and length 0x15)
        pass
    

async def main():
    print("scanning for 5 seconds, please wait...")

    scanner = BleakScanner()
    scanner.register_detection_callback(device_found)
    while (True):
        await scanner.start()
        await asyncio.sleep(15.0)
        await scanner.stop()
    

if __name__ == "__main__":
    asyncio.run(main())


# https://bleak.readthedocs.io/en/latest/api/scanner.html#bleak.BleakScanner.discovered_devices_and_advertisement_data