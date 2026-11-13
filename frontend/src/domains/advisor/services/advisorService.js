import apiClient from "../../../services/apiClient";


const createConversation = async () => {
  const response = await apiClient.post("/advisor/", {});

  return response.data;
};


const askAdvisor = async (conversationId, question) => {
  const response = await apiClient.post(
    `/advisor/${conversationId}/ask/`,
    {
      question,
    }
  );

  return response.data;
};


export default {
  createConversation,
  askAdvisor,
};