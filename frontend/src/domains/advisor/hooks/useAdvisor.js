import { useState } from "react";

const useAdvisor = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const submitQuestion = (question) => {
    const userMessage = {
      id: Date.now(),
      role: "user",
      content: question,
    };

    setMessages((currentMessages) => [
      ...currentMessages,
      userMessage,
    ]);

    setIsLoading(true);

    setTimeout(() => {
      const assistantMessage = {
        id: Date.now() + 1,
        role: "assistant",
        content: "I'm processing your question...",
      };

      setMessages((currentMessages) => [
        ...currentMessages,
        assistantMessage,
      ]);

      setIsLoading(false);
    }, 1000);
  };

  const selectSuggestion = (question) => {
    submitQuestion(question);
  };

  return {
    messages,
    isLoading,
    submitQuestion,
    selectSuggestion,
  };
};

export default useAdvisor;