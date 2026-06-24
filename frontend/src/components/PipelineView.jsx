function PipelineView() {

  const stages = [
  "Intent Extraction",
  "System Design",
  "Schema Generation",
  "Validation",
  "Repair Engine",
  "Runtime Execution"
];

  return (

    <div className="card">

      <h2>
        Compiler Pipeline
      </h2>

      <div className="pipeline">

        {
          stages.map(
            (stage,index)=>(
              <div
                key={index}
                className="stage"
              >
                {stage}
              </div>
            )
          )
        }

      </div>

    </div>
  );
}

export default PipelineView;