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
    

    const login = async (username, password) => {
        try {
            const response = await axiosInstance.post('token/', {
                username,
                password,
            });

            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);

            setUser({ username });
            return { success: true };
        } catch (error) {
            // این خط ارور واقعی را در کنسول مرورگر (F12) چاپ می‌کند تا بفهمیم داستان چیست
            console.error("Login Error details:", error);

            return {
                success: false,
                // اگر سرور پاسخ داده بود ارور سرور را نشان بده، در غیر این صورت پیغام خطای شبکه
                error: error.response?.data?.detail || error.message || 'خطا در برقراری ارتباط با سرور',
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

