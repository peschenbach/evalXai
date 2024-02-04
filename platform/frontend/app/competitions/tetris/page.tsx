import React from "react";
import { SingleCompetition } from "@/app/components/SingleCompetition";
import Header from "@/app/components/Header";

const CompetitionPage = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex flex-1 flex-col items-center justify-center p-24 bg-gray-300">
        <SingleCompetition competitionName={"Tetris"} />
      </main>
      <footer className="w-full bg-gray-800 text-white text-center p-4">
        <p>© 2023 A TUB Project - Explainable AI Project.</p>
      </footer>
    </div>
  );
};

export default CompetitionPage;
