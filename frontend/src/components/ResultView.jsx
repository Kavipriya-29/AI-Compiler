function ResultView({
  response
}) {

  return (

    <div className="card">

      <h2>
        Generated Output
      </h2>

      <pre>
        {
          JSON.stringify(
            response,
            null,
            2
          )
        }
      </pre>

    </div>
  );
}

export default ResultView;