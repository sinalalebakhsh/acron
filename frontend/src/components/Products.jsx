import React, { useState, useEffect } from 'react';
import axiosInstance from '../api/axiosInstance';
import { useCart } from '../context/CartContext'; // 👈 اضافه شد

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const { addToCart } = useCart(); // 👈 دریافت تابع افزودن به سبد

  useEffect(() => {
    // دریافت لیست محصولات از API جنگو
    axiosInstance.get('products/')
      .then((response) => {
        // بسته به اینکه API شما صفحه بندی دارد یا لیست مستقیم برمی گرداند
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

  if (loading) return <h3 style={{ textAlign: 'center', marginTop: '50px' }}>در حال بارگذاری محصولات...</h3>;
  if (error) return <h3 style={{ textAlign: 'center', color: 'red', marginTop: '50px' }}>{error}</h3>;

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2 style={{ textAlign: 'center', marginBottom: '30px' }}>کاتالوگ محصولات ACRON</h2>
      
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
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
              <p style={{ color: '#64748b', fontSize: '14px' }}>{product.description || 'بدون توضیحات'}</p>
            </div>
            <div style={{ marginTop: '15px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <span style={{ fontWeight: 'bold', color: '#059669' }}>
                {product.price ? `${Number(product.price).toLocaleString()} تومان` : 'قیمت تعیین‌نشده'}
              </span>
              <button 
              onClick={() => addToCart(product.id)} // 👈 کلیک و ارسال ID محصول
              style={{
                padding: '8px 12px',
                backgroundColor: '#2563eb',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer'
              }}>
                افزودن به سبد
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Products;


