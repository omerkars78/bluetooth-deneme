import asyncio
from uuid import UUID
import json 
from construct import Array, Byte, Const, Int8sl, Int16ub, Struct
from construct.core import ConstError

from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
class UUIDEncoder(json.JSONEncoder):
    def default(self, uuid):
        if isinstance(uuid, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return uuid.hex
        return json.JSONEncoder.default(self, uuid)
class Beacons():

    def __init__(self):
        self.ibeacon_format = Struct(
                                        "type_length" / Const(b"\x02\x15"),
                                        "uuid" / Array(16, Byte),
                                        "major" / Int16ub,
                                        "minor" / Int16ub,
                                        "power" / Int8sl,
                                    )
        self.device = BLEDevice
        self.advertisement_data = AdvertisementData
        self.macadress = self.device.address 
    
    def get_beacons(self, device: BLEDevice, advertisement_data: AdvertisementData):
            
            ibeacon_format = Struct(
                                        "type_length" / Const(b"\x02\x15"),
                                        "uuid" / Array(16, Byte),
                                        "major" / Int16ub,
                                        "minor" / Int16ub,
                                        "power" / Int8sl,
                                    )
            
        
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
                    return print(beacons)
            
            except KeyError:
            # Apple company ID (0x004c) not found
                pass
            except ConstError:
            # No iBeacon (type 0x02 and length 0x15)
                pass

device = Beacons()
device.get_beacons(device,device.advertisement_data)