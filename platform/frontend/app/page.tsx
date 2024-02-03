import React from "react";
import Header from "./components/Header";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex flex-1 flex-col items-center justify-center p-24 bg-gray-300">
        <h1 className="text-4xl font-bold mb-4"> Welcome</h1>
        <p className="text-lg mb-8">
          Explore and participate in Explainable AI Benchmarking Challenges.
        </p>
      </main>
      <footer className="w-full bg-gray-800 text-white text-center p-4">
        <p>© 2023 A TUB Project - Explainable AI Project.</p>
      </footer>
    </div>
  );
}
