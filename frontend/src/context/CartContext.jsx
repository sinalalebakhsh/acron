import React, { createContext, useState, useEffect, useContext } from 'react';
import axiosInstance from '../api/axiosInstance';

const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState(null);
  const [cartCount, setCartCount] = useState(0);

  // ۱. دریافت یا ایجاد سبد خرید هنگام ورود به سایت
  const fetchOrCreateCart = async () => {
    let cartId = localStorage.getItem('cart_id');
    try {
      if (!cartId) {
        // ایجاد سبد خرید جدید در جنگو
        const response = await axiosInstance.post('carts/');
        cartId = response.data.id;
        localStorage.setItem('cart_id', cartId);
      }
      
      // دریافت جزئیات سبد خرید
      const response = await axiosInstance.get(`carts/${cartId}/`);
      setCart(response.data);
      
      // محاسبه مجموع تعداد آیتم‌های داخل سبد
      const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
      setCartCount(totalItems);
    } catch (error) {
      console.error('خطا در دریافت سبد خرید:', error);
    }
  };

  useEffect(() => {
    fetchOrCreateCart();
  }, []);

  // ۲. تابع افزودن محصول به سبد خرید
  const addToCart = async (productId) => {
    let cartId = localStorage.getItem('cart_id');
    if (!cartId) {
      await fetchOrCreateCart();
      cartId = localStorage.getItem('cart_id');
    }

    try {
      await axiosInstance.post(`carts/${cartId}/items/`, {
        product_id: productId,
        quantity: 1,
      });
      // به‌روزرسانی مجدد اطلاعات سبد خرید
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در افزودن به سبد خرید:', error);
    }
  };

  return (
    <CartContext.Provider value={{ cart, cartCount, addToCart, refreshCart: fetchOrCreateCart }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);


