import apiClient from "../../../services/apiClient";

const orderService = {
  // دریافت سفارش‌های کاربر جاری
  getOrders: async () => {
    const response = await apiClient.get("/orders/");

    // Django REST Framework ممکن است پاسخ paginated برگرداند:
    // {
    //   count: ...,
    //   next: ...,
    //   previous: ...,
    //   results: [...]
    // }
    //
    // یا در صورت غیرفعال بودن pagination مستقیماً آرایه برگرداند.
    if (Array.isArray(response.data)) {
      return response.data;
    }

    if (Array.isArray(response.data?.results)) {
      return response.data.results;
    }

    return [];
  },

  // دریافت یک سفارش مشخص
  getOrder: async (orderId) => {
    const response = await apiClient.get(`/orders/${orderId}/`);
    return response.data;
  },

  // ایجاد سفارش از روی سبد خرید
  createOrder: async (cartId, addressId) => {
    const response = await apiClient.post("/orders/", {
      cart_id: cartId,
      address_id: addressId,
    });

    return response.data;
  },

  // پرداخت یک سفارش
  payOrder: async (orderId) => {
    const response = await apiClient.post(
      `/orders/${orderId}/pay/`
    );

    return response.data;
  },
};

export default orderService;

