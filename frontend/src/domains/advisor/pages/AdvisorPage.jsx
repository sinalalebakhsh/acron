import AdvisorHero from "../components/AdvisorHero";
import AdvisorInput from "../components/AdvisorInput";
import AdvisorSuggestions from "../components/AdvisorSuggestions";
import AdvisorResponse from "../components/AdvisorResponse";

import useAdvisor from "../hooks/useAdvisor";

const AdvisorPage = () => {
  const {
    messages,
    isLoading,
    isInitializing,
    submitQuestion,
    selectSuggestion,
  } = useAdvisor();

  const isBusy = isInitializing || isLoading;

  return (
    <main>
      <AdvisorHero />

      {isInitializing && (
        <p className="advisor-status">
          Initializing Advisor...
        </p>
      )}

      <AdvisorResponse messages={messages} />

      {isLoading && (
        <p className="advisor-status">
          Thinking...
        </p>
      )}

      <AdvisorInput
        onSubmit={submitQuestion}
        disabled={isBusy}
      />

      <AdvisorSuggestions
        onSelect={selectSuggestion}
        disabled={isBusy}
      />
    </main>
  );
};

export default AdvisorPage;
