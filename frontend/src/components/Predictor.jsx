import React, { useState } from "react";
import axios from "axios";

const Predictor = () => {
  const [input, setInput] = useState("");
  const [nextWord, setNextWord] = useState("");

  const handlePredict = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", {
        text: input,
      });
      setNextWord(res.data.next_word);
    } catch (error) {
      setNextWord("Error predicting word.");
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Next Word Predictor</h1>
      <input
        type="text"
        className="border p-2 w-full mb-2"
        placeholder="Type a sentence..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded"
        onClick={handlePredict}
      >
        Predict
      </button>
      {nextWord && (
        <p className="mt-4 text-lg">
          <strong>Next word:</strong> {nextWord}
        </p>
      )}
    </div>
  );
};

export default Predictor;
