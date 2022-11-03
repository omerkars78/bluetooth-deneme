from flask import Flask
import asyncio
from uuid import UUID



from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/3000')
# ‘/’ URL is bound with hello_world() function.


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



if __name__ == "__main__":
    asyncio.run(main())
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()