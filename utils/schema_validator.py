from jsonschema import validate, ValidationError

def validate_schema(instance, schema):
    """
    Validate a JSON response against a schema with helpful error messages.

    :param instance: The actual JSON (dict) response
    :param schema: The expected schema (dict)
    :raises AssertionError: if schema validation fails
    """
    try:
        validate(instance=instance, schema=schema)
    except ValidationError as e:
        raise AssertionError(
            f"Schema validation failed: {e.message}\n"
            f"Instance: {instance}\n"
            f"Schema: {schema}"
        )
