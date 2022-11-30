import {useState, useEffect} from 'react'
import Circle from './components/Circle';
import SelectMenu from './components/SelectMenu';
import Header from './components/Header';


function App() {
  const [data, setData] = useState([])
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://127.0.0.1:5000/get_bluetooth');
      const data = await response.json();
      setData(data);
    }
    fetchData();
  }, []);
  return (
    <div className="flex flex-col bg-[#69e521] w-full h-screen justify-between">
      {/* <Header/>
      <Circle/>
      <SelectMenu/> */}
      {data}
    </div>
  );
}
// bg-[#307BFE]
export default App;
