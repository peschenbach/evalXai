"use client";

import React from "react";
import FileUpload from "./FileUpload";
import { Button } from "@mui/material";
import axios from "axios";

interface SingleCompetitionProps {
  competitionName: string;
}

export const SingleCompetition = (props: SingleCompetitionProps) => {
  const getMLModel = async () => {
    const challengeId = 1;
    try {
      const response = await axios.get(
        `localhost:8000/api/dataset/${challengeId}/`,
        { responseType: "blob" }
      );
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", "model.pkl");
      document.body.appendChild(link);
      link.click();
      console.log(response.data);
    } catch (error) {
      console.error("Error fetching ML model:", error);
    }
  };

  return (
    <>
      <div className="flex flex-col min-h-screen">
        <main className="flex flex-1 flex-col items-center justify-center p-24 bg-gray-300">
          <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg mb-20">
            <h2 className="text-2xl font-semibold mb-4 text-center">
              {props.competitionName} Competition
            </h2>
            <p>
              You can start by uploading a file. The file will be processed and
              stored in a database.
            </p>
            <div className="mt-5 flex justify-center">
              <a href="http://localhost:8000/api/mlmodel/1">
                <Button
                  variant="contained"
                  color="primary"
                  className="m-5 bg-red bg-gray-800"
                >
                  Download ML Model
                </Button>
              </a>
              <a href="http://localhost:8000/api/dataset/1">
                <Button
                  variant="contained"
                  color="primary"
                  className="m-5 bg-gray-800"
                >
                  Download Dataset
                </Button>
              </a>
            </div>
          </div>

          <FileUpload />
        </main>
      </div>
    </>
  );
};
