import React from "react";
import Button from "@mui/material/Button";

export const FileUpload = () => {
  return (
    <>
      <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-center">
          Upload your file
        </h2>
        <div className="flex flex-col items-center justify-center border-2 border-dashed border-gray-300 p-10 rounded-lg mb-4">
          <p className="text-gray-500 mb-3">Drag and drop your file here</p>
          <Button variant="contained" size="large" className="bg-gray-800">
            Browse Files
          </Button>
        </div>
      </div>
    </>
  );
};

export default FileUpload;
