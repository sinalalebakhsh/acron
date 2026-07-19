import React, { useContext } from 'react';
import { AuthContext } from './context/AuthContext';
import Login from './components/Login';

function App() {
  const { user, logout } = useContext(AuthContext);

  return (
    <div>
      {user ? (
        <div style={{ textAlign: 'center', marginTop: '100px', fontFamily: 'sans-serif', direction: 'rtl' }}>
          <h1>خوش آمدید! شما با موفقیت وارد پروژه Acron شدید.</h1>
          <button 
            onClick={logout} 
            style={{ padding: '10px 20px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', marginTop: '20px' }}
          >
            خروج از حساب
          </button>
        </div>
      ) : (
        <Login />
      )}
    </div>
  );
}

export default App;