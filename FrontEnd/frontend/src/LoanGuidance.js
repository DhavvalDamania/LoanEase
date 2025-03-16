import React, { useState } from "react";
import axios from "axios";

const LoanGuidance = () => {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");

  const handleAskQuestion = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/loan_guidance", { question });
      setResponse(res.data.response);
    } catch (error) {
      console.error("Error fetching loan guidance:", error);
    }
  };

  return (
    <div>
      <h2>Loan Guidance</h2>
      <input type="text" value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask a question..." />
      <button onClick={handleAskQuestion}>Ask</button>
      <p>Response: {response}</p>
    </div>
  );
};

export default LoanGuidance;
