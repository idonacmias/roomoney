import logo from './logo.svg';
import './App.css';



import FunctionDiv from './div.js';
import ClassDiv from './ClassDiv.js';

function App(props) {
  const num2 = 6
  var num3 = 1.1
  const num4 = num2 + num3
  num3 = 10 + num4
  name = {name}
  return (
    <>
      <h1>{%name%}</h1>
      <FunctionDiv num2={num2} num3={num3} num4={num4}/>
      <ClassDiv num={num2}/>
    </>
  );  
}

export default App;
