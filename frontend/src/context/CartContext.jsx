import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

import { useAuth } from "./AuthContext";
import cartService from "../services/cartService";

const CartContext = createContext(null);

export const CartProvider = ({ children }) => {
  const {
    isAuthenticated,
    loading: authLoading,
  } = useAuth();

  const [cart, setCart] = useState(null);
  const [loading, setLoading] = useState(true);

  // --------------------------------------------------
  // دریافت یا ایجاد Cart
  // --------------------------------------------------

const fetchOrCreateCart = async () => {
  setLoading(true);

  try {
    // ---------------------------------------------
    // Authenticated user
    // ---------------------------------------------

    if (isAuthenticated) {
      const cartData = await cartService.getMyCart();

      setCart(cartData);

      if (cartData?.id) {
        localStorage.setItem("cart_id", cartData.id);
      }

      return;
    }

    // ---------------------------------------------
    // Guest user
    // ---------------------------------------------

    let cartId = localStorage.getItem("cart_id");

    if (!cartId) {
      const newCart = await cartService.createCart();

      cartId = newCart.id;

      localStorage.setItem("cart_id", cartId);

      setCart(newCart);

      return;
    }

    try {
      const cartData = await cartService.getCart(cartId);

      setCart(cartData);
    } catch (error) {
      if (error.response?.status === 404) {
        localStorage.removeItem("cart_id");

        const newCart = await cartService.createCart();

        localStorage.setItem(
          "cart_id",
          newCart.id
        );

        setCart(newCart);
      } else {
        throw error;
      }
    }

  } catch (error) {
    console.error(
      "Failed to fetch cart:",
      error.response?.data || error
    );

    setCart(null);

  } finally {
    setLoading(false);
  }
};
  // --------------------------------------------------
  // اجرای Cart loading هنگام تغییر وضعیت Authentication
  // --------------------------------------------------

useEffect(() => {
  if (authLoading) {
    return;
  }

  fetchOrCreateCart();
}, [isAuthenticated, authLoading]);

  // --------------------------------------------------
  // افزودن محصول به Cart
  // --------------------------------------------------

  const addToCart = async (productId) => {
    try {
      let cartId =
        cart?.id ||
        localStorage.getItem("cart_id");

      // اگر Cart نداریم، یک Cart ایجاد می‌کنیم
      if (!cartId) {
        const newCart =
          await cartService.createCart();

        cartId = newCart.id;

        localStorage.setItem(
          "cart_id",
          cartId
        );
      }

      try {
        await cartService.addItem(
          cartId,
          productId,
          1
        );
      } catch (error) {
        /*
         * ممکن است cart_id موجود در localStorage
         * دیگر در Backend وجود نداشته باشد.
         */

        const invalidCart =
          error.response?.status === 400 &&
          error.response?.data?.cart_id;

        if (!invalidCart) {
          throw error;
        }

        // Cart قدیمی را حذف می‌کنیم
        localStorage.removeItem("cart_id");

        // Cart جدید ایجاد می‌کنیم
        const newCart =
          await cartService.createCart();

        cartId = newCart.id;

        localStorage.setItem(
          "cart_id",
          cartId
        );

        // دوباره محصول را اضافه می‌کنیم
        await cartService.addItem(
          cartId,
          productId,
          1
        );
      }

      // دریافت وضعیت جدید Cart
      await fetchOrCreateCart();
    } catch (error) {
      console.error(
        "Failed to add item to cart:",
        error.response?.data || error
      );

      throw error;
    }
  };

  // --------------------------------------------------
  // تغییر تعداد محصول
  // --------------------------------------------------

  const updateQuantity = async (
    itemId,
    newQuantity
  ) => {
    if (newQuantity < 1) {
      return;
    }

    try {
      await cartService.updateItem(
        itemId,
        newQuantity
      );

      await fetchOrCreateCart();
    } catch (error) {
      console.error(
        "Failed to update cart item:",
        error.response?.data || error
      );

      throw error;
    }
  };

  // --------------------------------------------------
  // حذف محصول از Cart
  // --------------------------------------------------

  const removeFromCart = async (itemId) => {
    try {
      await cartService.removeItem(itemId);

      await fetchOrCreateCart();
    } catch (error) {
      console.error(
        "Failed to remove cart item:",
        error.response?.data || error
      );

      throw error;
    }
  };

  // --------------------------------------------------
  // پاک کردن وضعیت Cart در Frontend
  // --------------------------------------------------

  const clearCartState = () => {
    setCart(null);
    localStorage.removeItem("cart_id");
  };

  // --------------------------------------------------
  // تعداد کل محصولات Cart
  // --------------------------------------------------

  const totalItemsCount =
    cart?.items?.reduce(
      (total, item) =>
        total + item.quantity,
      0
    ) || 0;

  // --------------------------------------------------
  // Context
  // --------------------------------------------------

  return (
    <CartContext.Provider
      value={{
        cart,
        loading,
        totalItemsCount,
        addToCart,
        updateQuantity,
        removeFromCart,
        clearCartState,
        refreshCart: fetchOrCreateCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () =>
  useContext(CartContext);