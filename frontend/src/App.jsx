import React, { useContext, useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthContext } from './context/AuthContext';
import axiosInstance from './api/axiosInstance'; // وارد کردن نمونه اکسپوس خودمان
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';
import Cart from './components/Cart'; // 👈 اضافه شد





function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  const [profileData, setProfileData] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    // ارسال درخواست به اِندپوینت واقعی پروفایل در جنگو
    axiosInstance.get('customers/profile/') 
      .then((response) => {
        // ذخیره اطلاعات واقعی مشتری (مانند تلفن، کد ملی یا هر چه در سریالایزر هست)
        setProfileData(response.data);
      })
      .catch((err) => {
        console.error("API Call Error:", err);
        setError('خطا در دریافت اطلاعات واقعی پروفایل از دیتابیس.');
      });
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '80px', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h1>به پنل اصلی پروژه Acron خوش آمدید!</h1>
      <p style={{ color: '#555', fontSize: '18px' }}>کاربر جاری سیستم: <strong>{user?.username}</strong></p>
      
      <hr style={{ width: '50%', margin: '20px auto', borderColor: '#eee' }} />

      <div style={{ padding: '20px', backgroundColor: error ? '#ffebee' : '#e8f5e9', display: 'inline-block', borderRadius: '6px', minWidth: '350px', textAlign: 'right' }}>
        <h4 style={{ margin: '0 0 10px 0', color: error ? '#c62828' : '#2e7d32', textAlign: 'center' }}>
          {error ? 'خطا در ارتباط' : 'مشخصات واقعی شما از دیتابیس جنگو:'}
        </h4>
        
        {error ? (
          <p style={{ color: '#333', textAlign: 'center' }}>{error}</p>
        ) : profileData ? (
          <pre style={{ direction: 'ltr', backgroundColor: '#fff', padding: '10px', borderRadius: '4px', overflowX: 'auto' }}>
            {JSON.stringify(profileData, null, 2)}
          </pre>
        ) : (
          <p style={{ textAlign: 'center' }}>در حال بارگذاری اطلاعات...</p>
        )}
      </div>

      <br />
      {/* <button 
        onClick={logout} 
        style={{ padding: '10px 20px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', marginTop: '30px', fontWeight: 'bold' }}
      >
        خروج از حساب
      </button> */}
    </div>
  );
}


// ...........



import { useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Products from './components/Products';



function App() {
  const { user } = useAuth();

  return (
    <Router>
      <Navbar />
      <Routes>
        <Route 
          path="/login" 
          element={user ? <Navigate to="/" replace /> : <Login />} 
        />
        <Route 
          path="/" 
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } 
        />
        <Route 
          path="/products" 
          element={
            <ProtectedRoute>
              <Products />
            </ProtectedRoute>
          } 
        />
        <Route 
          path="/cart" 
          element={
            <ProtectedRoute>
              <Cart />
            </ProtectedRoute>
          } 
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;


