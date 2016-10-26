import pytest

from valkit import ValidatorError
from valkit.extra import valid_hex_string
from valkit.extra import valid_uuid_string
from valkit.extra import valid_json_string


# =====
def test_ok__valid_hex_string():
    for arg in ["d41d8cd98f00b204e9800998ecf8427e", "D41D8CD98F00B204E9800998ECF8427E"]:
        assert valid_hex_string(arg) == arg


def test_fail__valid_hex_string():
    for arg in ["d41d8cd98f00b204e9800998ecf8427ex", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_hex_string(arg)


# =====
def test_ok__valid_uuid_string():
    for arg in [
        "550e8400-e29b-41d4-a716-446655440000",
        "00000000-0000-0000-C000-000000000046",
        "00000000-0000-0000-C000-000000000000",
    ]:
        assert valid_uuid_string(arg) == arg


def test_fail__valid_uuid_string():
    for arg in ["550e8400-e29b-41d4-a716-44665544", "ffffuuuu-0000-0000-C000-000000000046", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_uuid_string(arg)


# =====
def test_ok__valid_json_string():
    json_string = """{"1": 1, "3": ["a", "b", "c"], "2": 2}"""
    assert valid_json_string(json_string) == json_string


def test_fail__valid_json_string():
    with pytest.raises(ValidatorError):
        valid_json_string("{1:1}")
