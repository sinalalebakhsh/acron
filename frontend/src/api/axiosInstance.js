import axios from 'axios';

// ۱. ساخت نمونه پایه اکسپوس
const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/', // آدرس بک‌اند جنگو
    timeout: 5000,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
});

// ۲. اینترسپتور درخواست‌ها: تزریق خودکار توکن به هدر تمام درخواست‌ها
axiosInstance.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem('access_token');
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// ۳. اینترسپتور پاسخ‌ها: مدیریت هوشمند خطای 401 و تمدید توکن با Refresh Token
axiosInstance.interceptors.response.use(
    (response) => response,
    async (error) => {
        const originalRequest = error.config;

        // اگر سرور خطای 401 داد و این درخواست قبلاً یک‌بار برای تمدید تلاش نکرده بود
        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            const refreshToken = localStorage.getItem('refresh_token');

            if (refreshToken) {
                try {
                    // ارسال درخواست تمدید توکن به لایه احراز هویت جنگو
                    const response = await axios.post('http://127.0.0.1:8000/api/token/refresh/', {
                        refresh: refreshToken,
                    });

                    const newAccessToken = response.data.access;
                    localStorage.setItem('access_token', newAccessToken);

                    // به‌روزرسانی هدر درخواست اصلی با توکن جدید و اجرای مجدد آن
                    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                    return axiosInstance(originalRequest);
                } catch (refreshError) {
                    // اگر خودِ ریفرش توکن هم منقضی یا باطل شده باشد -> خروج کاربر
                    localStorage.removeItem('access_token');
                    localStorage.removeItem('refresh_token');
                    
                    // بعداً در لایه Context این بخش را برای انتقال کاربر به صفحه لاگین بهینه‌تر می‌کنیم
                    window.location.href = '/login'; 
                    return Promise.reject(refreshError);
                }
            }
        }
        return Promise.reject(error);
    }
);

export default axiosInstance;

