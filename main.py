import json


def format_data(data):
    return json.dumps(data, indent=4, sort_keys=True)


def validate_json(json_string):
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    sample = {"author": "Oliwier", "project": "INFI", "year": 2026}
    print(format_data(sample))
