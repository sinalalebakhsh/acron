import React, { useEffect, useState } from 'react';
import axiosInstance from '../api/axiosInstance';

function Profile() {
  const [profile, setProfile] = useState(null);
  const [addresses, setAddresses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // وضعیت فرم آدرس جدید
  const [showAddForm, setShowAddForm] = useState(false);
  const [newAddress, setNewAddress] = useState({
    title: '',
    receiver_name: '',
    phone_number: '',
    province: '',
    city: '',
    street: '',
    postal_code: '',
  });
  const [submitting, setSubmitting] = useState(false);

  // دریافت اطلاعات پروفایل و آدرس‌ها
  const fetchProfileData = async () => {
    try {
      const response = await axiosInstance.get('customers/profile/');
      setProfile(response.data);
      setAddresses(response.data.addresses || []);
    } catch (err) {
      console.error('خطا در دریافت پروفایل:', err);
      setError('خطا در دریافت اطلاعات پروفایل.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfileData();
  }, []);

  // تغییر آدرس پیش‌فرض
  const handleSetDefault = async (addressId) => {
    try {
      await axiosInstance.post(`customers/addresses/${addressId}/set-default/`);
      fetchProfileData(); // به‌روزرسانی لیست
    } catch (err) {
      alert('خطا در تغییر آدرس پیش‌فرض');
    }
  };

  // ثبت آدرس جدید
  const handleAddAddress = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await axiosInstance.post('customers/addresses/', newAddress);
      setShowAddForm(false);
      setNewAddress({
        title: '',
        receiver_name: '',
        phone_number: '',
        province: '',
        city: '',
        street: '',
        postal_code: '',
      });
      fetchProfileData();
    } catch (err) {
      alert('خطا در ثبت آدرس جدید. لطفاً ورودی‌ها را بررسی کنید.');
    } finally {
      setSubmitting(false);
    }
  };

  // حذف آدرس
  const handleDeleteAddress = async (addressId) => {
    if (!window.confirm('آیا از حذف این آدرس اطمینان دارید؟')) return;
    try {
      await axiosInstance.delete(`customers/addresses/${addressId}/`);
      fetchProfileData();
    } catch (err) {
      alert('خطا در حذف آدرس');
    }
  };

  if (loading) {
    return <div style={{ textAlign: 'center', marginTop: '50px', direction: 'rtl' }}>در حال دریافت اطلاعات کاربر... 🔄</div>;
  }

  if (error) {
    return <div style={{ textAlign: 'center', marginTop: '50px', color: '#dc2626', direction: 'rtl' }}>{error}</div>;
  }

  return (
    <div style={{ padding: '30px', maxWidth: '850px', margin: '0 auto', fontFamily: 'sans-serif', direction: 'rtl' }}>
      
      {/* کارت اطلاعات کاربر */}
      <div style={{
        backgroundColor: '#fff',
        border: '1px solid #e2e8f0',
        borderRadius: '10px',
        padding: '20px',
        marginBottom: '25px',
        boxShadow: '0 2px 4px rgba(0,0,0,0.03)'
      }}>
        <h2 style={{ margin: '0 0 15px 0', color: '#0f172a' }}>پروفایل کاربری 👤</h2>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', color: '#334155' }}>
          <div><strong>نام کاربری:</strong> {profile?.username}</div>
          <div><strong>ایمیل:</strong> {profile?.email || 'ثبت نشده'}</div>
          <div><strong>نام و نام خانوادگی:</strong> {profile?.first_name} {profile?.last_name}</div>
          <div><strong>شماره تماس:</strong> {profile?.customer_phone || 'ثبت نشده'}</div>
        </div>
      </div>

      {/* بخش آدرس‌ها */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '15px' }}>
        <h3 style={{ margin: 0, color: '#0f172a' }}>آدرس‌های پستی من ({addresses.length}) 📍</h3>
        <button
          onClick={() => setShowAddForm(!showAddForm)}
          style={{
            backgroundColor: showAddForm ? '#64748b' : '#2563eb',
            color: '#fff',
            border: 'none',
            padding: '8px 16px',
            borderRadius: '6px',
            cursor: 'pointer',
            fontWeight: 'bold'
          }}
        >
          {showAddForm ? 'انصراف' : '+ افزودن آدرس جدید'}
        </button>
      </div>

      {/* فرم افزودن آدرس جدید */}
      {showAddForm && (
        <form onSubmit={handleAddAddress} style={{
          backgroundColor: '#f8fafc',
          border: '1px solid #cbd5e1',
          borderRadius: '10px',
          padding: '20px',
          marginBottom: '25px'
        }}>
          <h4 style={{ marginTop: 0, color: '#1e293b' }}>افزودن آدرس پستی جدید</h4>
          
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', marginBottom: '12px' }}>
            <input
              type="text"
              placeholder="عنوان (مثلاً خانه، محل کار)"
              value={newAddress.title}
              onChange={(e) => setNewAddress({ ...newAddress, title: e.target.value })}
              required
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="نام گیرنده"
              value={newAddress.receiver_name}
              onChange={(e) => setNewAddress({ ...newAddress, receiver_name: e.target.value })}
              required
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="شماره تماس گیرنده"
              value={newAddress.phone_number}
              onChange={(e) => setNewAddress({ ...newAddress, phone_number: e.target.value })}
              required
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="کد پستی (۱۰ رقمی)"
              value={newAddress.postal_code}
              onChange={(e) => setNewAddress({ ...newAddress, postal_code: e.target.value })}
              required
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="استان"
              value={newAddress.province}
              onChange={(e) => setNewAddress({ ...newAddress, province: e.target.value })}
              required
              style={inputStyle}
            />
            <input
              type="text"
              placeholder="شهر"
              value={newAddress.city}
              onChange={(e) => setNewAddress({ ...newAddress, city: e.target.value })}
              required
              style={inputStyle}
            />
          </div>

          <textarea
            placeholder="آدرس دقیق پستی (خیابان، کوچه، پلاک، واحد)"
            value={newAddress.street}
            onChange={(e) => setNewAddress({ ...newAddress, street: e.target.value })}
            required
            rows="3"
            style={{ ...inputStyle, width: '100%', marginBottom: '15px' }}
          />

          <button
            type="submit"
            disabled={submitting}
            style={{
              backgroundColor: '#16a34a',
              color: '#fff',
              border: 'none',
              padding: '10px 20px',
              borderRadius: '6px',
              cursor: 'pointer',
              fontWeight: 'bold'
            }}
          >
            {submitting ? 'در حال ثبت...' : 'ذخیره آدرس'}
          </button>
        </form>
      )}

      {/* لیست آدرس‌ها */}
      {addresses.length === 0 ? (
        <p style={{ color: '#64748b' }}>هیچ آدرسی ثبت نکرده‌اید.</p>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
          {addresses.map((addr) => (
            <div key={addr.id} style={{
              border: addr.is_default ? '2px solid #2563eb' : '1px solid #e2e8f0',
              backgroundColor: addr.is_default ? '#eff6ff' : '#fff',
              borderRadius: '8px',
              padding: '15px 20px',
              position: 'relative'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                <strong style={{ fontSize: '16px', color: '#0f172a' }}>
                  {addr.title || 'آدرس بدون عنوان'}
                </strong>
                {addr.is_default ? (
                  <span style={{ backgroundColor: '#2563eb', color: '#fff', fontSize: '12px', padding: '2px 8px', borderRadius: '12px' }}>
                    آدرس پیش‌فرض
                  </span>
                ) : (
                  <button
                    onClick={() => handleSetDefault(addr.id)}
                    style={{ background: 'none', border: 'none', color: '#2563eb', cursor: 'pointer', fontSize: '13px' }}
                  >
                    انتخاب به‌عنوان پیش‌فرض
                  </button>
                )}
              </div>

              <p style={{ margin: '5px 0', color: '#334155', fontSize: '14px' }}>
                {addr.province}، {addr.city}، {addr.street}
              </p>
              
              <div style={{ fontSize: '13px', color: '#64748b', marginTop: '8px', display: 'flex', gap: '20px' }}>
                <span>گیرنده: {addr.receiver_name}</span>
                <span>تلفن: {addr.phone_number}</span>
                <span>کد پستی: {addr.postal_code}</span>
              </div>

              <button
                onClick={() => handleDeleteAddress(addr.id)}
                style={{
                  position: 'absolute',
                  top: '15px',
                  left: '15px',
                  background: 'none',
                  border: 'none',
                  color: '#dc2626',
                  cursor: 'pointer',
                  fontSize: '13px'
                }}
              >
                حذف
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

const inputStyle = {
  padding: '8px 12px',
  borderRadius: '6px',
  border: '1px solid #cbd5e1',
  fontSize: '14px',
  boxSizing: 'border-box'
};


export default Profile;



