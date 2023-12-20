import React from "react";
import { Button } from "@mui/material";
import axios from "axios";

function getResults() {
  let result = "";
  console.log("Test");
  return result;
}

export const Display = () => {
  return (
    <>
      <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-center">
          Display your results
        </h2>
        <div className="text-center">
          <Button
            variant="contained"
            className="bg-gray-800"
            onClick={getResults}
          >
            Get Results
          </Button>
        </div>
      </div>
    </>
  );
};

export default Display;
