import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axiosInstance';
import { Link } from 'react-router-dom';

function Orders() {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [payingOrderId, setPayingOrderId] = useState(null);

  const statusConfig = {
    P: { label: 'در انتظار پرداخت', color: '#d97706', bgColor: '#fef3c7' },
    C: { label: 'پرداخت موفق', color: '#16a34a', bgColor: '#dcfce7' },
    X: { label: 'لغو شده', color: '#dc2626', bgColor: '#fee2e2' },
  };

  const fetchOrders = async () => {
    try {
      const response = await axiosInstance.get('orders/');
      const rawData = response.data;
      const ordersArray = Array.isArray(rawData) 
        ? rawData 
        : (rawData?.results || []);

      setOrders(ordersArray);
    } catch (err) {
      console.error('خطا در دریافت سفارشات:', err);
      setError('خطا در دریافت لیست سفارش‌ها. لطفاً مجدداً تلاش کنید.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  // ارسال درخواست پردازش پرداخت به بک‌اند
  const handlePayment = async (orderId) => {
    setPayingOrderId(orderId);
    try {
      await axiosInstance.post(`orders/${orderId}/pay/`);
      
      alert('پرداخت با موفقیت انجام شد! 💳✨');
      
      // دریافت مجدد اطلاعات سفارشات برای به‌روزرسانی وضعیت روی صفحه
      await fetchOrders();
    } catch (err) {
      console.error('خطا در پرداخت:', err);
      const serverMessage = err.response?.data?.detail || 'خطایی در پردازش پرداخت رخ داد.';
      alert(serverMessage);
    } finally {
      setPayingOrderId(null);
    }
  };

  if (loading) {
    return (
      <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif', direction: 'rtl' }}>
        در حال دریافت تاریخچه سفارشات... 🔄
      </div>
    );
  }

  if (error) {
    return (
      <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', fontFamily: 'sans-serif', direction: 'rtl' }}>
        {error}
      </div>
    );
  }

  if (orders.length === 0) {
    return (
      <div style={{ textAlign: 'center', marginTop: '60px', fontFamily: 'sans-serif', direction: 'rtl' }}>
        <h2>هنوز هیچ سفارشی ثبت نکرده‌اید 📦</h2>
        <p style={{ color: '#64748b', marginTop: '10px' }}>محصولات مورد علاقه خود را انتخاب و سفارش دهید.</p>
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

  return (
    <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
      <h2 style={{ marginBottom: '20px', color: '#0f172a' }}>سفارش‌های من ({orders.length})</h2>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {orders.map((order) => {
          const status = statusConfig[order.status] || { label: order.status || 'نامشخص', color: '#475569', bgColor: '#f1f5f9' };
          
          let formattedDate = '---';
          if (order.created_at) {
            try {
              formattedDate = new Date(order.created_at).toLocaleDateString('fa-IR');
            } catch {
              formattedDate = order.created_at;
            }
          }

          return (
            <div key={order.id} style={{
              border: '1px solid #e2e8f0',
              borderRadius: '10px',
              backgroundColor: '#fff',
              overflow: 'hidden',
              boxShadow: '0 2px 4px rgba(0,0,0,0.04)'
            }}>
              {/* سربرگ کارت */}
              <div style={{
                padding: '15px 20px',
                backgroundColor: '#f8fafc',
                borderBottom: '1px solid #e2e8f0',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
              }}>
                <div>
                  <span style={{ fontSize: '13px', color: '#64748b' }}>شناسه سفارش: </span>
                  <strong style={{ fontSize: '14px', color: '#1e293b' }}>
                    {order.id ? String(order.id).substring(0, 8) : '---'}...
                  </strong>
                  <span style={{ margin: '0 10px', color: '#cbd5e1' }}>|</span>
                  <span style={{ fontSize: '13px', color: '#64748b' }}>تاریخ: {formattedDate}</span>
                </div>

                <span style={{
                  padding: '4px 12px',
                  borderRadius: '20px',
                  fontSize: '13px',
                  fontWeight: 'bold',
                  color: status.color,
                  backgroundColor: status.bgColor
                }}>
                  {status.label}
                </span>
              </div>

              {/* لیست اقلام */}
              <div style={{ padding: '20px' }}>
                <h4 style={{ margin: '0 0 12px 0', fontSize: '15px', color: '#334155' }}>اقلام سفارش:</h4>
                <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                  {order.items && order.items.map((item) => (
                    <li key={item.id} style={{
                      padding: '10px 0',
                      borderBottom: '1px dashed #f1f5f9',
                      display: 'flex',
                      justifyContent: 'space-between',
                      alignItems: 'center'
                    }}>
                      <span style={{ fontWeight: '500', color: '#0f172a' }}>
                        {item.product_name || `محصول کد ${item.product}`}
                      </span>

                      <div style={{ display: 'flex', gap: '15px', alignItems: 'center', fontSize: '14px' }}>
                        <span style={{
                          backgroundColor: '#f1f5f9',
                          padding: '3px 8px',
                          borderRadius: '5px',
                          color: '#475569',
                          fontSize: '13px'
                        }}>
                          تعداد: <strong>{item.quantity}</strong>
                        </span>

                        {item.unit_price && (
                          <span style={{ color: '#0f172a' }}>
                            قیمت واحد: <strong>{Number(item.unit_price).toLocaleString()}</strong> تومان
                          </span>
                        )}
                      </div>
                    </li>
                  ))}
                </ul>

                {/* جمع کل و دکمه پرداخت */}
                <div style={{
                  marginTop: '15px',
                  paddingTop: '15px',
                  borderTop: '1px solid #e2e8f0',
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center'
                }}>
                  {order.total_price !== undefined && (
                    <div style={{ fontWeight: 'bold', color: '#059669', fontSize: '15px' }}>
                      مجموع فاکتور: {Number(order.total_price).toLocaleString()} تومان
                    </div>
                  )}

                  {order.status === 'P' && (
                    <button
                      onClick={() => handlePayment(order.id)}
                      disabled={payingOrderId === order.id}
                      style={{
                        backgroundColor: payingOrderId === order.id ? '#94a3b8' : '#16a34a',
                        color: 'white',
                        border: 'none',
                        padding: '8px 18px',
                        borderRadius: '6px',
                        cursor: payingOrderId === order.id ? 'not-allowed' : 'pointer',
                        fontSize: '14px',
                        fontWeight: 'bold',
                        transition: 'background-color 0.2s'
                      }}
                    >
                      {payingOrderId === order.id ? 'در حال پرداخت...' : 'پرداخت فاکتور 💳'}
                    </button>
                  )}
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default Orders;


