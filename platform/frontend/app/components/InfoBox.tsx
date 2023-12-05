import React from "react";

export const InfoBox = () => {
  return (
    <>
      <div className="w-full max-w-3xl mx-auto bg-white shadow-md p-8 rounded-lg mb-20">
        <h2 className="text-2xl font-semibold mb-4 text-center">Welcome!</h2>
        <p>
          You can start by uploading a file. The file will be processed and
          stored in a database.
        </p>
      </div>
    </>
  );
};
