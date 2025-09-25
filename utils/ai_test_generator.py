import os
import openai
import yaml
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tests_from_schema(schema_file, output_file="tests/generated/test_ai_generated.py"):
    with open(schema_file, "r") as f:
        schema = yaml.safe_load(f)

    prompt = f"""
    You are a QA automation engineer.
    Given this OpenAPI schema, generate pytest test cases (positive + negative).
    Schema:
    {yaml.dump(schema)}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You write clean pytest test cases with requests library."},
            {"role": "user", "content": prompt}
        ]
    )

    test_code = response["choices"][0]["message"]["content"]

    os.makedirs("tests/generated", exist_ok=True)
    with open(output_file, "w") as f:
        f.write(test_code)

    print(f"✅ AI-generated tests written to {output_file}")
