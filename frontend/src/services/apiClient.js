import axios from 'axios';

// تعریف آدرس پایه API (می‌تواند از فایل .env خوانده شود)
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api';

// ایجاد یک اینس‌تنس اختصاصی از اکسیدوس برای درخواست‌های عمومی و احراز هویت شده
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// ----------------------------------------------------------------
// ۱. Request Interceptor: تزریق توکن به هدر درخواست‌ها
// ----------------------------------------------------------------
apiClient.interceptors.request.use(
  (config) => {
    const accessToken = localStorage.getItem('access_token');
    
    // اگر توکن در حافظه مرورگر موجود بود، آن را به هدر Authorization اضافه کن
    if (accessToken && !config.headers['Authorization']) {
      config.headers['Authorization'] = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// ----------------------------------------------------------------
// ۲. Response Interceptor: مدیریت خطای 401 و تمدید خودکار توکن
// ----------------------------------------------------------------
apiClient.interceptors.response.use(
  (response) => response, // اگر پاسخ موفقیت‌آمیز بود، بدون تغییر آن را پاس بده
  async (error) => {
    const originalRequest = error.config;

    // بررسی اینکه آیا خطا مربوط به انقضای توکن (401) است و آیا قبلاً این درخواست را مجدد تلاش نکرده‌ایم؟
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true; // علامت‌گذاری درخواست برای جلوگیری از حلقه بی‌نهایت

      const refreshToken = localStorage.getItem('refresh_token');

      // اگر رفرش توکن وجود نداشت، کاربر باید مجدداً لاگین کند
      if (!refreshToken) {
        handleLogout();
        return Promise.reject(error);
      }

      try {
        // ارسال درخواست تمدید توکن به اِندپوینت بک‌اند
        // نکته مهم: از خود apiClient استفاده نمی‌کنیم تا وارد اینترسپتور قبلی نشود
        const response = await axios.post(`${API_BASE_URL}/token/refresh/`, {
          refresh: refreshToken,
        });

        const newAccessToken = response.data.access;

        // ذخیره توکن دسترسی جدید در مرورگر
        localStorage.setItem('access_token', newAccessToken);

        // به‌روزرسانی هدر درخواست اصلی با توکن جدید
        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`;

        // ارسال مجدد درخواست اصلی کاربر با توکن جدید
        return apiClient(originalRequest);
      } catch (refreshError) {
        // اگر فرآیند تمدید توکن هم با خطا مواجه شد (مثلاً رفرش توکن هم منقضی شده بود)
        handleLogout();
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  }
);

// تابع کمکی برای پاکسازی اطلاعات در صورت منقضی شدن کامل نشست کاربری
function handleLogout() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  // هدایت کاربر به صفحه لاگین (در صورت استفاده از React Router می‌توان این منطق را بهبود داد)
  if (window.location.pathname !== '/login') {
    window.location.href = '/login';
  }
}

export default apiClient;




