import axiosInstance from "../api/axiosInstance";

const cartService = {
  // دریافت سبد خرید کاربر لاگین‌شده
  getMyCart: async () => {
    const response = await axiosInstance.get("carts/mine/");
    return response.data;
  },

  // ایجاد سبد خرید جدید
  createCart: async () => {
    const response = await axiosInstance.post("carts/");
    return response.data;
  },

  // دریافت سبد خرید با ID
  getCart: async (cartId) => {
    const response = await axiosInstance.get(`carts/${cartId}/`);
    return response.data;
  },

  // افزودن محصول به سبد خرید
  addItem: async (cartId, productId, quantity = 1) => {
    const response = await axiosInstance.post("carts/cart-items/", {
      cart_id: cartId,
      product_id: productId,
      quantity,
    });

    return response.data;
  },

  // تغییر تعداد یک آیتم
  updateItem: async (itemId, quantity) => {
    const response = await axiosInstance.patch(
      `carts/cart-items/${itemId}/`,
      {
        quantity,
      }
    );

    return response.data;
  },

  // حذف آیتم
  removeItem: async (itemId) => {
    await axiosInstance.delete(
      `carts/cart-items/${itemId}/`
    );
  },
};

export default cartService;