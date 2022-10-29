# import bluetooth

# nearby_devices = bluetooth.discover_devices(lookup_names=True)
# print("Found {} devices.".format(len(nearby_devices)))

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name)) 

import asyncio
from bleak import BleakScanner
# from bleak import BleakClient
from bleak import  BleakGATTCharacteristic
# async def main():
#     devices = await BleakScanner.discover()
#     for d in devices:
#         print(d)

# asyncio.run(main())

# address = "54:91:F5:74:A5:A2:"
# MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"

# async def main_1(address):
#     async with BleakClient(address) as client:
#         model_number = await client.read_gatt_char(MODEL_NBR_UUID)
#         print("Model Number: {0}".format("".join(map(chr, model_number))))

# asyncio.run(main_1(address))

# async def main():
#     devices = await BleakScanner.discover()
#     x = BleakScanner.discovered_devices_and_advertisement_data
#     for d in devices:
#         print(d)
#     for i in x:
#         print(i) 
# asyncio.run(main())

# import asyncio

# from bleak import BleakScanner
# # from bleak import BaseBleakScanner

# async def main():
#     print("scanning for 5 seconds, please wait...")

#     devices = await BleakScanner.discover(return_adv=True)

#     for d, a in devices.values():
#         print()
#         print(d)                    # beacon names are POI
#         print("-" * len(str(d)))
#         print(a)


# if __name__ == "__main__":
#     asyncio.run(main())

# https://bleak.readthedocs.io/en/latest/api/scanner.html#bleak.BleakScanner.discovered_devices_and_advertisement_data
import asyncio

from bleak import BleakScanner
# from bleak import BaseBleakScanner

async def main():
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(return_adv=True)

    # for d, a in devices.values():
    #     print()
    #     print(d)                    # beacon names are POI
    #     print("-" * len(str(d)))
    #     print(a)
    print(devices.keys())



if __name__ == "__main__":
    asyncio.run(main())