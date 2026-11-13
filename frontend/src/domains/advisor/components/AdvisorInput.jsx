import { useState } from "react";

const AdvisorInput = ({ onSubmit, disabled = false }) => {
  const [question, setQuestion] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    const trimmedQuestion = question.trim();

    if (!trimmedQuestion || disabled) {
      return;
    }

    onSubmit(trimmedQuestion);

    setQuestion("");
  };

  return (
    <form onSubmit={handleSubmit} className="advisor-input">
      <input
        type="text"
        value={question}
        onChange={(event) => setQuestion(event.target.value)}
        placeholder="Ask ACRON Advisor..."
        disabled={disabled}
      />

      <button
        type="submit"
        disabled={disabled}
      >
        Ask
      </button>
    </form>
  );
};

export default AdvisorInput;