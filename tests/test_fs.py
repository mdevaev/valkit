import os

from typing import Any

import pytest

from valkit import ValidatorError
from valkit.fs import valid_path
from valkit.fs import valid_filename


# =====
@pytest.mark.parametrize("arg, retval", [
    ("/root", "/root"),
    (".",     os.path.abspath(".")),
    ("~",     os.path.expanduser("~")),
])
def test_ok__valid_path_exists__expanduser_abspath(arg: Any, retval: str) -> None:  # pylint: disable=invalid-name
    assert valid_path(arg, True, True, True) == retval


@pytest.mark.parametrize("arg", [
    "/C:",
    "",
    None,
])
def test_fail__valid_path_exists__expanduser_abspath(arg: Any) -> None:  # pylint: disable=invalid-name
    with pytest.raises(ValidatorError):
        valid_path(arg, True, True, True)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("test",       "test"),
    ("test test [test] #test$", "test test [test] #test$"),
    (".test",      ".test"),
    ("..test",     "..test"),
    ("..тест..",   "..тест.."),
    ("..те\\ст..", "..те\\ст.."),
    (".....",      "....."),
    (".....txt",   ".....txt"),
    ("test/",      "test"),
])
def test_ok__valid_filename(arg: Any, retval: str) -> None:
    assert valid_filename(arg) == retval


@pytest.mark.parametrize("arg", [
    ".",
    "..",
    "/test",
    "../test",
    "./.",
    "../.",
    "./..",
    "../..",
    "",
    None,
])
def test_fail__valid_filename(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_filename(arg)


# =====
@pytest.mark.parametrize("arg", [
    "/C:",
    "",
    None,
])
def test_fail__valid_path__make(arg: Any) -> None:
    validator = valid_path.mk(True, True, True)
    with pytest.raises(ValidatorError):
        validator(arg)
