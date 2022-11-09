from flask import Flask
# from becaon import minor 
app = Flask(__name__)

from bleak import BleakScanner
import asyncio 
@app.route("/")



async def main():
    print("scanning for 5 seconds, please wait...")

    devices = await BleakScanner.discover(return_adv=True)
        
    for d, a in devices.values():
        return d,a
        
if __name__ == "__main__":
    asyncio.run(main())