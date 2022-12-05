// First, let's get a list of all the devices that are visible
document.getElementById("mybutton").addEventListener("click", function() {
  navigator.bluetooth.requestDevice({
    acceptAllDevices: true
   } )}.then(
function(services) {
  // Now we can loop through each service and get its details
  for (let i = 0; i < services.length; i++) {
    let service = services[i];
    console.log('Service ' + i + ' UUID: ' + service.uuid);
    console.log('Service ' + i + ' Name: ' + service.name);
    console.log('Service ' + i + ' Name: ' + service.device.name);
    console.log('Service ' + i + ' Name: ' + service.rssi);
    // We can also get the characteristics of each service
    service.getCharacteristics()}}).then(function(characteristics) {
      
      for (let j = 0; j < characteristics.length; j++)
       {
        let characteristic = characteristics[j];
        console.log(characteristic.uuid);}
        }).then(function(device) {
    // Now, let's get more information about each device
    return device.gatt.connect();
  }))
  .then(function(server) {
    // Now we can get the detailed bluetooth data
    return server.getPrimaryServices();
  })

