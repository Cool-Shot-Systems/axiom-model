type MessageBubbleProps = {
  role: "user" | "axiom";
  content: string;
};

export default function MessageBubble({ role, content }: MessageBubbleProps) {
  const isUser = role === "user";
  return (
    <div className={`message message--${role}`}>
      <div className="message__meta">{isUser ? "You" : "AXIOM"}</div>
      <div className="message__content">{content}</div>
    </div>
  );
}
