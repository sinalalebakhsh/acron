import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext'; // 👈 اضافه شد

function Navbar() {
  const { user, logout, isAuthenticated } = useAuth();
  const navigate = useNavigate();
  // const { cartCount } = useCart(); // 👈 دریافت تعداد آیتم‌های سبد خرید
  // 🔴 ۲. دریافت تعداد کل آیتم‌ها از Context
  const { totalItemsCount } = useCart(); 

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
        <Link to="/cart" style={{ textDecoration: 'none' }}>
            <span style={{
              backgroundColor: '#0284c7',
              color: 'white',
              padding: '6px 12px',
              borderRadius: '12px',
              fontSize: '14px',
              fontWeight: 'bold',
              cursor: 'pointer'
            }}>
              🛒 سبد خرید: {totalItemsCount}
            </span>
        </Link>
        <Link to="/orders" style={{ color: 'white', textDecoration: 'none', marginLeft: '15px' }}> سفارش‌های من </Link>
      </div>


       <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
        {user ? (
          <>
            {/* لینک به صفحه پروفایل کاربر */}
            <Link to="/profile" style={{
              color: '#38bdf8',
              textDecoration: 'none',
              fontWeight: 'bold',
              backgroundColor: '#1e293b',
              padding: '6px 12px',
              borderRadius: '6px'
            }}>
              پروفایل {user.username || user} 👤
            </Link>

            <button
              onClick={handleLogout}
              style={{
                backgroundColor: '#dc2626',
                color: '#fff',
                border: 'none',
                padding: '6px 12px',
                borderRadius: '6px',
                cursor: 'pointer'
              }}
            >
              خروج 
            </button>
          </>
        ) : (
          <Link to="/login" style={{ color: '#fff', textDecoration: 'none' }}>
            ورود / ثبت‌نام
          </Link>
        )}
      </div>
      
    </nav>
  );
}

export default Navbar;


