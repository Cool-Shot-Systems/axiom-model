"use client";

import { useEffect, useMemo, useRef, useState } from "react";

import { generateResponse } from "../lib/api";
import MessageBubble from "./MessageBubble";

type ChatMessage = {
  id: string;
  role: "user" | "axiom";
  content: string;
};

const DEFAULT_ERROR =
  "We were unable to generate a response right now. Please try again.";

export default function ChatBox() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight });
  }, [messages, loading]);

  const canSend = useMemo(() => {
    return Boolean(input.trim()) && !loading;
  }, [input, loading]);

  const handleSend = async () => {
    if (!canSend) {
      return;
    }

    const trimmed = input.trim();
    const userMessage: ChatMessage = {
      id: crypto.randomUUID(),
      role: "user",
      content: trimmed,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const responseText = await generateResponse(trimmed);
      const axiomMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "axiom",
        content: responseText || DEFAULT_ERROR,
      };
      setMessages((prev) => [...prev, axiomMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="chat">
      <div className="chat__window" ref={scrollRef}>
        {messages.length === 0 ? (
          <div className="chat__empty">
            Start a conversation with AXIOM.
          </div>
        ) : (
          messages.map((message) => (
            <MessageBubble
              key={message.id}
              role={message.role}
              content={message.content}
            />
          ))
        )}
        {loading && <div className="chat__loading">AXIOM is thinking…</div>}
      </div>
      <div className="chat__input">
        <textarea
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="Ask AXIOM a question..."
          rows={3}
        />
        <button type="button" onClick={handleSend} disabled={!canSend}>
          Send
        </button>
      </div>
    </section>
  );
}
