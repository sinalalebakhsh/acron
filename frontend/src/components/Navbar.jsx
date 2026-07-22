import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext'; // 👈 اضافه شد

function Navbar() {
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  const { cartCount } = useCart(); // 👈 دریافت تعداد آیتم‌های سبد خرید

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <nav style={{
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      padding: '15px 30px',
      backgroundColor: '#1e293b',
      color: 'white',
      direction: 'rtl',
      fontFamily: 'sans-serif'
    }}>
      <div style={{ display: 'flex', gap: '20px', alignItems: 'center' }}>
        <h2 style={{ margin: 0, color: '#38bdf8' }}>ACRON</h2>
        <Link to="/" style={{ color: 'white', textDecoration: 'none' }}>داشبورد</Link>
        <Link to="/products" style={{ color: 'white', textDecoration: 'none' }}>محصولات</Link>
      </div>

      <div>
        {isAuthenticated ? (
          <div style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
            <span>خوش آمدی، <strong>{user?.username}</strong></span>
            <button 
              onClick={handleLogout} 
              style={{ padding: '6px 12px', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
            >
              خروج
            </button>
          </div>
        ) : (
          <Link to="/login" style={{ color: '#38bdf8', textDecoration: 'none' }}>ورود به حساب</Link>
        )}
      </div>
    </nav>
  );
}

export default Navbar;


