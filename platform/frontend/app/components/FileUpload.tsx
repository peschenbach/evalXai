import React, { useRef, useState, ChangeEvent } from "react";
import Button from "@mui/material/Button";
import axios, { AxiosError } from "axios";

export const FileUpload = () => {
  const [uploadStatus, setUploadStatus] = useState<string>("");
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileUpload = async (event: ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (files && files.length > 0) {
      const selectedFile = files[0];
      const formData = new FormData();
      formData.append("file", selectedFile);

      try {
        const response = await axios.post(
          "http://localhost:8000/api/xai/1/",
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        );
        setUploadStatus(
          `File uploaded successfully: ${JSON.stringify(response.data)}`
        );
      } catch (error) {
        let errorMessage = "An error occurred";
        if (axios.isAxiosError(error)) {
          errorMessage = `Error uploading file: ${
            error.response ? JSON.stringify(error.response.data) : errorMessage
          }`;
        }
        setUploadStatus(errorMessage);
      }
    }
  };

  const handleButtonClick = () => {
    fileInputRef.current?.click();
  };

  return (
    <>
      <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg">
        <h2 className="text-2xl font-semibold mb-4 text-center">
          Upload your file
        </h2>
        <div className="flex justify-center">
          <input
            type="file"
            onChange={handleFileUpload}
            style={{ display: "none" }}
            ref={fileInputRef}
          />

          <Button
            variant="contained"
            color="primary"
            className="bg-blue-500"
            onClick={handleButtonClick}
          >
            Select and Upload File
          </Button>
        </div>
        {uploadStatus && <p>{uploadStatus}</p>}
      </div>
    </>
  );
};

export default FileUpload;
