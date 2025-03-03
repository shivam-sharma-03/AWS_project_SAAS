import React, { useState } from "react";
import { Loader2, Copy } from "lucide-react";
import "./App.css";

export default function SarcasmRoaster() {
  const [roast, setRoast] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);
  const [darknessLevel, setDarknessLevel] = useState("low");
  const [language, setLanguage] = useState("en");

  const API_URL =
    "https://gbb43ddqba.execute-api.eu-north-1.amazonaws.com/prod_v1/sarcasm";

  const generateRoast = async () => {
    if (!roast.trim()) return;
    setLoading(true);
    setResponse("");

    const requestBody = { roast, level: darknessLevel, language };
    console.log("Sending request:", requestBody); // Log request payload

    try {
      const res = await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody),
      });

      const data = await res.json();
      console.log("API Response:", data); // Log API response

      setResponse(data.reply || "Something went wrong. Try again!");
    } catch (error) {
      console.error("API Error:", error);
      setResponse("Error fetching response. Check API Gateway.");
    }
    setLoading(false);
  };

  const copyToClipboard = () => {
    navigator.clipboard.writeText(response);
  };

  return (
    <div className="app-container">
      <h1 className="app-title">🔥 Sarcasm As A Service</h1>

      <div className="input-container">
        <input
          type="text"
          placeholder="Enter a roast..."
          value={roast}
          onChange={(e) => setRoast(e.target.value)}
          className="roast-input"
        />
        <button
          onClick={generateRoast}
          disabled={loading}
          className="roast-button"
        >
          {loading ? <Loader2 className="animate-spin" /> : "Find Comeback"}
        </button>

        <div className="level-selection-box">
          <span className="level-label">Darkness Level:</span>
          <div className="darkness-selector">
            <button
              onClick={() => setDarknessLevel("low")}
              className={`darkness-button ${darknessLevel === "low" ? "active" : ""}`}
            >
            
            </button>
            <span className="Low-label">Low</span>
            <button
              onClick={() => setDarknessLevel("mid")}
              className={`darkness-button ${darknessLevel === "mid" ? "active" : ""}`}
            >
              
            </button>
            <span className="Low-label">Mid</span>
            <button
              onClick={() => setDarknessLevel("max")}
              className={`darkness-button ${darknessLevel === "max" ? "active" : ""}`}
            >
              
            </button>
            <span className="Low-label">Max</span>
          </div>
        </div>

        <div className="language-toggle">
          <span>English</span>
          <label className="switch">
            <input
              type="checkbox"
              checked={language === "hi"}
              onChange={() => setLanguage(language === "en" ? "hi" : "en")}
            />
            <span className="slider round"></span>
          </label>
          <span>Hindi</span>
        </div>
      </div>

      {response && (
        <div className="response-container">
          <div className="response-content">
            <span>{response}</span>
            <button onClick={copyToClipboard} className="copy-button">
              <Copy size={18} />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
