import { useState } from "react";

function PromptForm({ setResponse }) {
  const [prompt, setPrompt] = useState("");

  async function generate() {
    try {
      const res = await fetch(
        "https://ai-compiler-81so.onrender.com/generate",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt,
          }),
        }
      );

      const data = await res.json();
      setResponse(data);
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to connect to backend");
    }
  }

  return (
    <div className="card">
      <textarea
        rows="8"
        value={prompt}
        placeholder="Enter requirements..."
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button onClick={generate}>
        Generate
      </button>
    </div>
  );
}

export default PromptForm;