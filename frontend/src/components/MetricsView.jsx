function MetricsView({ metrics }) {

  return (

    <div className="card">

      <h2>
        📊 Metrics
      </h2>

      <p>
        <strong>Requests:</strong>{" "}
        {metrics.requests}
      </p>

      <p>
        <strong>Failures:</strong>{" "}
        {metrics.failures}
      </p>

      <p>
        <strong>Success Rate:</strong>{" "}
        {metrics.success_rate}%
      </p>

      <p>
        <strong>Runtime Validation Score:</strong>{" "}
        {metrics.runtime_validation_score}
      </p>

      <p>
        <strong>Average Latency:</strong>{" "}
        {metrics.average_latency_ms} ms
      </p>

      <p>
        <strong>Repair Rate:</strong>{" "}
        {metrics.repair_rate}
      </p>

      <p>
        <strong>Failure Types:</strong>{" "}
        {
          metrics.failure_types &&
          metrics.failure_types.length > 0
            ? metrics.failure_types.join(", ")
            : "None"
        }
      </p>

    </div>
  );
}

export default MetricsView;