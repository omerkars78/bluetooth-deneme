import React from 'react'

const SelectMenu = () => {
    return (
        <div className='flex-col items-center'>
            <span className='text-center items-center text-white py-8 font-bold text-l ml-12' >Lütfen Gitmek İstediğiniz Kliniği Seçiniz </span>
            <div className='flex items-center justify-center text-3xl py-10 text-white font-bold'>

                <button id="dropdownDefault" data-dropdown-toggle="dropdown" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800" type="button">Klinik Seçiniz <svg class="ml-2 w-4 h-4" aria-hidden="true" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></button>

                <div id="dropdown" className="hidden z-10 w-44  bg-white rounded divide-y divide-gray-100 shadow dark:bg-gray-700">
                    <ul class="py-1 text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownDefault">
                        <li>
                            <a href="#" className="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Kardiyoloji</a>
                        </li>
                        <li>
                            <a href="#" className="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">KBB</a>
                        </li>
                        <li>
                            <a href="#" className="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Cildiye</a>
                        </li>
                        <li>
                            <a href="#" className="block py-2 px-4 hover:bg-gray-100 dark:hover:bg-gray-600 dark:hover:text-white">Dahiliye</a>
                        </li>
                    </ul>
                </div>

            </div>{/* Select Option */}
        </div>
    )
}

export default SelectMenu
