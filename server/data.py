# aldığın verileri json olarak kaydet. 
# uygulama her çalıştığında yeni bir json dosyası oluşsun.
import asyncio
from bleak import BleakScanner
import json
# from bleak import BaseBleakScanner

async def main():
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(return_adv=True)

    for d, a in devices.values():
        print()
        print(d)                    # beacon names are POI
        print("-" * len(str(d)))
        print(a)
    print(devices.keys())

    with open("data.json","w") as file:
       json.dump(devices,file)

if __name__ == "__main__":
    asyncio.run(main())

    