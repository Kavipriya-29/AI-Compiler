def system_design(intent):

    entities = ["User"]

    pages = ["Login", "Dashboard"]

    feature_to_entity = {

        "contacts": "Contact",
        "students": "Student",
        "teachers": "Teacher",
        "payments": "Payment",
        "patients": "Patient",
        "doctors": "Doctor",
        "appointments": "Appointment",
        "employees": "Employee",
        "products": "Product",
        "orders": "Order",
        "inventory": "Inventory",
        "tickets": "Ticket",
        "events": "Event",
        "courses": "Course",
        "reports": "Report",
        "subscriptions": "Subscription"
    }

    plural_map = {

        "Contact": "Contacts",
        "Student": "Students",
        "Teacher": "Teachers",
        "Payment": "Payments",
        "Patient": "Patients",
        "Doctor": "Doctors",
        "Appointment": "Appointments",
        "Employee": "Employees",
        "Product": "Products",
        "Order": "Orders",
        "Inventory": "Inventories",
        "Ticket": "Tickets",
        "Event": "Events",
        "Course": "Courses",
        "Report": "Reports",
        "Subscription": "Subscriptions"
    }

    for feature in intent["features"]:

        feature = feature.lower()

        if feature in feature_to_entity:

            entity = feature_to_entity[feature]

            if entity not in entities:

                entities.append(entity)

            page_name = plural_map.get(
                entity,
                entity + "s"
            )

            if page_name not in pages:

                pages.append(page_name)

    return {

        "pages": pages,

        "entities": entities,

        "roles": intent["roles"]
    }