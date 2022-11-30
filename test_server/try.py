import asyncio
from bleak import BleakScanner
# from bleak import BaseBleakScanner

async def main():
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(return_adv=True)

    for d, a in devices.values():
        print()
        print(d)                    # beacon names are POI
        print("-" * len(str(d)))
        print(a)
    # print(devices.keys())



if __name__ == "__main__":
    asyncio.run(main())

    