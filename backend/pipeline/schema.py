def generate_schema(design):

    ui_pages = []

    api = {}

    db_tables = {}

    # Special Plural Mapping

    plural_map = {

        "user": "users",
        "contact": "contacts",
        "student": "students",
        "teacher": "teachers",
        "payment": "payments",
        "patient": "patients",
        "doctor": "doctors",
        "appointment": "appointments",
        "employee": "employees",
        "product": "products",
        "order": "orders",
        "inventory": "inventories",
        "ticket": "tickets",
        "event": "events",
        "course": "courses",
        "report": "reports",
        "subscription": "subscriptions"
    }

    # UI Generation

    for page in design["pages"]:

        if page.lower() == "login":

            ui_pages.append({

                "name": page,

                "components": [
                    "EmailInput",
                    "PasswordInput",
                    "LoginButton"
                ]
            })

        elif page.lower() == "dashboard":

            ui_pages.append({

                "name": page,

                "components": [
                    "Cards",
                    "Charts",
                    "SummaryTable"
                ]
            })

        else:

            ui_pages.append({

                "name": page,

                "components": [
                    "Table",
                    "Form",
                    "Button"
                ]
            })

    # Database + API Generation

    for entity in design["entities"]:

        entity_lower = entity.lower()

        table_name = plural_map.get(
            entity_lower,
            entity_lower + "s"
        )

        # User Schema

        if entity_lower == "user":

            db_tables[table_name] = {

                "id": "int",

                "name": "string",

                "email": "string",

                "role": "string"
            }

        # Payment Schema

        elif entity_lower == "payment":

            db_tables[table_name] = {

                "id": "int",

                "amount": "float",

                "status": "string"
            }

        # Appointment Schema

        elif entity_lower == "appointment":

            db_tables[table_name] = {

                "id": "int",

                "patient_id": "int",

                "doctor_id": "int",

                "date": "string"
            }

        # Generic Schema

        else:

            db_tables[table_name] = {

                "id": "int",

                "name": "string"
            }

        api[f"/{table_name}"] = {

            "method": "GET"
        }

    # Login API

    if "Login" in design["pages"]:

        api["/login"] = {

            "method": "POST"
        }

    # Roles

    auth = {}

    for role in design["roles"]:

        role_lower = role.lower()

        if role_lower == "admin":

            auth[role] = [

                "create",
                "read",
                "update",
                "delete"
            ]

        elif role_lower == "teacher":

            auth[role] = [

                "read",
                "update"
            ]

        else:

            auth[role] = [

                "read"
            ]

    # Final Schema

    return {

        "ui": {

            "pages": ui_pages
        },

        "api": api,

        "database": {

            "tables": db_tables
        },

        "auth": auth,

        "assumptions": []
    }
