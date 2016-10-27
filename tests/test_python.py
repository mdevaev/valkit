import logging

import pytest

from valkit import ValidatorError
from valkit.python import valid_object_name
from valkit.python import valid_object_path
from valkit.python import valid_logging_level


# =====
def test_ok__valid_object_name():
    for arg in [
        "__test",
        "__test__",
        "Object_Name",
        "objectName123",
        "_",
    ]:
        assert valid_object_name(arg) == arg


def test_fail__valid_object_name():
    for arg in [".object", "123object", "/object"]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_object_name(arg)


# =====
def test_ok__valid_object_path():
    for arg in [
        "__test",
        "__test__",
        "Object_Name",
        "objectName123",
        "_",
        "__test.test",
        "_._._",
    ]:
        assert valid_object_path(arg) == arg


def test_fail__valid_object_path():
    for arg in [".object", "123object", "/object", "a.b.c." "a.1x.b"]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_object_path(arg)


# =====
def test_ok__valid_logging_level():
    for arg in logging._levelToName:  # pylint: disable=protected-access
        assert valid_logging_level(arg) == arg
        assert valid_logging_level(str(arg)) == arg

    for (arg, retval) in logging._nameToLevel.items():  # pylint: disable=protected-access
        assert valid_logging_level(arg) == retval
        assert valid_logging_level(arg.lower()) == retval


def test_fail__valid_logging_level():
    for arg in ["foo", "bar", "111", 111, "info"]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_logging_level(arg, up=False)
