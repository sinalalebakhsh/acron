import React, { useState } from 'react';
import { useCart } from '../context/CartContext';
import { Link, useNavigate } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';

function Cart() {
  const { cart, cartCount, refreshCart } = useCart();
  const navigate = useNavigate();

  // وضعیت‌های مربوط به پنجره دریافت آدرس و ثبت سفارش
  const [showAddressModal, setShowAddressModal] = useState(false);
  const [shippingAddress, setShippingAddress] = useState('');
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  if (!cart || !cart.items || cart.items.length === 0) {
    return (
      <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
        <h2>سبد خرید شما خالی است 🛒</h2>
        <p style={{ color: '#64748b', marginTop: '10px' }}>می‌توانید محصولات را از کاتالوگ انتخاب کنید.</p>
        <Link to="/products" style={{
          display: 'inline-block',
          marginTop: '15px',
          padding: '10px 20px',
          backgroundColor: '#2563eb',
          color: 'white',
          textDecoration: 'none',
          borderRadius: '6px'
        }}>
          مشاهده کاتالوگ محصولات
        </Link>
      </div>
    );
  }

  const calculateTotalPrice = () => {
    return cart.items.reduce((sum, item) => {
      const price = item.total_price || (item.product?.price ? Number(item.product.price) * item.quantity : 0);
      return sum + price;
    }, 0);
  };

  // تابع ارسال درخواست ثبت سفارش به بک‌اند
  const handlePlaceOrder = async (e) => {
    e.preventDefault();
    setErrorMessage('');

    if (shippingAddress.trim().length < 10) {
      setErrorMessage('آدرس ارسال باید حداقل ۱۰ کاراکتر باشد.');
      return;
    }

    setLoading(true);
    try {
      const cartId = localStorage.getItem('cart_id');
      
      // ۱. ارسال درخواست به بک‌اند
      await axiosInstance.post('orders/', {
        cart_id: cartId,
        shipping_address: shippingAddress
      });

      // ۲. پاکسازی سبد خرید از حافظه مرورگر پس از ثبت موفق سفارش
      localStorage.removeItem('cart_id');
      await refreshCart();

      alert('🎉 سفارش شما با موفقیت ثبت شد!');
      setShowAddressModal(false);
      
      // انتقال کاربر به صفحه داشبورد یا لیست سفارشات
      navigate('/orders');
    } catch (error) {
      console.error('خطا در ثبت سفارش:', error.response?.data);
      const backendError = error.response?.data?.non_field_errors?.[0] 
        || error.response?.data?.shipping_address?.[0]
        || error.response?.data?.detail 
        || 'خطایی در ثبت سفارش رخ داد.';
      setErrorMessage(backendError);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سبد خرید شما ({cartCount} آیتم)</h2>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        {cart.items.map((item) => (
          <div key={item.id} style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '15px 20px',
            border: '1px solid #e2e8f0',
            borderRadius: '8px',
            backgroundColor: '#fff'
          }}>
            <div style={{ flex: 1 }}>
              <h3 style={{ margin: '0 0 5px 0', fontSize: '18px' }}>
                {item.product?.name || `محصول کد ${item.product_id}`}
              </h3>
              <span style={{ color: '#059669', fontWeight: 'bold' }}>
                تعداد: {item.quantity}
              </span>
            </div>
            <div style={{ fontWeight: 'bold', fontSize: '16px' }}>
              {(item.total_price 
                ? Number(item.total_price) 
                : (Number(item.product?.price || 0) * item.quantity)
              ).toLocaleString()} تومان
            </div>
          </div>
        ))}
      </div>

      {/* خلاصه فاکتور */}
      <div style={{
        marginTop: '30px',
        padding: '20px',
        backgroundColor: '#f8fafc',
        border: '1px solid #cbd5e1',
        borderRadius: '8px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center'
      }}>
        <div>
          <span style={{ fontSize: '16px', color: '#475569' }}>مجموع قابل پرداخت:</span>
          <h2 style={{ margin: '5px 0 0 0', color: '#059669' }}>
            {calculateTotalPrice().toLocaleString()} تومان
          </h2>
        </div>

        <button 
          onClick={() => setShowAddressModal(true)}
          style={{
            padding: '12px 24px',
            backgroundColor: '#16a34a',
            color: 'white',
            border: 'none',
            borderRadius: '6px',
            fontSize: '16px',
            fontWeight: 'bold',
            cursor: 'pointer'
          }}
        >
          ادامه جهت ثبت سفارش ➔
        </button>
      </div>

      {/* پنجره مودال دریافت آدرس */}
      {showAddressModal && (
        <div style={{
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          backgroundColor: 'rgba(0,0,0,0.5)',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          zIndex: 1000
        }}>
          <div style={{
            backgroundColor: '#fff',
            padding: '30px',
            borderRadius: '10px',
            width: '90%',
            maxWidth: '500px',
            direction: 'rtl'
          }}>
            <h3 style={{ marginTop: 0 }}>تکمیل آدرس ارسال سفارش</h3>
            <form onSubmit={handlePlaceOrder}>
              <div style={{ marginBottom: '15px' }}>
                <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold' }}>
                  آدرس دقیق پستی:
                </label>
                <textarea 
                  rows="4"
                  value={shippingAddress}
                  onChange={(e) => setShippingAddress(e.target.value)}
                  placeholder="مثال: تهران، خیابان آزادی، پلاک ۱۲، واحد ۴ (حداقل ۱۰ کاراکتر)"
                  style={{
                    width: '100%',
                    padding: '10px',
                    borderRadius: '6px',
                    border: '1px solid #cbd5e1',
                    boxSizing: 'border-box'
                  }}
                  required
                />
              </div>

              {errorMessage && (
                <div style={{ color: '#dc2626', marginBottom: '15px', fontSize: '14px' }}>
                  {errorMessage}
                </div>
              )}

              <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '10px' }}>
                <button
                  type="button"
                  onClick={() => setShowAddressModal(false)}
                  disabled={loading}
                  style={{
                    padding: '10px 18px',
                    backgroundColor: '#e2e8f0',
                    border: 'none',
                    borderRadius: '6px',
                    cursor: 'pointer'
                  }}
                >
                  انصراف
                </button>
                <button
                  type="submit"
                  disabled={loading}
                  style={{
                    padding: '10px 20px',
                    backgroundColor: '#16a34a',
                    color: '#fff',
                    border: 'none',
                    borderRadius: '6px',
                    fontWeight: 'bold',
                    cursor: loading ? 'not-allowed' : 'pointer'
                  }}
                >
                  {loading ? 'در حال ثبت...' : 'تایید و ثبت سفارش نهایی'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}

export default Cart;