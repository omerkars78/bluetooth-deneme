# from flask import Flask
# import asyncio
# from uuid import UUID
# from bleak import BleakScanner
# from bleak.backends.device import BLEDevice
# from bleak.backends.scanner import AdvertisementData
# # Flask constructor takes the name of
# # current module (__name__) as argument.
# app = Flask(__name__)

# @app.route('/')

# async def main():
#     print("scanning for 5 seconds, please wait...")

#     devices = await BleakScanner.discover(return_adv=True)

#     for d, a in devices.values():
#         print()
#         print(d)                    # beacon names are POI
#         print("-" * len(str(d)))
#         print(a)
#     # print(devices.keys())



# if __name__ == "__main__":
#     asyncio.run(main())
 
# if __name__ == '__main__':

#     app.run()
# from uuid import UUID
# from bleak import BleakScanner
# from bleak.backends.device import BLEDevice
# from bleak.backends.scanner import AdvertisementData
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# async def main():
#     return "<h1>Hello!</h1>"

#     devices = await BleakScanner.discover(return_adv=True)

#     for d, a in devices.values():
#         print()
#         print(d)                    # beacon names are POI
#         print("-" * len(str(d)))
#         print(a)
#     # print(devices.keys())

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)

from flask import Flask, request, render_template
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData
# Flask constructor
app = Flask(__name__)  
async def main():

    devices = await BleakScanner.discover(return_adv=True)

    for d, a in devices.values():
        print()
        print(d)                    # beacon names are POI
        print("-" * len(str(d)))
        print(a)
    # print(devices.keys())
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
async def gfg():
    devices = await BleakScanner.discover(return_adv=True)
    adress = devices.values() 
    if request.method == "GET":
    #    # getting input with name = fname in HTML form
       adress = request.get_data("adress")
    #    # getting input with name = lname in HTML form
    #    last_name = request.form.get("lname")
    #    return "Your name is "+first_name + last_name
    
    return adress 
    return render_template("index.html")
 
if __name__=='__main__':
   app.run()    