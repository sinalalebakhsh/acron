import AdvisorHero from "../components/AdvisorHero";
import AdvisorInput from "../components/AdvisorInput";
import AdvisorSuggestions from "../components/AdvisorSuggestions";
import AdvisorResponse from "../components/AdvisorResponse";

import useAdvisor from "../hooks/useAdvisor";

const AdvisorPage = () => {
  const {
    messages,
    isLoading,
    submitQuestion,
    selectSuggestion,
  } = useAdvisor();

  return (
    <main>
      <AdvisorHero />

      <AdvisorResponse messages={messages} />

      <AdvisorInput
        onSubmit={submitQuestion}
        disabled={isLoading}
      />

      <AdvisorSuggestions
        onSelect={selectSuggestion}
      />
    </main>
  );
};

export default AdvisorPage;