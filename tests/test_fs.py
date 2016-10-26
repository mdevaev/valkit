import os

import pytest

from valkit import ValidatorError
from valkit.fs import valid_path
from valkit.fs import valid_filename


# =====
def test_ok__valid_path_exists__expanduser_abspath():  # pylint: disable=invalid-name
    for (arg, retval) in [
        ("/root", "/root"),
        (".",     os.path.abspath(".")),
        ("~",     os.path.expanduser("~")),
    ]:
        assert valid_path(arg, True, True, True) == retval


def test_fail__valid_path_exists__expanduser_abspath():  # pylint: disable=invalid-name
    for arg in ["/C:", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_path(arg, True, True, True)


# =====
def test_ok__valid_filename():
    for (arg, retval) in [
        ("test",       "test"),
        ("test test [test] #test$", "test test [test] #test$"),
        (".test",      ".test"),
        ("..test",     "..test"),
        ("..тест..",   "..тест.."),
        ("..те\\ст..", "..те\\ст.."),
        (".....",      "....."),
        (".....txt",   ".....txt"),
        ("test/",      "test"),
    ]:
        assert valid_filename(arg) == retval


def test_fail__valid_filename():
    for arg in [".", "..", "/test", "../test", "./.", "../.", "./..", "../..", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_filename(arg)


# =====
def test_fail__valid_path__make():
    validator = valid_path.mk(True, True, True)
    for arg in ["/C:", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            validator(arg)
