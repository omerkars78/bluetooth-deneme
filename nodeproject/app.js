



var bluetooth=  require('bluetooth');

bluetooth.on('discover', function(bluetoothDevice) {
    console.log('Found device: ' + bluetoothDevice.address);
    console.log('Name: ' + bluetoothDevice.name);
    console.log('Class: ' + bluetoothDevice.class);
    console.log('RSSI: ' + bluetoothDevice.rssi);
    console.log('Connectable: ' + bluetoothDevice.connectable);
    console.log('UUIDs: ' + bluetoothDevice.uuids);
	console.log('Data: ' + bluetoothDevice.data);
});

bluetooth.startScanning();

// // function createAddItemWindow() {

// //     // Create a new window
// //     addItemWindown = new BrowserWindow({
// //         width: 300,
// //         height: 200,
// //         title: 'Add Item',

// //         // The lines below solved the issue
// //         webPreferences: {
// //             nodeIntegration: true,
// //             contextIsolation: false
// //         }
// // })}

// // createAddItemWindow();
// import bluetooth from 'node-bluetooth';
// const bluetooth = require('node-bluetooth');

// // create bluetooth device instance
// const device = new bluetooth.DeviceINQ();
 
// device.listPairedDevices(console.log);

// // // search for bluetooth devices
// device.on('finished', console.log.bind(console, 'finished'));
// device.on('found', function found(address, name) {
//     console.log('Found: ' + address + ' with name ' + name);
//     device.findSerialPortChannel(address, function(channel) {
//         console.log('Found RFCOMM channel for serial port on %s: ', name, channel);
//     });
// });

// device.scan();