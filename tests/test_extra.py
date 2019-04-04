from typing import Any

import pytest

from valkit import ValidatorError
from valkit.extra import valid_hex_string
from valkit.extra import valid_uuid_string
from valkit.extra import valid_json_string


# =====
@pytest.mark.parametrize("arg", [
    "d41d8cd98f00b204e9800998ecf8427e",
    "D41D8CD98F00B204E9800998ECF8427E",
])
def test_ok__valid_hex_string(arg: Any) -> None:
    assert valid_hex_string(arg) == arg


@pytest.mark.parametrize("arg", [
    "d41d8cd98f00b204e9800998ecf8427ex",
    "",
    None,
])
def test_fail__valid_hex_string(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_hex_string(arg)


# =====
@pytest.mark.parametrize("arg", [
    "550e8400-e29b-41d4-a716-446655440000",
    "00000000-0000-0000-C000-000000000046",
    "00000000-0000-0000-0000-000000000000",
])
def test_ok__valid_uuid_string(arg: Any) -> None:
    assert valid_uuid_string(arg) == arg


@pytest.mark.parametrize("arg", [
    "550e8400-e29b-41d4-a716-44665544",
    "ffffuuuu-0000-0000-C000-000000000046",
    "",
    None,
])
def test_fail__valid_uuid_string(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_uuid_string(arg)


# =====
def test_ok__valid_json_string() -> None:
    json_string = """{"1": 1, "3": ["a", "b", "c"], "2": 2}"""
    assert valid_json_string(json_string) == json_string


def test_fail__valid_json_string() -> None:
    with pytest.raises(ValidatorError):
        valid_json_string("{1:1}")
