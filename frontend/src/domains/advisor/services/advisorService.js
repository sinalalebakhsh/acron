const askAdvisor = async (question) => {
  console.log("Advisor service received:", question);

  return {
    role: "assistant",
    content: "I'm processing your question...",
  };
};

export default {
  askAdvisor,
};