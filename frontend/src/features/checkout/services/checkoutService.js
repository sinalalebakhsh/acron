import apiClient from "../../../services/apiClient";

const checkoutService = {
  // دریافت آدرس‌های مشتری جاری
  getAddresses: async () => {
    const response = await apiClient.get("/customers/addresses/");

    if (Array.isArray(response.data)) {
      return response.data;
    }

    if (Array.isArray(response.data?.results)) {
      return response.data.results;
    }

    return [];
  },

  // ثبت سفارش جدید بر اساس سبد خرید و آدرس انتخاب‌شده
  createOrder: async (cartId, addressId) => {
    const response = await apiClient.post("/orders/", {
      cart_id: cartId,
      address_id: addressId,
    });

    return response.data;
  },
};

export default checkoutService;