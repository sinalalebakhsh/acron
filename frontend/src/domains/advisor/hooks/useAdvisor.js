import { useEffect, useState } from "react";

import advisorService from "../services/advisorService";


const useAdvisor = () => {
  const [conversationId, setConversationId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isInitializing, setIsInitializing] = useState(true);


  useEffect(() => {
    const initializeConversation = async () => {
      try {
        const conversation =
          await advisorService.createConversation();

        setConversationId(conversation.id);
      } catch (error) {
        console.error(
          "Failed to create advisor conversation:",
          error
        );
      } finally {
        setIsInitializing(false);
      }
    };

    initializeConversation();
  }, []);


  const submitQuestion = async (question) => {
    if (!conversationId) {
      console.error(
        "Cannot submit question: conversation is not ready."
      );
      return;
    }

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
        await advisorService.askAdvisor(
          conversationId,
          question
        );

      setMessages((currentMessages) => [
        ...currentMessages,
        {
          id: assistantMessage.id,
          role: assistantMessage.role,
          content: assistantMessage.content,
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
    conversationId,
    messages,
    isLoading,
    isInitializing,
    submitQuestion,
    selectSuggestion,
  };
};


export default useAdvisor;