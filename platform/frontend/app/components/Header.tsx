"use client";

import React from "react";
import { Button } from "@mui/material";

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-semibold">
          Explainable AI Benchmarking Plattform
        </h1>
        <nav className="flex space-x-4">
          <Button variant="outlined"> Upload </Button>
          <Button variant="outlined">Display</Button>
          <div></div>

          <p>Login</p>

          <p>Settings</p>
        </nav>
      </div>
    </header>
  );
};

export default Header;
