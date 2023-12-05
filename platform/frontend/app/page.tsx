import Header from "./components/Header";
import FileUpload from "./components/FileUpload";
import { InfoBox } from "./components/InfoBox";
export default function Home() {
  return (
    <>
      <Header />
      <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gray-300">
        <InfoBox />
        <FileUpload />
      </main>
    </>
  );
}
