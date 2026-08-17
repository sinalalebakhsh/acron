import { useState } from "react";

import AdvisorHero from "../components/AdvisorHero";
import AdvisorInput from "../components/AdvisorInput";
import AdvisorSuggestions from "../components/AdvisorSuggestions";
import AdvisorResponse from "../components/AdvisorResponse";

const AdvisorPage = () => {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleQuestionSubmit = (question) => {
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

  const handleSuggestionSelect = (question) => {
    handleQuestionSubmit(question);
  };

  return (
    <main>
      <AdvisorHero />

      <AdvisorResponse messages={messages} />

      <AdvisorInput
        onSubmit={handleQuestionSubmit}
        disabled={isLoading}
      />

      <AdvisorSuggestions
        onSelect={handleSuggestionSelect}
      />
    </main>
  );
};

export default AdvisorPage;