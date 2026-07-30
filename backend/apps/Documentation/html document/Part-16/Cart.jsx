import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axiosInstance';
import { useNavigate, Link } from 'react-router-dom';
import { useCart } from '../context/CartContext'; // 🔴 ۱. اضافه کردن ایمپورت

function Cart() {
  // 🔴 ۲. فراخوانی هوک در بالاترین سطح کامپوننت (قبل از هر شرط و return)
  const { clearCartState } = useCart();

  const [cart, setCart] = useState(null);
  const [addresses, setAddresses] = useState([]);
  const [selectedAddressId, setSelectedAddressId] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const fetchCartAndAddresses = async () => {
    try {
      // ۱. دریافت اطلاعات سبد خرید
      const cartRes = await axiosInstance.get('carts/mine/');
      setCart(cartRes.data);

      // ۲. دریافت لیست آدرس‌های ذخیره‌شده کاربر
      const addrRes = await axiosInstance.get('customers/addresses/');
      const addrList = Array.isArray(addrRes.data) ? addrRes.data : (addrRes.data?.results || []);
      setAddresses(addrList);

      // انتخاب خودکار آدرس پیش‌فرض در صورت وجود
      const defaultAddr = addrList.find(a => a.is_default);
      if (defaultAddr) {
        setSelectedAddressId(defaultAddr.id);
      } else if (addrList.length > 0) {
        setSelectedAddressId(addrList[0].id);
      }
    } catch (err) {
      console.error('خطا در دریافت اطلاعات:', err);
      setError('خطا در بارگذاری اطلاعات سبد خرید یا آدرس‌ها.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCartAndAddresses();
  }, []);

  // نهایی کردن و ثبت سفارش
  const handlePlaceOrder = async (e) => {
    e.preventDefault();
    if (!selectedAddressId) {
      alert('لطفاً یک آدرس برای ارسال انتخاب کنید.');
      return;
    }

    const selectedAddrObj = addresses.find(a => String(a.id) === String(selectedAddressId));
    if (!selectedAddrObj) {
      alert('آدرس انتخابی معتبر نیست.');
      return;
    }

    // ساخت رشته کامل آدرس جهت ثبت در سفارش
    const formattedAddress = `${selectedAddrObj.province}، ${selectedAddrObj.city}، ${selectedAddrObj.street} - گیرنده: ${selectedAddrObj.receiver_name} (${selectedAddrObj.phone_number})`;

    setSubmitting(true);
    try {
      await axiosInstance.post('orders/', {
        cart_id: cart.id,
        shipping_address: formattedAddress,
      });

      // 🔴 ۳. پاکسازی عدد و اطلاعات سبد خرید در Navbar
      clearCartState();

      alert('سفارش شما با موفقیت ثبت شد! 🎉');
      navigate('/orders');
    } catch (err) {
      console.error('خطا در ثبت سفارش:', err);
      alert('خطا در ثبت سفارش. لطفاً مجدداً تلاش کنید.');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div style={{ textAlign: 'center', marginTop: '50px', direction: 'rtl' }}>در حال بارگذاری سبد خرید... 🔄</div>;
  }

  if (error) {
    return <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', direction: 'rtl' }}>{error}</div>;
  }

  if (!cart || !cart.items || cart.items.length === 0) {
    return (
      <div style={{ textAlign: 'center', marginTop: '60px', direction: 'rtl', fontFamily: 'sans-serif' }}>
        <h2>سبد خرید شما خالی است 🛒</h2>
        <Link to="/products" style={{ display: 'inline-block', marginTop: '15px', color: '#2563eb' }}>
          مشاهده کاتالوگ محصولات
        </Link>
      </div>
    );
  }

  return (
    <div style={{ padding: '30px', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سبد خرید من 🛒</h2>

      {/* اقلام سبد خرید */}
      <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '15px', marginBottom: '20px', backgroundColor: '#fff' }}>
        {cart.items.map((item) => (
          <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '10px 0', borderBottom: '1px dashed #f1f5f9' }}>
            <div>
              <strong>{item.product?.name || `محصول ${item.product}`}</strong>
              <div style={{ fontSize: '13px', color: '#64748b' }}>تعداد: {item.quantity}</div>
            </div>
            <div>{Number(item.total_price || 0).toLocaleString()} تومان</div>
          </div>
        ))}
        <div style={{ marginTop: '15px', textAlign: 'left', fontWeight: 'bold', fontSize: '16px', color: '#059669' }}>
          جمع کل: {Number(cart.total_price || 0).toLocaleString()} تومان
        </div>
      </div>

      {/* بخش انتخاب آدرس ارسال */}
      <div style={{ border: '1px solid #e2e8f0', borderRadius: '8px', padding: '20px', backgroundColor: '#f8fafc' }}>
        <h3 style={{ marginTop: 0, color: '#1e293b' }}>آدرس تحویل سفارش 📍</h3>

        {addresses.length === 0 ? (
          <div style={{ color: '#dc2626', marginBottom: '15px' }}>
            شما هنوز هیچ آدرسی ثبت نکرده‌اید! 
            <br />
            <Link to="/profile" style={{ color: '#2563eb', fontWeight: 'bold', display: 'inline-block', marginTop: '8px' }}>
              + افزودن آدرس در صفحه پروفایل
            </Link>
          </div>
        ) : (
          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '8px', fontWeight: 'bold', color: '#334155' }}>
              انتخاب از آدرس‌های ذخیره‌شده:
            </label>
            <select
              value={selectedAddressId}
              onChange={(e) => setSelectedAddressId(e.target.value)}
              style={{
                width: '100%',
                padding: '10px',
                borderRadius: '6px',
                border: '1px solid #cbd5e1',
                fontSize: '14px',
                backgroundColor: '#fff'
              }}
            >
              {addresses.map((addr) => (
                <option key={addr.id} value={addr.id}>
                  {addr.title ? `[${addr.title}] ` : ''}{addr.province}، {addr.city}، {addr.street} ({addr.receiver_name}) {addr.is_default ? '⭐ پیش‌فرض' : ''}
                </option>
              ))}
            </select>
            
            <Link to="/profile" style={{ fontSize: '12px', color: '#2563eb', display: 'inline-block', marginTop: '8px' }}>
              مدیریت آدرس‌ها / افزودن آدرس جدید
            </Link>
          </div>
        )}

        <button
          onClick={handlePlaceOrder}
          disabled={submitting || addresses.length === 0}
          style={{
            width: '100%',
            padding: '12px',
            backgroundColor: addresses.length === 0 ? '#94a3b8' : '#16a34a',
            color: '#fff',
            border: 'none',
            borderRadius: '6px',
            fontSize: '16px',
            fontWeight: 'bold',
            cursor: addresses.length === 0 ? 'not-allowed' : 'pointer'
          }}
        >
          {submitting ? 'در حال ثبت سفارش...' : 'تکمیل و ثبت سفارش 📦'}
        </button>
      </div>
    </div>
  );
}

export default Cart;