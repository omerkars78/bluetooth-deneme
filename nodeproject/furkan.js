// function handleBluetoothDevice(){navigator.bluetooth.requestDevice({acceptAllDevices: true}).then(data => setDatass(data)) 
// console.log(datass.name)
// console.log(datass.id)
// console.log(datass.gatt)
// }
let device; 
  function handleBluetoothDevice(){
navigator.bluetooth.requestDevice({acceptAllDevices: true})
  .then(data => {
    device = data;
    console.log(device.name);
    console.log(device.id);
    console.log(device.gatt.connect());
  })
  .catch(error => {
    console.error('Error:', error);
  });
  }