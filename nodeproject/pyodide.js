// async function main(){
//     let pyodide = await loadPyodide();
//     await pyodide.runPythonAsync(`
//     from pyodide.http import pyfetch
//     response = await pyfetch("beacon.py")
//     with open("beacon.py", "wb") as f:
//         f.write(await response.bytes())
// `)
// pyodide.loadPackage(['construct']).then(() => {
//     // construct modülü yüklendiğinde burada bulunan kodlar çalıştırılacak
// });
// pkg = pyodide.pyimport("beacon");
// pkg.do_something();
// }
// main();

async function main(){
    let pyodide = await loadPyodide();
    await pyodide.runPythonAsync(`
    from pyodide.http import pyfetch
    response = await pyfetch("beacon.py")
    with open("beacon.py", "wb") as f:
        f.write(await response.bytes())
`)
pkg = pyodide.pyimport("beacon");
pkg.do_something();
}
main();