import { useState } from 'react';
import './App.css'
import { Button } from './components/Button';
function App() {

  const [ color, setColor ] = useState('blue');

  const changeColor = (newColor) => {
    setColor(newColor)
    console.log("changed")
  }
  return (
    <>
     <div
      className="h-screen flex gap-4 items-center justify-center"
      style={{ backgroundColor: color }}
    >
        <Button color='black' c={changeColor}></Button>
        <Button color='green' c={changeColor}></Button>
        <Button color='yellow' c={changeColor}></Button>
        <Button color='white' c={changeColor}></Button>
     </div>
    </>
  )
}

export default App
