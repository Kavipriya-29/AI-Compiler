import { useState } from "react";

function PromptForm({ setResponse }) {

  const [prompt, setPrompt] =
    useState("");

  async function generate() {

    const res =
      await fetch(
        "http://127.0.0.1:8000/generate",
        {
          method:"POST",

          headers:{
            "Content-Type":
            "application/json"
          },

          body:JSON.stringify({
            prompt
          })
        }
      );

    const data =
      await res.json();

    setResponse(data);
  }

  return (

    <div className="card">

      <textarea
        rows="8"
        value={prompt}
        placeholder="Enter requirements..."
        onChange={(e)=>
          setPrompt(
            e.target.value
          )
        }
      />

      <button
        onClick={generate}
      >
        Generate
      </button>

    </div>
  );
}

export default PromptForm;