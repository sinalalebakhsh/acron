import apiClient from './apiClient';

const authService = {
  // متد لاگین و دریافت توکن‌های اولیه
  login: async (username, password) => {
    const response = await apiClient.post('/token/', { username, password });
    if (response.data.access && response.data.refresh) {
      localStorage.setItem('access_token', response.data.access);
      localStorage.setItem('refresh_token', response.data.refresh);
    }
    return response.data;
  },

  // دریافت اطلاعات کاربر فعلی (اکانت محافظت‌شده)
  getCurrentUser: async () => {
    const response = await apiClient.get('/accounts/me/'); // فرض بر وجود اِندپوینت me
    return response.data;
  },

  // خروج از حساب کاربری
  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/login';
  }
};

export default authService;

