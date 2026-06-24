def repair_schema(schema, errors):

    repaired_items = []

    for error in errors:

        # Missing database

        if "database missing" in error:

            schema["database"] = {
                "tables": {}
            }

            repaired_items.append(
                "database created"
            )

        # Missing auth

        if "auth missing" in error:

            schema["auth"] = {
                "admin": ["all"],
                "user": ["read"]
            }

            repaired_items.append(
                "auth created"
            )

        # Missing UI

        if "ui missing" in error:

            schema["ui"] = {
                "pages": [
                    {
                        "name": "Dashboard",
                        "components": [
                            "Table",
                            "Form",
                            "Button"
                        ]
                    }
                ]
            }

            repaired_items.append(
                "ui created"
            )

        # Missing API

        if "api missing" in error:

            schema["api"] = {}

            repaired_items.append(
                "api created"
            )

        # API exists but table missing

        if "api without matching table" in error:

            entity = (
                error
                .split(" api")[0]
                .strip()
                .replace("/", "")
            )

            if "database" not in schema:

                schema["database"] = {
                    "tables": {}
                }

            schema["database"]["tables"][entity] = {
                "id": "int",
                "name": "string"
            }

            repaired_items.append(
                f"{entity} table created"
            )

        # Table exists but API missing

        if "table without api" in error:

            entity = (
                error
                .split(" table")[0]
                .strip()
            )

            if "api" not in schema:

                schema["api"] = {}

            schema["api"][f"/{entity}"] = {
                "method": "GET"
            }

            repaired_items.append(
                f"{entity} api created"
            )

        # Missing page components

        if "page missing components" in error:

            page_name = (
                error
                .replace(
                    " page missing components",
                    ""
                )
                .strip()
            )

            for page in schema["ui"]["pages"]:

                if page["name"] == page_name:

                    page["components"] = [
                        "Table",
                        "Form",
                        "Button"
                    ]

                    repaired_items.append(
                        f"{page_name} components added"
                    )

        # Missing roles

        if "no auth roles defined" in error:

            schema["auth"] = {

                "admin": ["all"],

                "user": ["read"]
            }

            repaired_items.append(
                "default roles added"
            )

    schema["repair_log"] = repaired_items

    schema["repair_count"] = len(
        repaired_items
    )

    return schema