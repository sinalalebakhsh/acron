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
  const { isAuthenticated } = useAuth();

  const [cart, setCart] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchOrCreateCart = async () => {
    setLoading(true);

    try {
      // کاربر لاگین شده
      if (isAuthenticated) {
        const cartData = await cartService.getMyCart();

        setCart(cartData);

        if (cartData?.id) {
          localStorage.setItem("cart_id", cartData.id);
        }

        return;
      }

      // کاربر مهمان
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

          localStorage.setItem("cart_id", newCart.id);

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

  useEffect(() => {
    fetchOrCreateCart();
  }, [isAuthenticated]);

  const addToCart = async (productId) => {
    try {
      let cartId =
        cart?.id ||
        localStorage.getItem("cart_id");

      if (!cartId) {
        const newCart = await cartService.createCart();

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
        const invalidCart =
          error.response?.status === 400 &&
          error.response?.data?.cart_id;

        if (!invalidCart) {
          throw error;
        }

        localStorage.removeItem("cart_id");

        const newCart =
          await cartService.createCart();

        cartId = newCart.id;

        localStorage.setItem(
          "cart_id",
          cartId
        );

        await cartService.addItem(
          cartId,
          productId,
          1
        );
      }

      await fetchOrCreateCart();
    } catch (error) {
      console.error(
        "Failed to add item to cart:",
        error.response?.data || error
      );

      throw error;
    }
  };

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

  const clearCartState = () => {
    setCart(null);
  };

  const totalItemsCount =
    cart?.items?.reduce(
      (total, item) =>
        total + item.quantity,
      0
    ) || 0;

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