import React from 'react';

function App() {
  return (
    <div style={{ padding: '40px', fontFamily: 'Arial' }}>
      <h1>🎉 AI DevOps Pipeline Optimizer</h1>
      <h2>✅ Frontend is Running!</h2>
      
      <div style={{ marginTop: '30px', padding: '20px', background: '#f0f0f0', borderRadius: '8px' }}>
        <h3>Quick Links:</h3>
        <ul>
          <li><a href="http://localhost:8000" target="_blank">Backend API</a></li>
          <li><a href="http://localhost:8000/docs" target="_blank">API Documentation</a></li>
        </ul>
      </div>

      <div style={{ marginTop: '30px', padding: '20px', background: '#e3f2fd', borderRadius: '8px' }}>
        <h3>✅ Status:</h3>
        <p>✅ React is working</p>
        <p>✅ Vite dev server is running</p>
        <p>✅ Frontend is accessible at http://localhost:3000</p>
      </div>

      <div style={{ marginTop: '30px' }}>
        <button 
          onClick={() => alert('Button clicked! React is working perfectly!')}
          style={{ 
            padding: '10px 20px', 
            fontSize: '16px', 
            background: '#1976d2', 
            color: 'white', 
            border: 'none', 
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Test Button - Click Me!
        </button>
      </div>
    </div>
  );
}

export default App;
