// First, let's get a list of all the devices that are visible

navigator.bluetooth.requestDevice({
    acceptAllDevices: true
  }).then(function(device) {
    // Now, let's get more information about each device
    return device.gatt.connect();
  })
  .then(function(server) {
    // Now we can get the detailed bluetooth data
    return server.getPrimaryServices();
  })
//   .then(function(services) {
//     // Now we can loop through each service and get its details
//     for (let i = 0; i < services.length; i++) {
//       let service = services[i];
//       console.log('Service ' + i + ' UUID: ' + service.uuid);
//       console.log('Service ' + i + ' Name: ' + service.name);
//       // We can also get the characteristics of each service
//       service.getCharacteristics().then(function(characteristics) {
//         for (let j = 0; j < characteristics.length; j++) {
//           let characteristic = characteristics[j];
//           console.log(characteristic.uuid);)}



// var bluetooth=  require('bluetooth');

// bluetooth.on('discover', function(bluetoothDevice) {
//     console.log('Found device: ' + bluetoothDevice.address);
//     console.log('Name: ' + bluetoothDevice.name);
//     console.log('Class: ' + bluetoothDevice.class);
//     console.log('RSSI: ' + bluetoothDevice.rssi);
//     console.log('Connectable: ' + bluetoothDevice.connectable);
//     console.log('UUIDs: ' + bluetoothDevice.uuids);
// 	console.log('Data: ' + bluetoothDevice.data);
// });

// bluetooth.startScanning();

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