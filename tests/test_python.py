import logging

from typing import Any

import pytest

from valkit import ValidatorError
from valkit.python import valid_object_name
from valkit.python import valid_object_path
from valkit.python import valid_logging_level


# =====
@pytest.mark.parametrize("arg", [
    "__test",
    "__test__",
    "Object_Name",
    "objectName123",
    "_",
])
def test_ok__valid_object_name(arg: Any) -> None:
    assert valid_object_name(arg) == arg


@pytest.mark.parametrize("arg", [
    ".object",
    "123object",
    "/object",
])
def test_fail__valid_object_name(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_object_name(arg)


# =====
@pytest.mark.parametrize("arg", [
    "__test",
    "__test__",
    "Object_Name",
    "objectName123",
    "_",
    "__test.test",
    "_._._",
])
def test_ok__valid_object_path(arg: Any) -> None:
    assert valid_object_path(arg) == arg


@pytest.mark.parametrize("arg", [
    ".object",
    "123object",
    "/object",
    "a.b.c.",
    "a.1x.b",
])
def test_fail__valid_object_path(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_object_path(arg)


# =====
@pytest.mark.parametrize("arg, retval", [
    *list(zip(logging._levelToName, logging._levelToName)),  # pylint: disable=protected-access
    *[(str(arg), arg) for arg in logging._levelToName],  # pylint: disable=protected-access
    *list(logging._nameToLevel.items()),  # pylint: disable=protected-access
    *[(arg.lower(), retval) for (arg, retval) in logging._nameToLevel.items()],  # pylint: disable=protected-access
])
def test_ok__valid_logging_level(arg: Any, retval: int) -> None:
    assert valid_logging_level(arg) == retval


@pytest.mark.parametrize("arg", [
    "foo",
    "bar",
    "111",
    111,
    "info",
])
def test_fail__valid_logging_level(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_logging_level(arg, up=False)
