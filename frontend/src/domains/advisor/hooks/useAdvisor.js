import { useState } from "react";

import advisorService from "../services/advisorService";

const useAdvisor = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const submitQuestion = async (question) => {
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

    try {
      const assistantMessage =
        await advisorService.askAdvisor(question);

      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: Date.now() + 1,
          ...assistantMessage,
        },
      ]);
    } catch (error) {
      console.error("Advisor error:", error);

      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: Date.now() + 1,
          role: "assistant",
          content:
            "Something went wrong. Please try again.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
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