import axiosInstance from "../../../api/axiosInstance";

export async function getProducts(page = 1) {
  const response = await axiosInstance.get("products/", {
    params: {
      page,
    },
  });

  return response.data;
}

export async function getProductBySlug(slug) {
  const response = await axiosInstance.get(
    `products/${slug}/`
  );

  return response.data;
}