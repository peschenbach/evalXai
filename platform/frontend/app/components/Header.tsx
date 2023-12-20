"use client";

import React from "react";
import { Button } from "@mui/material";
import useSwitchMode from "../zustand/useSwitchMode";

const Header: React.FC = () => {
  const mode = useSwitchMode((state) => state.mode);
  const setMode = useSwitchMode((state) => state.setMode);
  return (
    <header className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-semibold">
          Explainable AI Benchmarking Plattform
        </h1>
        <nav className="flex space-x-4">
          <Button
            variant="outlined"
            className={mode === "Upload" ? "bg-gray-950" : ""}
            onClick={() => setMode("Upload")}
          >
            Upload
          </Button>
          <Button
            variant="outlined"
            className={mode === "Display" ? "bg-gray-950" : ""}
            onClick={() => setMode("Display")}
          >
            Display
          </Button>
          <div></div>

          <p>Login</p>

          <p>Settings</p>
        </nav>
      </div>
    </header>
  );
};

export default Header;
