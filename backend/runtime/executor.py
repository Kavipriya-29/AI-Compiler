def simulate_execution(schema):

    pages = len(
        schema["ui"]["pages"]
    )

    apis = len(
        schema["api"]
    )

    tables = len(
        schema["database"]["tables"]
    )

    roles = len(
        schema["auth"]
    )

    assumptions = len(
        schema.get(
            "assumptions",
            []
        )
    )

    repair_count = schema.get(
        "repair_count",
        0
    )

    components = 0

    for page in schema["ui"]["pages"]:

        components += len(
            page.get(
                "components",
                []
            )
        )

    executable = (

        pages > 0 and
        apis > 0 and
        tables > 0 and
        roles > 0
    )

    complexity_score = (

        (pages * 2) +
        (apis * 3) +
        (tables * 4) +
        (roles * 2) +
        components
    )

    validation_score = min(

        100,

        round(

            60 +

            (pages * 3) +

            (apis * 3) +

            (tables * 4) +

            (roles * 2)

        )
    )

    architecture_score = min(

        100,

        round(

            (
                pages +
                apis +
                tables +
                roles +
                components
            )

            * 2

        )
    )

    if validation_score >= 90:

        readiness = "PRODUCTION_READY"

    elif validation_score >= 75:

        readiness = "DEPLOYABLE"

    elif validation_score >= 50:

        readiness = "PARTIALLY_READY"

    else:

        readiness = "NEEDS_REPAIR"

    runtime_health = "HEALTHY"

    if repair_count > 0:

        runtime_health = "REPAIRED"

    if not executable:

        runtime_health = "FAILED"

    return {

        "status":

        "SUCCESS"
        if executable
        else "FAILED",

        "pages":
        pages,

        "apis":
        apis,

        "tables":
        tables,

        "roles":
        roles,

        "components":
        components,

        "assumptions":
        assumptions,

        "repair_count":
        repair_count,

        "complexity_score":
        complexity_score,

        "architecture_score":
        architecture_score,

        "validation_score":
        validation_score,

        "build_readiness":
        readiness,

        "runtime_health":
        runtime_health,

        "executable":
        executable
    }