import React, { useContext, useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthContext } from './context/AuthContext';
import axiosInstance from './api/axiosInstance'; // وارد کردن نمونه اکسپوس خودمان
import Login from './components/Login';
import ProtectedRoute from './components/ProtectedRoute';

// پنل اصلی پروژه Acron (با قابلیت دریافت دیتا از سرور)
function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  const [serverMessage, setServerMessage] = useState('در حال بارگذاری اطلاعات از جنگو...');
  const [error, setError] = useState('');

  useEffect(() => {
    // ۱. ارسال درخواست به یک اِندپوینت دلخواه در جنگو که نیاز به لاگین دارد.
    // نکته: آدرس زیر را می‌توانید به هر کدام از اِندپوینت‌های محافظت‌شده جنگوی خود تغییر دهید (مثلاً 'profile/' یا 'dashboard/')
    axiosInstance.get('dashboard/') 
      .then((response) => {
        // اگر سرور پاسخ داد، دیتا را در استیت ذخیره می‌کنیم
        // فرض می‌کنیم جنگو یک فیلد به نام message یا شبیه آن پس می‌فرستد
        setServerMessage(response.data.message || 'اطلاعات با موفقیت دریافت شد اما فیلد message یافت نشد.');
      })
      .catch((err) => {
        console.error("API Call Error:", err);
        setError('فرانت‌اِند درخواست را فرستاد، اما بک‌اِند خطایی برگرداند یا این اِندپوینت هنوز ساخته نشده است.');
      });
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '80px', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h1>به پنل اصلی پروژه Acron خوش آمدید!</h1>
      <p style={{ color: '#555', fontSize: '18px' }}>کاربر جاری: <strong>{user?.username}</strong></p>
      
      <hr style={{ width: '50%', margin: '20px auto', borderColor: '#eee' }} />

      {/* نمایش پیام دریافتی از جنگو */}
      <div style={{ padding: '20px', backgroundColor: error ? '#ffebee' : '#e8f5e9', display: 'inline-block', borderRadius: '6px', minWidth: '300px' }}>
        <h4 style={{ margin: '0 0 10px 0', color: error ? '#c62828' : '#2e7d32' }}>پاسخ زنده از سرور جنگو:</h4>
        <p style={{ margin: 0, color: '#333' }}>{error ? error : serverMessage}</p>
      </div>

      <br />
      <button 
        onClick={logout} 
        style={{ padding: '10px 20px', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', marginTop: '30px', fontWeight: 'bold' }}
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
        <Route 
          path="/login" 
          element={user ? <Navigate to="/" replace /> : <Login />} 
        />
        <Route 
          path="/" 
          element = {
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } 
        />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
}

export default App;

