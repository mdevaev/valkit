import pytest

from valkit import ValidatorError
from valkit.unix import valid_username
from valkit.unix import valid_groupname


# =====
def test_ok__valid_username():
    for arg in [
        "glados",
        "test",
        "_",
        "_foo_bar_",
    ]:
        assert valid_username(arg) == arg


def test_fail__valid_username():
    for arg in ["-molestia", "te~st", "-", "-foo_bar", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_username(arg)


# =====
def test_ok__valid_groupname():
    for arg in [
        "glados",
        "test",
        "_",
        "_foo_bar_",
    ]:
        assert valid_groupname(arg) == arg


def test_fail__valid_groupname():
    for arg in ["-molestia", "te~st", "-", "-foo_bar", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_groupname(arg)
