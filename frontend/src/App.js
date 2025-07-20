import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [nextWord, setNextWord] = useState("");
  const [history, setHistory] = useState([]);
  const [darkMode, setDarkMode] = useState(false);
    useEffect(() => {
  document.body.classList.toggle("dark", darkMode);
}, [darkMode]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handlePredict = async () => {
    if (!text.trim()) return;
    setLoading(true);
    setError("");
    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      if (data.next_word) {
        setNextWord(data.next_word);
        setHistory((prev) => [{ input: text, prediction: data.next_word }, ...prev]);
      } else {
        setError(data.error || "Prediction failed.");
      }
    } catch (err) {
      setError("⚠️ Error connecting to backend.");
    }
    setLoading(false);
  };

  const toggleDarkMode = () => setDarkMode(!darkMode);

  return (
    <div className="app">
      <header>
        <h1>Next-Word Predictor</h1>
        <button onClick={toggleDarkMode}>{darkMode ? "🌞 Light" : "🌙 Dark"}</button>
      </header>

      <main>
        <textarea
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Type a sentence..."
        />
        <button onClick={handlePredict} disabled={loading}>
          {loading ? "Predicting..." : "Predict Next Word"}
        </button>

        {nextWord && (
          <div className="result">
            <span>Next word might be:</span>
            <strong>{nextWord}</strong>
          </div>
        )}

        {error && <div className="error">{error}</div>}

        {history.length > 0 && (
          <div className="history">
            <h3>📝 History</h3>
            <ul>
              {history.map((item, i) => (
                <li key={i}>
                  <em>{item.input}</em> → <strong>{item.prediction}</strong>
                </li>
              ))}
            </ul>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
