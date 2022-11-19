import React from 'react'
import { AiOutlineArrowUp } from 'react-icons/ai'
import {  BsDot } from 'react-icons/bs'
import { AiOutlineArrowRight } from 'react-icons/ai'
import { AiOutlineArrowLeft } from 'react-icons/ai'
import { AiOutlineClose } from 'react-icons/ai'
import { AiOutlineArrowDown } from 'react-icons/ai'
const circle = () => {
    return (
        <div>

            <div className="w-full bg-[#69e521] flex p-5 ">

                <div className=" flex w-full bg-white rounded-15 text-black rounded-full items-center justify-center">
                    <div className='text-[320px]'>
                        <BsDot/>
                        {/* <AiOutlineArrowUp /> */}
                        {/* <AiOutlineArrowRight /> */}
                        {/* <AiOutlineArrowLeft /> */}
                        {/* <AiOutlineClose/> */}
                        {/* <AiOutlineArrowDown /> */}
                    </div>
                </div>
            
            </div>{/* Circle */}
        </div>
    )
}

export default circle
