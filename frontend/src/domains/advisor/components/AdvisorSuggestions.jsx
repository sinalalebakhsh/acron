const suggestions = [
  "What products do you recommend?",
  "Show me my recent orders",
  "Help me find a product",
  "What can ACRON Advisor do?",
];

const AdvisorSuggestions = ({ onSelect }) => {
  return (
    <section className="advisor-suggestions">
      <h2>Suggested questions</h2>

      <div className="advisor-suggestions-list">
        {suggestions.map((suggestion) => (
          <button
            key={suggestion}
            type="button"
            onClick={() => onSelect(suggestion)}
          >
            {suggestion}
          </button>
        ))}
      </div>
    </section>
  );
};

export default AdvisorSuggestions;