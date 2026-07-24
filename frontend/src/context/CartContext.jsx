import React, { createContext, useState, useEffect, useContext } from 'react';
import axiosInstance from '../api/axiosInstance';

const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState(null);
  const [cartCount, setCartCount] = useState(0);

  // ۱. دریافت یا ایجاد سبد خرید
  const fetchOrCreateCart = async () => {
    let cartId = localStorage.getItem('cart_id');
    try {
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
    let cartId = localStorage.getItem('cart_id');
    
    if (!cartId) {
      const newCartResponse = await axiosInstance.post('carts/');
      cartId = newCartResponse.data.id;
      localStorage.setItem('cart_id', cartId);
    }

    try {
      await axiosInstance.post('cart-items/', {
        cart_id: cartId,
        product_id: productId,
        quantity: 1,
      });
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در افزودن به سبد خرید:', error.response?.data || error);
    }
  };

  // ۳. تغییر تعداد محصول در سبد خرید (تغییر با PATCH) 👈 جدید
  const updateQuantity = async (itemId, newQuantity) => {
    if (newQuantity < 1) return;
    try {
      await axiosInstance.patch(`cart-items/${itemId}/`, {
        quantity: newQuantity
      });
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در به‌روزرسانی تعداد:', error.response?.data || error);
    }
  };

  // ۴. حذف کامل محصول از سبد خرید (حذف با DELETE) 👈 جدید
  const removeFromCart = async (itemId) => {
    try {
      await axiosInstance.delete(`cart-items/${itemId}/`);
      await fetchOrCreateCart();
    } catch (error) {
      console.error('خطا در حذف آیتم از سبد خرید:', error.response?.data || error);
    }
  };

  return (
    <CartContext.Provider value={{ 
      cart, 
      cartCount, 
      addToCart, 
      updateQuantity, 
      removeFromCart, 
      refreshCart: fetchOrCreateCart 
    }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);


