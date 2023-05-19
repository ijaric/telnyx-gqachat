import orjson


def extract_data(filename: str = "documentation.json") -> list[dict]:
    with open(filename, "rb") as file:
        data = orjson.loads(file.read())

    # Remove duplicates
    unique_data = [dict(t) for t in set(tuple(d.items()) for d in data)]
    return unique_data
