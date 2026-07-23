import React, { useState, useEffect } from 'react';
import axiosInstance from '../api/axiosInstance';
import { useCart } from '../context/CartContext';

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [addingId, setAddingId] = useState(null); // 👈 نگهداری ID محصول در حال اضافه شدن
  const [successId, setSuccessId] = useState(null); // 👈 نگهداری ID محصولی که اضافه شد

  const { addToCart } = useCart();

  useEffect(() => {
    axiosInstance.get('products/')
      .then((response) => {
        const data = response.data.results || response.data;
        setProducts(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error('خطا در دریافت محصولات:', err);
        setError('امکان دریافت لیست محصولات وجود ندارد.');
        setLoading(false);
      });
  }, []);

  const handleAddToCart = async (productId) => {
    setAddingId(productId); // فعال کردن حالت لودینگ دکمه
    await addToCart(productId);
    setAddingId(null);
    
    // نمایش پیام موفقیت‌آمیز به مدت ۱.۵ ثانیه
    setSuccessId(productId);
    setTimeout(() => {
      setSuccessId(null);
    }, 1500);
  };

  if (loading) return <h3 style={{ textAlign: 'center', marginTop: '50px' }}>در حال بارگذاری محصولات...</h3>;
  if (error) return <h3 style={{ textAlign: 'center', color: 'red', marginTop: '50px' }}>{error}</h3>;

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '30px' }}>کاتالوگ محصولات ACRON</h2>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
        gap: '20px'
      }}>
        {products.map((product) => (
          <div key={product.id} style={{
            border: '1px solid #e2e8f0',
            borderRadius: '8px',
            padding: '15px',
            backgroundColor: '#fff',
            boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between'
          }}>
            <div>
              <h3 style={{ margin: '0 0 10px 0', color: '#0f172a' }}>{product.name || product.title}</h3>
              <p style={{ color: '#64748b', fontSize: '14px', lineHeight: '1.6' }}>{product.description || 'بدون توضیحات'}</p>
            </div>
            <div style={{ marginTop: '15px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontWeight: 'bold', color: '#059669' }}>
                {product.price ? `${Number(product.price).toLocaleString()} تومان` : 'قیمت تعیین‌نشده'}
              </span>
              
              <button 
                onClick={() => handleAddToCart(product.id)}
                disabled={addingId === product.id}
                style={{
                  padding: '8px 14px',
                  backgroundColor: successId === product.id ? '#10b981' : '#2563eb',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: addingId === product.id ? 'not-allowed' : 'pointer',
                  fontWeight: 'bold',
                  transition: 'background-color 0.2s'
                }}
              >
                {addingId === product.id 
                  ? 'در حال افزودن...' 
                  : successId === product.id 
                    ? 'افزوده شد ✓' 
                    : 'افزودن به سبد'}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Products;