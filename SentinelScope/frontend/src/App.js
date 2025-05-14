import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [email, setEmail] = useState("");
  const [results, setResults] = useState([]);

  const fetchLeaks = async () => {
    const res = await axios.get(`http://localhost:8000/osint/leaks/${email}`);
    setResults(res.data.results);
  };

  return (
    <div>
      <h1>SentinelScope - OSINT Panel</h1>
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
      <button onClick={fetchLeaks}>Buscar filtraciones</button>
      <pre>{JSON.stringify(results, null, 2)}</pre>
    </div>
  );
}

export default App;
