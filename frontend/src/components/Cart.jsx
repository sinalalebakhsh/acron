import React from 'react';
import { useCart } from '../context/CartContext';
import { Link } from 'react-router-dom';

function Cart() {
  const { cart, cartCount, updateQuantity, removeFromCart } = useCart();

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

  // محاسبه قیمت کل سبد خرید
  const calculateTotalPrice = () => {
    return cart.items.reduce((sum, item) => {
      const price = item.total_price || (item.product?.price ? Number(item.product.price) * item.quantity : 0);
      return sum + price;
    }, 0);
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
            backgroundColor: '#fff',
            boxShadow: '0 1px 3px rgba(0,0,0,0.05)'
          }}>
            {/* اطلاعات محصول */}
            <div style={{ flex: 1 }}>
              <h3 style={{ margin: '0 0 5px 0', fontSize: '18px', color: '#1e293b' }}>
                {item.product?.name || item.product?.title || `محصول کد ${item.product_id}`}
              </h3>
              <span style={{ color: '#059669', fontWeight: 'bold' }}>
                {item.product?.price ? `${Number(item.product.price).toLocaleString()} تومان` : ''}
              </span>
            </div>

            {/* کنترلرهای افزایش / کاهش تعداد */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginLeft: '30px' }}>
              <button 
                onClick={() => updateQuantity(item.id, item.quantity + 1)}
                style={{
                  width: '32px',
                  height: '32px',
                  backgroundColor: '#e2e8f0',
                  border: 'none',
                  borderRadius: '4px',
                  fontSize: '18px',
                  fontWeight: 'bold',
                  cursor: 'pointer'
                }}
              >
                +
              </button>

              <span style={{ fontWeight: 'bold', fontSize: '16px', minWidth: '20px', textAlign: 'center' }}>
                {item.quantity}
              </span>

              <button 
                onClick={() => updateQuantity(item.id, item.quantity - 1)}
                disabled={item.quantity <= 1}
                style={{
                  width: '32px',
                  height: '32px',
                  backgroundColor: item.quantity <= 1 ? '#f1f5f9' : '#e2e8f0',
                  color: item.quantity <= 1 ? '#cbd5e1' : '#000',
                  border: 'none',
                  borderRadius: '4px',
                  fontSize: '18px',
                  fontWeight: 'bold',
                  cursor: item.quantity <= 1 ? 'not-allowed' : 'pointer'
                }}
              >
                -
              </button>
            </div>

            {/* قیمت کل آیتم و دکمه حذف */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '20px' }}>
              <span style={{ fontWeight: 'bold', fontSize: '16px', color: '#0f172a', minWidth: '100px', textAlign: 'left' }}>
                {(item.total_price 
                  ? Number(item.total_price) 
                  : (Number(item.product?.price || 0) * item.quantity)
                ).toLocaleString()} تومان
              </span>

              <button 
                onClick={() => removeFromCart(item.id)}
                style={{
                  padding: '6px 12px',
                  backgroundColor: '#fee2e2',
                  color: '#ef4444',
                  border: '1px solid #fca5a5',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '14px',
                  fontWeight: 'bold'
                }}
              >
                حذف 🗑️
              </button>
            </div>
          </div>
        ))}
      </div>

      {/* بخش خلاصه فاکتور و جمع کل */}
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
          onClick={() => alert('مرحله بعدی: اتصال به ثبت سفارش و درگاه پرداخت')}
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
    </div>
  );
}

export default Cart;

