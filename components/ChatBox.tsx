"use client";

import { useEffect, useMemo, useRef, useState } from "react";

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

  const apiUrl = process.env.NEXT_PUBLIC_AXIOM_API_URL ?? "";
  const apiKey = process.env.NEXT_PUBLIC_AXIOM_API_KEY ?? "";

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
      if (!apiUrl || !apiKey) {
        throw new Error("Missing API configuration");
      }

      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: trimmed, max_tokens: 150 }),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = (await response.json()) as { response?: string };
      const content =
        typeof data.response === "string" && data.response.length > 0
          ? data.response
          : DEFAULT_ERROR;

      const axiomMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "axiom",
        content,
      };
      setMessages((prev) => [...prev, axiomMessage]);
    } catch (error) {
      const axiomMessage: ChatMessage = {
        id: crypto.randomUUID(),
        role: "axiom",
        content: DEFAULT_ERROR,
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
