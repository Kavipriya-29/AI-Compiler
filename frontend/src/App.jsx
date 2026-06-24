import { useState } from "react";

import PromptForm from "./components/PromptForm";
import PipelineView from "./components/PipelineView";
import ResultView from "./components/ResultView";
import MetricsView from "./components/MetricsView";

function App() {

  const [response, setResponse] = useState(null);

  return (
    <div className="container">

      <h1>
        🚀 AI Compiler for Software Generation
      </h1>

      <p
        style={{
          textAlign: "center",
          color: "#94a3b8"
        }}
      >
        Natural Language → Architecture → Schema → Validation → Executable App
      </p>

      <PromptForm setResponse={setResponse} />

      {response && (
        <>
          <PipelineView />

          <ResultView
            response={response}
          />

          <MetricsView
            metrics={response.metrics}
          />
        </>
      )}

    </div>
  );
}

export default App;