import React, { useState } from "react";
import axios from "axios";

const Translation = () => {
  const [text, setText] = useState("");
  const [translatedText, setTranslatedText] = useState("");
  const [sourceLang, setSourceLang] = useState("en-IN");
  const [targetLang, setTargetLang] = useState("hi-IN");

  const handleTranslate = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/translate", { text, source_lang: sourceLang, target_lang: targetLang });
      setTranslatedText(res.data.translated_text);
    } catch (error) {
      console.error("Error translating:", error);
    }
  };

  return (
    <div>
      <h2>Translate Text</h2>
      <input type="text" value={text} onChange={(e) => setText(e.target.value)} placeholder="Enter text..." />
      <select value={sourceLang} onChange={(e) => setSourceLang(e.target.value)}>
        <option value="en-IN">English</option>
        <option value="hi-IN">Hindi</option>
      </select>
      <select value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
        <option value="hi-IN">Hindi</option>
        <option value="en-IN">English</option>
      </select>
      <button onClick={handleTranslate}>Translate</button>
      <p>Translation: {translatedText}</p>
    </div>
  );
};

export default Translation;
