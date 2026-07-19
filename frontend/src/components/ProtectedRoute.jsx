import React, { useContext } from 'react';
import { Navigate } from 'react-router-dom';
import { AuthContext } from '../context/AuthContext';

// این کامپوننت دور هر صفحه‌ای بپیچد، آن صفحه پنهان و امن می‌شود
function ProtectedRoute({ children }) {
    const { user, loading } = useContext(AuthContext);

    if (loading) {
        return <div style={{ textAlign: 'center', marginTop: '50px' }}>در حال بارگذاری...</div>;
    }

    // اگر کاربر لاگین نکرده بود، او را به صفحه لاگین هدایت کن
    if (!user) {
        return <Navigate to="/login" replace />;
    }

    // اگر لاگین بود، اجازه بده محتوای صفحه را ببیند
    return children;
}

export default ProtectedRoute;


