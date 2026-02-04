import ChatBox from "../components/ChatBox";
import Header from "../components/Header";

export default function HomePage() {
  return (
    <main className="page">
      <Header />
      <section className="hero">
        <div>
          <h1>AXIOM</h1>
          <p className="subtitle">Built by Cool Shot Systems</p>
          <p className="description">
            AXIOM is an AI model developed and operated by Cool Shot Systems.
          </p>
        </div>
      </section>
      <ChatBox />
    </main>
  );
}
