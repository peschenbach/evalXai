import Header from "./components/Header";
import FileUpload from "./components/FileUpload";
import { InfoBox } from "./components/InfoBox";

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex flex-1 flex-col items-center justify-center p-24 bg-gray-300">
        <InfoBox />
        <FileUpload />
      </main>
      <footer className="w-full bg-gray-800 text-white text-center p-4">
        <p>© 2023 A TUB Project - Explainable AI Project.</p>
      </footer>
    </div>
  );
}
