import pytest

from valkit import ValidatorError
from valkit.common import valid_bool
from valkit.common import valid_number
from valkit.common import valid_in_list
from valkit.common import valid_string_list
from valkit.common import valid_empty


# =====
def test_ok__valid_bool():
    for (arg, retval) in [
        ("1",     True),
        ("true",  True),
        ("TRUE",  True),
        ("yes",   True),
        (1,       True),
        (True,    True),
        ("0",     False),
        ("false", False),
        ("FALSE", False),
        ("no",    False),
        (0,       False),
        (False,   False),
    ]:
        assert valid_bool(arg) == retval


def test_fail__valid_bool():
    for arg in ["x", -1, "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_bool(arg)


# =====
def test_ok__valid_number():
    for (arg, retval) in [
        ("1",    1),
        ("-1",   -1),
        (1,      1),
        (-1,     -1),
        (0,      0),
        (100500, 100500),
    ]:
        assert valid_number(arg) == retval


def test_fail__valid_number():
    for arg in ["1x", "", None, 100500.0]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_number(arg)


def test_ok__valid_number__min_max():
    for (arg, retval) in [
        (-5,   -5),
        (0,    0),
        (5,    5),
        ("-5", -5),
        ("0",  0),
        ("5",  5),
    ]:
        assert valid_number(arg, -5, 5) == retval


def test_fail__valid_number__min_max():  # pylint: disable=invalid-name
    for arg in [-6, 6, "-6", "6"]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_number(arg, -5, 5)


# =====
def test_ok__valid_in_list():
    for arg in [1, 3, "5"]:
        assert valid_in_list(arg, (1, 3, "5")) == arg


def test_fail__valid_in_list():
    for arg in ["1", "3", 5, ""]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_in_list(arg, (1, 3, "5"))


def test_ok__valid_in_list__subval():
    for (arg, retval) in [
        (1,   1),
        (3,   3),
        ("5", 5),
    ]:
        assert valid_in_list(arg, (1, 3, 5), valid_number) == retval


def test_fail__valid_in_list__subval():  # pylint: disable=invalid-name
    for arg in [None, ""]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_in_list(arg, (1, 3, 5, ""), valid_number)


# =====
def test_ok__valid_string_list():
    for (arg, retval) in [
        ("a, b, c",       ["a", "b", "c"]),
        ("a b c",         ["a", "b", "c"]),
        (["a", "b", "c"], ["a", "b", "c"]),
    ]:
        assert valid_string_list(arg) == retval


def test_ok__valid_string_list__subval():  # pylint: disable=invalid-name
    for (arg, retval) in [
        ("1, 2, 3", [1, 2, 3]),
        ("1 2 3",   [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    ]:
        assert valid_string_list(arg, subval=int) == retval


def test_fail__valid_string_list__none():  # pylint: disable=invalid-name
    with pytest.raises(ValidatorError):
        valid_string_list(None)


# =====
def test_ok__valid_empty__strip():
    for (arg, retval) in [
        ("",   None),
        (" ",  None),
        (None, None),
        ("x",  "x"),
    ]:
        assert valid_empty(arg, strip=True) == retval


def test_ok__valid_empty__validator_strip():  # pylint: disable=invalid-name
    for (arg, retval) in [
        ("",   None),
        (" ",  None),
        (None, None),
        (1,    1),
        ("1",  1),
    ]:
        assert valid_empty(arg, int, strip=True) == retval
