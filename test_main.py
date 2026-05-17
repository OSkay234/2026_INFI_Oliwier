from main import format_data, validate_json


def test_format_data():
    result = format_data({"b": 2, "a": 1})
    assert '"a": 1' in result
    assert '"b": 2' in result


def test_validate_json_valid():
    assert validate_json('{"key": "value"}') is True


def test_validate_json_invalid():
    assert validate_json('not json') is False
