import React, { createContext, useState, useEffect, useContext } from 'react';
import axiosInstance from '../api/axiosInstance';

const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState(null);
  const [cartCount, setCartCount] = useState(0);

  // ۱. دریافت یا ایجاد سبد خرید (پشتیبانی هوشمند از کاربر لاگین‌شده و مهمان)
  const fetchOrCreateCart = async () => {
    const token = localStorage.getItem('access_token');

    try {
      // سناریو اول: کاربر لاگین است -> دریافت سبد خرید اختصاصی کاربر از جنگو
      if (token) {
        const response = await axiosInstance.get('carts/mine/');
        setCart(response.data);
        if (response.data?.id) {
          localStorage.setItem('cart_id', response.data.id);
        }
        const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
        setCartCount(totalItems);
        return;
      }

      // سناریو دوم: کاربر مهمان است -> استفاده از UUID ذخیره‌شده در localStorage
      let cartId = localStorage.getItem('cart_id');

      // اگر کاربر مهمان هنوز آی‌دی سبد ندارد، یک سبد جدید در بک‌اند می‌سازیم
      if (!cartId) {
        const response = await axiosInstance.post('carts/');
        cartId = response.data.id;
        localStorage.setItem('cart_id', cartId);
      }

      const response = await axiosInstance.get(`carts/${cartId}/`);
      setCart(response.data);

      const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
      setCartCount(totalItems);
    } catch (error) {
      console.error('خطا در دریافت سبد خرید:', error);
      // اگر سبد خرید در دیتابیس یافت نشد (مثلاً پاک شده بود)، آی‌دی محلی را حذف کن
      if (error.response?.status === 404) {
        localStorage.removeItem('cart_id');
      }
    }
  };

  useEffect(() => {
    fetchOrCreateCart();
  }, []);

  // ۲. افزودن محصول به سبد خرید
  const addToCart = async (productId) => {
    try {
      let cartId = cart?.id || localStorage.getItem('cart_id');

      // اگر آی‌دی سبد خرید وجود نداشت، ابتدا یک سبد می‌سازیم
      if (!cartId) {
        const newCartResponse = await axiosInstance.post('carts/');
        cartId = newCartResponse.data.id;
        localStorage.setItem('cart_id', cartId);
      }

      // ارسال درخواست افزودن آیتم به اندپوینت درست در جنگو
      await axiosInstance.post('carts/cart-items/', {
        cart_id: cartId,
        product_id: productId,
        quantity: 1,
      });

      // به‌روزرسانی وضعیت سبد خرید
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در افزودن به سبد خرید:', error.response?.data || error);
    }
  };

  // ۳. تغییر تعداد محصول در سبد خرید (با استفاده از PATCH)
  const updateQuantity = async (itemId, newQuantity) => {
    if (newQuantity < 1) return;
    try {
      await axiosInstance.patch(`carts/cart-items/${itemId}/`, {
        quantity: newQuantity,
      });
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در به‌روزرسانی تعداد:', error.response?.data || error);
    }
  };

  // ۴. حذف کامل محصول از سبد خرید (با استفاده از DELETE)
  const removeFromCart = async (itemId) => {
    try {
      await axiosInstance.delete(`carts/cart-items/${itemId}/`);
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در حذف آیتم از سبد خرید:', error.response?.data || error);
    }
  };
  const [loading, setLoading] = useState(true);

  const fetchCart = async () => {
    try {
      const response = await axiosInstance.get('carts/mine/');
      setCart(response.data);
    } catch (error) {
      setCart(null);
    } finally {
      setLoading(false);
    }
  };

  // 🔴 تابعی برای صفر کردن سبد خرید در حافظه فرانت‌اند
  const clearCartState = () => {
    setCart(null);
  };

  useEffect(() => {
    fetchCart();
  }, []);

  // محاسبه تعداد کل آیتم‌ها برای نمایش در Navbar
  const totalItemsCount = cart?.items?.reduce((total, item) => total + item.quantity, 0) || 0;

  return (
    <CartContext.Provider
      value={{
        cart,
        totalItemsCount, 
        fetchCart, 
        clearCartState, // 🔴 اضافه شدن متد پاکسازی
        cartCount,
        addToCart,
        updateQuantity,
        removeFromCart,
        refreshCart: fetchOrCreateCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);