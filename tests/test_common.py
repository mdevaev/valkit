from typing import List
from typing import Any

import pytest

from valkit import ValidatorError
from valkit.common import valid_bool
from valkit.common import valid_number
from valkit.common import valid_in_list
from valkit.common import valid_string_list
from valkit.common import valid_empty


# =====
@pytest.mark.parametrize("arg, retval", [
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
])
def test_ok__valid_bool(arg: Any, retval: bool) -> None:
    assert valid_bool(arg) == retval


@pytest.mark.parametrize("arg", [
    "x",
    -1,
    "",
    None,
])
def test_fail__valid_bool(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_bool(arg)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("1",    1),
    ("-1",   -1),
    (1,      1),
    (-1,     -1),
    (0,      0),
    (100500, 100500),
])
def test_ok__valid_number(arg: Any, retval: int) -> None:
    assert valid_number(arg) == retval


@pytest.mark.parametrize("arg", [
    "1x",
    "",
    None,
    100500.0,
])
def test_fail__valid_number(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_number(arg)


@pytest.mark.parametrize("arg, retval", [
    (-5,   -5),
    (0,    0),
    (5,    5),
    ("-5", -5),
    ("0",  0),
    ("5",  5),
])
def test_ok__valid_number__min_max(arg: Any, retval: int) -> None:
    assert valid_number(arg, -5, 5) == retval


@pytest.mark.parametrize("arg", [
    -6,
    6,
    "-6",
    "6",
])
def test_fail__valid_number__min_max(arg: Any) -> None:  # pylint: disable=invalid-name
    with pytest.raises(ValidatorError):
        valid_number(arg, -5, 5)


# =====
@pytest.mark.parametrize("arg", [
    1,
    3,
    "5",
])
def test_ok__valid_in_list(arg: Any) -> None:
    assert valid_in_list(arg, [1, 3, "5"]) == arg


@pytest.mark.parametrize("arg", [
    "1",
    "3",
    5,
    "",
    None,
])
def test_fail__valid_in_list(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_in_list(arg, [1, 3, "5"])


@pytest.mark.parametrize("arg, retval", [
    (1,   1),
    (3,   3),
    ("5", 5),
])
def test_ok__valid_in_list__subval(arg: Any, retval: int) -> None:
    assert valid_in_list(arg, [1, 3, 5], valid_number) == retval


@pytest.mark.parametrize("arg", [
    1.0,
    None,
    "",
])
def test_fail__valid_in_list__subval(arg: Any) -> None:  # pylint: disable=invalid-name
    with pytest.raises(ValidatorError):
        valid_in_list(arg, [1, 3, 5, ""], valid_number)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("a, b, c",       ["a", "b", "c"]),
    ("a b c",         ["a", "b", "c"]),
    (["a", "b", "c"], ["a", "b", "c"]),
])
def test_ok__valid_string_list(arg: Any, retval: List) -> None:
    assert valid_string_list(arg) == retval


@pytest.mark.parametrize("arg, retval", [
    ("1, 2, 3", [1, 2, 3]),
    ("1 2 3",   [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
])
def test_ok__valid_string_list__subval(arg: Any, retval: List) -> None:  # pylint: disable=invalid-name
    assert valid_string_list(arg, subval=int) == retval


def test_fail__valid_string_list__none() -> None:  # pylint: disable=invalid-name
    with pytest.raises(ValidatorError):
        valid_string_list(None)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("",   None),
    (" ",  None),
    (None, None),
    ("x",  "x"),
    (1,    1),
])
def test_ok__valid_empty__strip(arg: Any, retval: Any) -> None:
    assert valid_empty(arg, strip=True) == retval


@pytest.mark.parametrize("arg, retval", [
    ("",   None),
    (" ",  None),
    (None, None),
    (1,    1),
    ("1",  1),
    (" 1", 1),
])
def test_ok__valid_empty__validator_strip(arg: Any, retval: Any) -> None:  # pylint: disable=invalid-name
    assert valid_empty(arg, int, strip=True) == retval
