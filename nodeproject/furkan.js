// function handleBluetoothDevice(){navigator.bluetooth.requestDevice({acceptAllDevices: true}).then(data => setDatass(data)) 
// console.log(data.name)
// console.log(data.id)
// console.log(data.gatt)
// }
// let device; 
// function handleBluetoothDevice(){
// navigator.bluetooth.requestDevice({acceptAllDevices: true})
//   .then(data => {
//     device = data;
//     console.log(device.name);
//     console.log(device.id);
//     console.log(device.gatt.connect());
//   })
//   .catch(error => {
//     console.error('Error:', error);
//   });
//   }

  // function handleClick() {
    
  //     navigator.bluetooth.requestDevice({acceptAllDevices: true})
  //       .then(data => {
  //         device = data;
  //         console.log(device.name);
  //         console.log(device.id);
  //         console.log(device.gatt.connect());
          
  //       })
  //       .catch(error => {
  //         console.error('Error:', error);
  //       });
 
  // }
  // const button = document.getElementById('mybutton');
  // button.addEventListener('click', handleClick);

  //   function handleClick() {
    
  //     navigator.bluetooth.requestDevice({acceptAllDevices: true})
  //       .then(data => {
  //         device = data;
  //         console.log(device.name);
  //         console.log(device.id);
  //         console.log(device.gatt.connect());
  //         console.log(device.BluetoothRemoteGATTService.getPrimaryService());
          
  //       })
  //       .catch(error => {
  //         console.error('Error:', error);
  //       });
 
  // }
  // const button = document.getElementById('mybutton');
  // button.addEventListener('click', handleClick);

//   function handleClick() {
//     navigator.bluetooth.requestDevice({acceptAllDevices: true})
//       .then(device => {
//         return device.gatt.connect();
//       })
//       .then(server => {
//         return server.getPrimaryServices();
//       })
//       .then(service => {
//         return service.getCharacteristic();
        
//       })
//       .catch(error => {
//         console.error('Error:', error);
//       });
//   }
// const button = document.getElementById('mybutton');
// button.addEventListener('click', handleClick)


// function handleClick() {
//   navigator.bluetooth.requestDevice({acceptAllDevices: true})
//     .then(device => {
//       return device.gatt.connect();
//     })
//     .then(server => {
//       return server.getPrimaryServices("\x02\x15");
//     })
//     .then(service => {
//       return service.getCharacteristic('2a37');
//     })
//     .then(characteristic => {
//       return characteristic.readValue();
//     })
//     .then(value => {
//       const uuid = value.getUint8(0);
//       const rssi = value.getInt8(1);
//       const address = value.getUint8(2);
//       const major = value.getUint16(3);
//       const minor = value.getUint16(5);

//       console.log(`UUID: ${uuid}`);
//       console.log(`RSSI: ${rssi}`);
//       console.log(`Address: ${address}`);
//       console.log(`Major: ${major}`);
//       console.log(`Minor: ${minor}`);
//     })
//     .catch(error => {
//       console.error('Error:', error);
//     });
// }

// const button = document.getElementById('mybutton');
// button.addEventListener('click', handleClick);

async function onButtonClick() {
  let filters = [];

  let filterService = document.querySelector('#service').value;
  if (filterService.startsWith('0x')) {
    filterService = parseInt(filterService);
  }
  if (filterService) {
    filters.push({services: [filterService]});
  }

  let filterName = document.querySelector('#name').value;
  if (filterName) {
    filters.push({name: filterName});
  }

  let filterNamePrefix = document.querySelector('#namePrefix').value;
  if (filterNamePrefix) {
    filters.push({namePrefix: filterNamePrefix});
  }

  let options = {};
  if (document.querySelector('#allDevices').checked) {
    options.acceptAllDevices = true;
  } else {
    options.filters = filters;
  }

  try {
    log('Requesting Bluetooth Device...');
    log('with ' + JSON.stringify(options));
    const device = await navigator.bluetooth.requestDevice(options);

    log('> Name:             ' + device.name);
    log('> Id:               ' + device.id);
    log('> Connected:        ' + device.gatt.connected);
  } catch(error)  {
    log('Argh! ' + error);
  }
}

const button = document.getElementById('mybutton');
button.addEventListener('click', onButtonClick)


// Çevredeki Bluetooth Cihazlarını Listeleme 
// async function populateBluetoothDevices() {
//   const devicesSelect = document.querySelector('#devicesSelect');
//   try {
//     console.log('Getting existing permitted Bluetooth devices...');
//     const devices = await navigator.bluetooth.getDevices();

//     console.log('> Got ' + devices.length + ' Bluetooth devices.');
//     devicesSelect.textContent = '';
//     for (const device of devices) {
//       const option = document.createElement('option');
//       option.value = device.id;
//       option.textContent = device.name;
//       devicesSelect.appendChild(option);
//     }
//   }
//   catch(error) {
//     console.log('Argh! ' + error);
//   }
// }

// async function onRequestBluetoothDeviceButtonClick() {
//   try {
//     console.log('Requesting any Bluetooth device...');
//     const device = await navigator.bluetooth.requestDevice({
//    // filters: [...] <- Prefer filters to save energy & show relevant devices.
//       acceptAllDevices: true
//     });

//    console.log('> Requested ' + device.name + ' (' + device.id + ')');
//     populateBluetoothDevices();
//   }
//   catch(error) {
//     console.log('Argh! ' + error);
//   }
// }

// async function onForgetBluetoothDeviceButtonClick() {
//   try {
//     const devices = await navigator.bluetooth.getDevices();

//     const deviceIdToForget = document.querySelector('#devicesSelect').value;
//     const device = devices.find((device) => device.id == deviceIdToForget);
//     if (!device) {
//       throw new Error('No Bluetooth device to forget');
//     }
//     console.log('Forgetting ' + device.name + 'Bluetooth device...');
//     await device.forget();

//     console.log('  > Bluetooth device has been forgotten.');
//     populateBluetoothDevices();
//   }
//   catch(error) {
//     console.log('Argh! ' + error);
//   }
// }

// window.onload = () => {
//   populateBluetoothDevices();
// };