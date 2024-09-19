import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import Results from "./components/Results";
import axios from "axios";

function App() {
  const [resumeText, setResumeText] = useState(null);
  const [jobKeywords, setJobKeywords] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);

  const handleResumeUpload = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("/upload-resume", formData);
    setResumeText(response.data.resume_text);
  };

  const handleJobDescriptionSubmit = async (jobDescription) => {
    const response = await axios.post("/upload-job-description", {
      job_description: jobDescription,
    });
    setJobKeywords(response.data.job_keywords);
  };

  const analyzeResume = async () => {
    const response = await axios.post("/analyze", {
      resume_text: resumeText,
      job_keywords: jobKeywords,
    });
    setAnalysisResult(response.data);
  };

  return (
    <div>
      <FileUpload onUpload={handleResumeUpload} />
      <textarea
        onBlur={(e) => handleJobDescriptionSubmit(e.target.value)}
        placeholder="Paste Job Description"
      />
      <button onClick={analyzeResume}>Analyze Resume</button>
      {analysisResult && <Results result={analysisResult} />}
    </div>
  );
}

export default App;
