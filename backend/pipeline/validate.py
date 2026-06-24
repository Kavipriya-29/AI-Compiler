def validate_schema(schema):

    errors = []

    # Required Sections

    required = [
        "ui",
        "api",
        "database",
        "auth"
    ]

    for key in required:

        if key not in schema:

            errors.append(
                f"{key} missing"
            )

    if errors:

        return errors

    # Load Objects

    tables = schema["database"].get(
        "tables",
        {}
    )

    apis = schema.get(
        "api",
        {}
    )

    pages = schema.get(
        "ui",
        {}
    ).get(
        "pages",
        []
    )

    auth = schema.get(
        "auth",
        {}
    )

    # API -> DB Validation

    for endpoint in apis:

        entity = endpoint.replace("/", "")

        if entity == "login":

            continue

        if entity not in tables:

            errors.append(
                f"{entity} api without matching table"
            )

    # DB -> API Validation

    for table in tables:

        endpoint = f"/{table}"

        if endpoint not in apis:

            errors.append(
                f"{table} table without api"
            )

    # Page Validation

    if len(pages) == 0:

        errors.append(
            "no pages generated"
        )

    page_names = []

    for page in pages:

        page_name = page.get(
            "name",
            ""
        )

        if page_name == "":

            errors.append(
                "page name missing"
            )

        if page_name in page_names:

            errors.append(
                f"duplicate page {page_name}"
            )

        page_names.append(
            page_name
        )

        if "components" not in page:

            errors.append(
                f"{page_name} page missing components"
            )

        elif len(
            page["components"]
        ) == 0:

            errors.append(
                f"{page_name} page has no components"
            )

    # Database Validation

    if len(tables) == 0:

        errors.append(
            "no database tables generated"
        )

    for table_name, fields in tables.items():

        if len(fields) == 0:

            errors.append(
                f"{table_name} table has no fields"
            )

        if "id" not in fields:

            errors.append(
                f"{table_name} table missing primary key"
            )

    # API Validation

    if len(apis) == 0:

        errors.append(
            "no apis generated"
        )

    for endpoint, config in apis.items():

        if "method" not in config:

            errors.append(
                f"{endpoint} missing method"
            )

    # Auth Validation

    if len(auth) == 0:

        errors.append(
            "no auth roles defined"
        )

    for role, permissions in auth.items():

        if len(permissions) == 0:

            errors.append(
                f"{role} role has no permissions"
            )

    # Login Validation

    login_exists = False

    for page in pages:

        if page["name"].lower() == "login":

            login_exists = True

    if login_exists:

        if "/login" not in apis:

            errors.append(
                "login page without login api"
            )

    return errors
