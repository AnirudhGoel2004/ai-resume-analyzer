import React, { useRef } from "react";

function FileUpload({ onUpload }) {
  const fileInputRef = useRef(null);

  const handleFileUpload = () => {
    const file = fileInputRef.current.files[0];
    if (file) {
      onUpload(file);
    }
  };

  return (
    <div>
      <input type="file" ref={fileInputRef} onChange={handleFileUpload} />
    </div>
  );
}

export default FileUpload;
