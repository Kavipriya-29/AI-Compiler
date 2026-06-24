import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import PromptRequest

from pipeline.intent import extract_intent
from pipeline.design import system_design
from pipeline.schema import generate_schema
from pipeline.validate import validate_schema
from pipeline.repair import repair_schema
from pipeline.refine import refine_schema

from runtime.executor import simulate_execution
from evaluation.metrics import metrics

app = FastAPI(
    title="AI Compiler",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():

    return {

        "status": "running",

        "service": "AI Compiler",

        "version": "1.0.0"
    }


@app.post("/generate")
def generate(req: PromptRequest):

    start_time = metrics.record()

    try:

        # -------------------------
        # STEP 1 - Intent Extraction
        # -------------------------

        intent = extract_intent(
            req.prompt
        )

        # -------------------------
        # STEP 2 - System Design
        # -------------------------

        design = system_design(
            intent
        )

        # -------------------------
        # STEP 3 - Schema Generation
        # -------------------------

        schema = generate_schema(
            design
        )

        # -------------------------
        # STEP 4 - Refinement
        # -------------------------

        schema = refine_schema(
            schema
        )

        # -------------------------
        # STEP 5 - Validation
        # -------------------------

        errors = validate_schema(
            schema
        )

        repaired = False

        if len(errors) > 0:

            repaired = True

            metrics.record_repair()

            schema = repair_schema(
                schema,
                errors
            )

        # -------------------------
        # STEP 6 - Runtime Execution
        # -------------------------

        runtime = simulate_execution(
            schema
        )

        # -------------------------
        # Runtime Health
        # -------------------------

        if runtime["validation_score"] >= 90:

            runtime["runtime_health"] = "HEALTHY"

        elif runtime["validation_score"] >= 75:

            runtime["runtime_health"] = "STABLE"

        else:

            runtime["runtime_health"] = "UNSTABLE"

        # -------------------------
        # Metrics
        # -------------------------

        latency = round(
            (
                time.time()
                - start_time
            ) * 1000,
            2
        )

        metrics.add_latency(
            latency
        )

        metrics.set_validation_score(
            runtime["validation_score"]
        )

        return {

            "intent": intent,

            "design": design,

            "schema": schema,

            "validation_errors": errors,

            "repaired": repaired,

            "runtime": runtime,

            "metrics": metrics.report()
        }

    except Exception as e:

        latency = round(
            (
                time.time()
                - start_time
            ) * 1000,
            2
        )

        metrics.add_latency(
            latency
        )

        metrics.fail(
            str(
                type(e).__name__
            )
        )

        return {

            "status": "FAILED",

            "error": str(e),

            "metrics": metrics.report()
        }


@app.get("/metrics")
def get_metrics():

    return metrics.report()


@app.get("/health")
def health():

    return {

        "status": "healthy",

        "requests": metrics.requests,

        "failures": metrics.failures
    }