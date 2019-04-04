from typing import Any

import pytest

from valkit import ValidatorError
from valkit.unix import valid_username
from valkit.unix import valid_groupname


# =====
_USERS_OK = [
    "glados",
    "test",
    "_",
    "_foo_bar_",
]

_USERS_FAIL = [
    "-molestia",
    "te~st",
    "-",
    "-foo_bar",
    "",
    "  ",
    " aix",
    None,
]


# =====
@pytest.mark.parametrize("arg", _USERS_OK)
def test_ok__valid_username(arg: Any) -> None:
    assert valid_username(arg) == arg


@pytest.mark.parametrize("arg", _USERS_FAIL)
def test_fail__valid_username(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_username(arg)


# =====
@pytest.mark.parametrize("arg", _USERS_OK)
def test_ok__valid_groupname(arg: Any) -> None:
    assert valid_groupname(arg) == arg


@pytest.mark.parametrize("arg", _USERS_FAIL)
def test_fail__valid_groupname(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_groupname(arg)
