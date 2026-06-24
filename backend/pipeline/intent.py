import json
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def extract_intent(prompt):

    try:

        response = model.generate_content(
            f"""
You are an Intent Extraction Engine.

Convert the following user request into STRICT JSON.

User Request:
{prompt}

Return ONLY valid JSON.

Format:

{{
  "app_type":"application",
  "features":[],
  "roles":["admin","user"]
}}
"""
        )

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        data = json.loads(text)

        if not isinstance(data, dict):
            raise Exception("Invalid JSON Structure")

        data.setdefault("app_type", "application")
        data.setdefault("features", [])
        data.setdefault("roles", ["admin", "user"])

        return data

    except Exception as e:

        print("Intent Extraction Error:", e)

        prompt_lower = prompt.lower()

        features = []

        keywords = [

            "login",
            "contacts",
            "dashboard",
            "payments",
            "analytics",
            "users",
            "roles",

            "students",
            "teachers",
            "courses",
            "assignments",
            "quizzes",

            "patients",
            "doctors",
            "appointments",
            "billing",

            "employees",
            "attendance",
            "payroll",
            "leave",

            "inventory",
            "products",
            "orders",
            "cart",

            "events",
            "tickets",

            "reports",
            "subscriptions",
            "premium"
        ]

        for keyword in keywords:

            if keyword in prompt_lower:

                features.append(keyword)

        app_type = "application"

        if "crm" in prompt_lower:
            app_type = "crm"

        elif "hospital" in prompt_lower:
            app_type = "hospital"

        elif "school" in prompt_lower:
            app_type = "school"

        elif "erp" in prompt_lower:
            app_type = "erp"

        elif "lms" in prompt_lower:
            app_type = "lms"

        elif "learning" in prompt_lower:
            app_type = "lms"

        elif "ecommerce" in prompt_lower:
            app_type = "ecommerce"

        elif "e-commerce" in prompt_lower:
            app_type = "ecommerce"

        elif "inventory" in prompt_lower:
            app_type = "inventory"

        elif "hr" in prompt_lower:
            app_type = "hr"

        elif "bank" in prompt_lower:
            app_type = "banking"

        elif "ticket" in prompt_lower:
            app_type = "booking"

        roles = ["admin", "user"]

        if "teacher" in prompt_lower:
            roles.append("teacher")

        if "student" in prompt_lower:
            roles.append("student")

        return {

            "app_type": app_type,

            "features": list(set(features)),

            "roles": list(set(roles))
        }