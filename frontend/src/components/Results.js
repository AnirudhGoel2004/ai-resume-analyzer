import React from "react";

function Results({ result }) {
  return (
    <div>
      <h3>Resume Analysis Result</h3>
      <p>Score: {result.score}%</p>
      <h4>Matched Skills:</h4>
      <ul>
        {result.feedback.matched_skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
      <h4>Missing Skills:</h4>
      <ul>
        {result.feedback.missing_skills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}

export default Results;
