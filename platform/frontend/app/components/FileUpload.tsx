"use client";
import React, { useState, ChangeEvent, DragEvent, useEffect } from "react";
import Button from "@mui/material/Button";
import axios from "axios";

const uploadFile = async (
  file: File,
  setUploadStatus: React.Dispatch<React.SetStateAction<string>>,
  setPrediction: React.Dispatch<React.SetStateAction<Number[]>>
) => {
  const content = await file.text();
  const jsonData = JSON.parse(content);
  console.log("Uploaded jsonData: ", jsonData);
  try {
    const response = await axios.post(
      "http://localhost:8000/api/prediction/",
      jsonData,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );

    console.log("File successfully uploaded", response.data);
    setUploadStatus("✅ File successfully uploaded!");
    setPrediction(response.data.prediction);
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      console.error("Upload failed", error.response.data);
      setUploadStatus("❌ File upload was not successful.");
    } else {
      console.error("Error during file upload", error);
      setUploadStatus("❌ File upload was not successful.");
    }
  }
};

export const FileUpload: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [uploadStatus, setUploadStatus] = useState<string>("");
  const [prediction, setPrediction] = useState<Number[]>([]);
  const [formattedPrediction, setFormattedPrediction] = useState<string>("");

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files ? event.target.files[0] : null;
    if (file) {
      setSelectedFile(file);
      uploadFile(file, setUploadStatus, setPrediction);
    }
  };

  const handleButtonClick = () => {
    document.getElementById("fileInput")?.click();
  };

  const handleDrop = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    if (file) {
      setSelectedFile(file);
      uploadFile(file, setUploadStatus, setPrediction);
    }
  };

  const handleDragOver = (event: DragEvent<HTMLDivElement>) => {
    event.preventDefault();
  };

  useEffect(() => {
    if (prediction.length > 0) {
      setFormattedPrediction("[" + prediction.join(", ") + "]");
    } else {
      setFormattedPrediction("");
    }
  }, [prediction]);

  return (
    <>
      <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-center">
          Upload your file
        </h2>
        <div
          className="flex flex-col items-center justify-center border-2 border-dashed border-gray-300 p-10 rounded-lg mb-4"
          onDrop={handleDrop}
          onDragOver={handleDragOver}
        >
          <p className="text-gray-500 mb-3">Drag and drop your file here</p>
          <input
            type="file"
            id="fileInput"
            style={{ display: "none" }}
            onChange={handleFileChange}
          />
          <Button
            variant="contained"
            size="large"
            className="bg-gray-800"
            onClick={handleButtonClick}
          >
            Browse Files
          </Button>
        </div>
        {selectedFile && (
          <p className="text-center ">File selected: {selectedFile.name}</p>
        )}
        {uploadStatus && <p className="text-center mt-4">{uploadStatus}</p>}
        {formattedPrediction && (
          <p className="text-center mt-4">Prediction: {formattedPrediction}</p>
        )}
      </div>
    </>
  );
};

export default FileUpload;
