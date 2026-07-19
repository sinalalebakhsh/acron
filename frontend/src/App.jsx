import React, { useContext } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthContext } from './context/AuthContext';
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';

// صفحه اصلی برنامه (داشبورد یا محیط اصلی پروژه Acron)
function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  return (
    <div style={{ textAlign: 'center', marginTop: '100px', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h1>به پنل اصلی پروژه Acron خوش آمدید!</h1>
      <p>این یک صفحه محافظت‌شده است و فقط کاربران لاگین‌شده آن را می‌بینند.</p>
      <button 
        onClick={logout} 
        style={{ padding: '10px 20px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', marginTop: '20px' }}
      >
        خروج از حساب
      </button>
    </div>
  );
}

function App() {
  const { user } = useContext(AuthContext);

  return (
    <Router>
      <Routes>
        {/* مسیر لاگین: اگر کاربر از قبل لاگین پدارد، او را مستقیم بفرست به صفحه اصلی */}
        <Route 
          path="/login" 
          element={user ? <Navigate to="/" replace /> : <Login />} 
        />

        {/* مسیر اصلی پروژه: توسط کامپوننت ProtectedRoute محافظت شده است */}
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } 
        />

        {/* هدایت کردن هر آدرس ناشناخته دیگر به صفحه اصلی */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;


