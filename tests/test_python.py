import pytest

from valkit import ValidatorError
from valkit.python import valid_object_name


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
