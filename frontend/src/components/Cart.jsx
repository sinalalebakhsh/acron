import React from 'react';
import { useCart } from '../context/CartContext';

function Cart() {
  const { cart, cartCount } = useCart();

  if (!cart || !cart.items || cart.items.length === 0) {
    return (
      <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
        <h2>سبد خرید شما خالی است 🛒</h2>
      </div>
    );
  }

  return (
    <div style={{ padding: '30px', maxWidth: '800px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2>سبد خرید شما ({cartCount} آیتم)</h2>
      
      <div style={{ display: 'flex', flexDirection: 'column', gap: '15px', marginTop: '20px' }}>
        {cart.items.map((item) => (
          <div key={item.id} style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '15px',
            border: '1px solid #e2e8f0',
            borderRadius: '8px',
            backgroundColor: '#fff'
          }}>
            <div>
              <h4 style={{ margin: '0 0 5px 0' }}>{item.product?.name || `محصول کد ${item.product_id}`}</h4>
              <span style={{ color: '#64748b', fontSize: '14px' }}>تعداد: {item.quantity}</span>
            </div>
            
            <div style={{ fontWeight: 'bold', color: '#059669' }}>
              {item.total_price 
                ? `${Number(item.total_price).toLocaleString()} تومان` 
                : item.product?.price 
                  ? `${(Number(item.product.price) * item.quantity).toLocaleString()} تومان`
                  : ''}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Cart;

