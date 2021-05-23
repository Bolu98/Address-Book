import React, {useState, useEffect} from 'react';
import './App.css';

function App() {
  const [initialMessage, setInitialMessage] = useState([])

  useEffect(()=> {
    fetch('/welcome').then(response => response.json())
    .then(message => setInitialMessage(message))
  }, []);
  return (
    <div className="App">
      <h1>{initialMessage.message}</h1>
    </div>
  );
}

export default App;
