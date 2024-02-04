import React from "react";
import FileUpload from "./FileUpload";
import { Button } from "@mui/material";

interface SingleCompetitionProps {
  competitionName: string;
}

export const SingleCompetition = (props: SingleCompetitionProps) => {
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
              <Button
                variant="contained"
                color="primary"
                className="m-5 bg-red bg-gray-800"
              >
                Download ML Model
              </Button>
              <Button
                variant="contained"
                color="primary"
                className="m-5 bg-gray-800"
              >
                Download Dataset
              </Button>
            </div>
          </div>

          <FileUpload />
        </main>
      </div>
    </>
  );
};
