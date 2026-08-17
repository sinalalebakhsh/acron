const AdvisorResponse = ({ messages }) => {
  if (!messages.length) {
    return null;
  }

  return (
    <section className="advisor-response">
      {messages.map((message) => (
        <div
          key={message.id}
          className={`advisor-message advisor-message-${message.role}`}
        >
          <p>{message.content}</p>
        </div>
      ))}
    </section>
  );
};

export default AdvisorResponse;