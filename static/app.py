from flask import Flask
import asyncio
from bleak import BleakScanner

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/beacons")
async def main():

    devices = await BleakScanner.discover(return_adv=True)
    for d, a in devices.values():
        print(a,d)

if __name__ == '__main__':
    app.run(debug=True)
