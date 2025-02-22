import Chat from "../components/Chat";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-6">Chatbot AI</h1>
      <Chat />
    </main>
  );
}
