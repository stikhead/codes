
import { useCallback, useEffect, useRef, useState } from 'react';

function App() {
  const [length, setLength] = useState(9);
  const [numberAllowed, setNumberAllowed] = useState(false);
  const [charAllowed, setcharAllowed] = useState(false);

  const [password, setPassword] = useState('')
  const passRef = useRef(null)

  const copyPassword = useCallback(()=>{
    passRef.current?.select()
    window.navigator.clipboard.writeText(password)
  }, [passRef, password])
  const passwordGenerator = useCallback(() => {
    let pass = ''
    let str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    if (numberAllowed) {
      str += '0123456789'
    }
    if (charAllowed) {
      str += '()[]{}@1|'
    }

    for(let i=1; i<=length; i++){
      pass+=str.charAt(Math.floor(Math.random() * str.length + 1))
    }
    setPassword(pass);

  }, [length, numberAllowed, charAllowed, setPassword]);
  
  useEffect(()=>{
      // eslint-disable-next-line react-hooks/set-state-in-effect
      passwordGenerator()

  },[length, numberAllowed, charAllowed, passwordGenerator])

  return (
   <>
    <div className='w-full max-w-md mx-auto shadow-md rounded-lg px-4 py-3 my-10 bg-gray-600 '>
      <div className='flex shadow rounded-lg overflow-hidden mb-4'>
        <input 
          type='text'
          value={password}
          className='outline-none w-full px-1 py-3 bg-white'
          placeholder='password'
          readOnly
          ref={passRef} />
        <button 
          onClick={copyPassword}
          className='bg-blue-700 text-white px-3 py-2 shrink-0 rounded-lg outline-none'>
          copy
        </button>
      </div>
      <div className='flex text-sm gap-x-3'>
        <div className='flex items-center gap-x-1'>
          <input 
            type="range"   
            min={6}
            max={40}
            value={length}
            className='cursor-pointer accent-blue-700 bg-blue-700'
            onChange={(e)=>{setLength(e.target.value)}}/>
            <label className='text-white'>length: {length}</label>

        <div className='flex items-center gap-x-1'>
          <input 
             type="checkbox" 
             className='accent-blue-700'
             defaultChecked={numberAllowed}
             onChange={() => {setNumberAllowed((prev) => !prev)}}/>
             <label className='text-white'>Numbers</label>
        </div>
        <div className='flex items-center gap-x-1'>
           <input 
             type="checkbox" 
             className='accent-blue-700'
             defaultChecked={charAllowed}
             onChange={() => {setcharAllowed((prev) => !prev)}}/>
             <label className='text-white'>Characters</label>
             </div>
        </div>
        
        <div className='flex items-center gap-x-1'>
           <button 
             onClick={passwordGenerator}
             className='accent-blue-700 text-white te py-2 rounded-lg px-2 bg-blue-700'
             >renew</button>
           
        </div>
      </div>
    </div>
   </>
  )
}

export default App
