import React from "react";
import LoanGuidance from "./components/LoanGuidance";
import Translation from "./components/Translation";
import SpeechToText from "./components/SpeechToText";
import TextToSpeech from "./components/TextToSpeech";
import "./App.css";

function App() {
  return (
    <div className="container">
      <h1 className="title">Loan Assistant</h1>
      <div className="section">
        <LoanGuidance />
      </div>
      <div className="section">
        <Translation />
      </div>
      <div className="section">
        <SpeechToText />
      </div>
      <div className="section">
        <TextToSpeech />
      </div>
    </div>
  );
}

export default App;
