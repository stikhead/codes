import { useState } from 'react';
import './App.css'
function App() {
  const [counter, setCounter ] = useState(15);
 
  const increaseValue = () => {
    
    let c = counter;
    c++;
    if(c>20){
      console.log(`value cannot be more than 20: ${counter}`)
      setCounter(20);
    } else {

      setCounter(c);
      console.log(`increased value ${counter}`)
    } 
  }

    const decreaseValue = () => {
    if(counter - 1 < 0){
      console.log(`value cannot be negative: ${counter}`)
      setCounter(0);
    } else {
      console.log(`decreased value ${counter}`)
      
      setCounter(counter - 1);
    }
  }
  return (
    <>
      <h1>whoops</h1>
      <h2> counter value: {counter}</h2>
      <button
      onClick={increaseValue}>increase  {counter}</button>
      <br></br>
      <button
      onClick={decreaseValue}>decrease  {counter}</button>
    </>
  )
}

export default App
