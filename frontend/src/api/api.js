import axios from 'axios';

// ۱. ساخت نمونه اختصاصی آکسیوس
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// ۲. Request Interceptor: افزودن توکن به هدر تمام درخواست‌ها
api.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem('access_token');
    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// ۳. Response Interceptor: دریافت توکن جدید در صورت بروز خطای 401
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // اگر خطای 401 دریافت شد و درخواست هنوز دوباره تلاش نشده بود
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refresh_token');
        if (!refreshToken) {
          throw new Error('توکن رفرش وجود ندارد');
        }

        // درخواست توکن جدید از جنگو
        const response = await axios.post('http://127.0.0.1:8000/api/accounts/token/refresh/', {
          refresh: refreshToken,
        });

        const newAccessToken = response.data.access;
        localStorage.setItem('access_token', newAccessToken);

        // جایگذاری توکن جدید در درخواست قبلی و اجرای مجدد آن
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
        return api(originalRequest);
      } catch (refreshError) {
        // اگر توکن رفرش هم منقضی شده بود، خروج کامل کاربر
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

export default api;

