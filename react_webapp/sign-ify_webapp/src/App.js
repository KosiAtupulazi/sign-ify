import React from 'react';
import './App.css';

function App() {
  
  const buttonEvent1 = () => {
    alert('button');
  };

  return (
    <div className="app">
      <h1>Sign-ify</h1>
      <button onClick={buttonEvent1}>Open App</button>
    </div>
  );
}

export default App;