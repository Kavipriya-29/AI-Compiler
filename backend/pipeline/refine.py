def refine_schema(schema):

    assumptions = []

    assumptions.append(
        "Default authentication enabled"
    )

    assumptions.append(
        "SQLite used as default database"
    )

    if "admin" in schema["auth"]:

        assumptions.append(
            "Admin role created automatically"
        )

    if "/payments" in schema["api"]:

        assumptions.append(
            "Payment gateway assumed as Stripe"
        )

    schema["assumptions"].extend(
        assumptions
    )

    return schema