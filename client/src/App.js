import Circle from './components/Circle';
import SelectMenu from './components/SelectMenu';
import Header from './components/Header';
function App() {
  return (
    <div className="flex flex-col bg-[#307BFE] w-full h-screen justify-between">
      <Header/>
      <Circle/>
      <SelectMenu/>
    </div>
  );
}

export default App;
