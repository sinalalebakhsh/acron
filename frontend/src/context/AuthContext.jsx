import React, { createContext, useState, useEffect, useContext } from 'react';
import axiosInstance from '../api/axiosInstance';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // بررسی وضعیت ورود با فراخوانی مسیر /api/me/
  useEffect(() => {
    const checkAuthStatus = async () => {
      const token = localStorage.getItem('access_token');
      if (token) {
        try {
          // 👈 دریافت اطلاعات کاربر از مسیر دقیق /api/me/
          const response = await axiosInstance.get('me/');
          setUser(response.data);
        } catch (error) {
          console.error('توکن نامعتبر است:', error);
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
        }
      }
      setLoading(false);
    };

    checkAuthStatus();
  }, []);

  // تابع ورود به حساب
  const login = async (username, password) => {
    // 👈 ارسال درخواست لاگین به مسیر دقیق /api/token/
    const response = await axiosInstance.post('token/', { 
      username: username, 
      password: password 
    });
    
    const { access, refresh } = response.data;

    // ذخیره توکن‌ها در Local Storage
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    
    // دریافت اطلاعات پروفایل کاربر بلافاصله پس از لاگین
    const userProfile = await axiosInstance.get('me/');
    setUser(userProfile.data);
    
    return response.data;
  };

  // تابع خروج
  const logout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout, loading, isAuthenticated: !!user }}>
      {!loading && children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
export { AuthContext };

