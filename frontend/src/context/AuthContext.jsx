import React, { createContext, useState, useEffect } from 'react';
import axiosInstance from '../api/axiosInstance';

// ایجاد کانتکست اصلی احراز هویت
export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // بررسی وضعیت کاربر در اولین ورود به سایت
        const checkAuth = () => {
            const token = localStorage.getItem('access_token');
            if (token) {
                // فعلاً وضعیت کاربر را بر اساس وجود توکن تایید می‌کنیم
                setUser({ loggedIn: true });
            }
            setLoading(false);
        };
        checkAuth();
    }, []);

    // تابع ورود به برنامه و دریافت توکن از جنگو
    const login = async (username, password) => {
        try {
            // ارسال درخواست به اندپوینت توکن جنگو (آدرس با baseURL ترکیب می‌شود -> api/token/)
            const response = await axiosInstance.post('token/', {
                username,
                password,
            });

            // ذخیره توکن‌ها در مرورگر
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);

            // به‌روزرسانی وضعیت کاربر در برنامه
            setUser({ username });
            return { success: true };
        } catch (error) {
            return {
                success: false,
                error: error.response?.data?.detail || 'نام کاربری یا رمز عبور اشتباه است.',
            };
        }
    };

    // تابع خروج از برنامه
    const logout = () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        setUser(null);
    };

    return (
        <AuthContext.Provider value={{ user, loading, login, logout }}>
            {!loading && children}
        </AuthContext.Provider>
    );
};

