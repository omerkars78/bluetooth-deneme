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
        device_id = 0 
        
        device_list = [
            {
            "Mac Adress" : macadress,
            "Local Name" : name ,
            "UUID":uuid,
            "Major":major,
            "Minor":minor,
            "TX Power":power,
            "RSSI":rssi
            }
        ] 

        list_device = {

            "Mac Adress" : macadress,
            "Local Name" : name ,
            "UUID":uuid,
            "Major":major,
            "Minor":minor,
            "TX Power":power,
            "RSSI":rssi

        }
       
        with open("data.json") as file:
            devices = json.load(file)
        
        devices.append(list_device)   
        with open("data.json","w") as file:
            json.dump(devices,file,ensure_ascii=False,indent=4,skipkeys=True,cls=UUIDEncoder,separators=(",",":"))
            
        

        
       
        
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
    
    

    
    while (True):
        
        await scanner.start()
        await asyncio.sleep(0.5)
        await scanner.stop()
        
asyncio.run(main())
