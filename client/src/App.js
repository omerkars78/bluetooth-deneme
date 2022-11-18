import {AiOutlineArrowUp} from 'react-icons/ai'
function App() {
  return (
    <div className="flex flex-col bg-[#307BFE] w-full h-screen justify-between">
          
          <div className="text-center items-center text-white py-10 font-bold text-2xl">{/* Title */}
            <h1 className="">Bina İçi Yönlendirme</h1>
          </div>
          
          <div className="w-full bg-[#307BFE] flex p-4">
          
              <div className=" flex w-full bg-white rounded-15 text-black rounded-full items-center justify-center">
                <div className='text-[350px]'>

                <AiOutlineArrowUp /> 
                </div>
              </div>  
          
          </div>{/* Circle */}
          
          <div className='flex items-center justify-center text-3xl py-10 text-white font-bold'>
            SELECT
          </div>{/* Select Option */}
    </div>
  );
}

export default App;
