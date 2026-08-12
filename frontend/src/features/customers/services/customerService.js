import apiClient from "../../../services/apiClient";

const customerService = {
  getAddresses: async () => {
    const response = await apiClient.get(
      "/customers/addresses/"
    );

    if (Array.isArray(response.data)) {
      return response.data;
    }

    if (Array.isArray(response.data?.results)) {
      return response.data.results;
    }

    return [];
  },
};

export default customerService;
