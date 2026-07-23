import React, { createContext, useState, useEffect, useContext } from 'react';
import axiosInstance from '../api/axiosInstance';

const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState(null);
  const [cartCount, setCartCount] = useState(0);

  // ۱. دریافت یا ساخت سبد خرید
  const fetchOrCreateCart = async () => {
    let cartId = localStorage.getItem('cart_id');
    try {
      if (!cartId) {
        // ساخت سبد جدید با آدرس /api/carts/
        const response = await axiosInstance.post('carts/');
        cartId = response.data.id;
        localStorage.setItem('cart_id', cartId);
      }
      
      // دریافت جزئیات سبد خرید با آدرس /api/carts/<cart_id>/
      const response = await axiosInstance.get(`carts/${cartId}/`);
      setCart(response.data);
      
      const totalItems = response.data.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;
      setCartCount(totalItems);
    } catch (error) {
      console.error('خطا در دریافت سبد خرید:', error);
      // اگر سبد خرید با این شناسه وجود نداشت، پاکش کن تا دفعه بعد جدید ساخته شود
      if (error.response?.status === 404) {
        localStorage.removeItem('cart_id');
      }
    }
  };

  useEffect(() => {
    fetchOrCreateCart();
  }, []);

 const addToCart = async (productId) => {
  let cartId = localStorage.getItem('cart_id');
  
  if (!cartId) {
    const newCartResponse = await axiosInstance.post('carts/');
    cartId = newCartResponse.data.id;
    localStorage.setItem('cart_id', cartId);
  }

  try {
    // 👈 نام کلید دقیقا به cart_id تغییر کرد
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




  return (
    <CartContext.Provider value={{ cart, cartCount, addToCart, refreshCart: fetchOrCreateCart }}>
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);

