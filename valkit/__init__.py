import re

from typing import List
from typing import Callable
from typing import TypeVar
from typing import NoReturn
from typing import Optional
from typing import Any


# =====
class ValidatorError(ValueError):
    pass


# =====
def raise_validator(
    arg: Any,
    name: str,
    err_extra: str="",
) -> NoReturn:

    err_extra = (": %s" % (err_extra) if err_extra else "")
    arg_str = ("%r" if isinstance(arg, (str, bytes)) else "'%s'") % (arg)
    raise ValidatorError(("The argument " + arg_str + " is not a valid %s%s") % (name, err_extra))


def not_none(
    arg: Any,
    name: str,
) -> Any:  # FIXME -> NotNone

    if arg is None:
        raise ValidatorError("Empty argument is not a valid %s" % (name))
    return arg


def not_none_string(
    arg: Any,
    name: str,
    strip: bool=False,
) -> str:

    arg = str(not_none(arg, name))
    return (arg.strip() if strip else arg)


def check_any(
    arg: Any,
    name: str,
    validators: List[Callable[[Any], Any]],
) -> Any:

    for validator in validators:
        try:
            return validator(arg)
        except Exception:
            pass
    raise_validator(arg, name)


def check_re_match(
    arg: Any,
    name: str,
    pattern: str,
    strip: bool=False,
    limit: Optional[int]=None,
) -> Any:

    arg = not_none_string(arg, name, strip)
    if limit is not None:
        arg = arg[:limit]
    if re.match(pattern, arg) is None:
        raise_validator(arg, name)
    return arg


def check_in_list(
    arg: Any,
    name: str,
    variants: List,
) -> Any:

    if arg not in variants:
        raise_validator(arg, name)
    return arg


def check_iterable(
    arg: Any,
    item_validator: Callable[[Any], Any],
    iterable_validator: Callable[[Any], Any],
) -> Optional[List]:

    return list(map(item_validator, iterable_validator(arg)))


_ValidatorT = TypeVar("_ValidatorT", bound=Callable)


def add_validator_magic(
    validator: _ValidatorT,
) -> _ValidatorT:

    def make(*args: Any, **kwargs: Any) -> Callable[[Any], Any]:
        return (lambda arg: validator(arg, *args, **kwargs))

    validator.mk = make
    return validator
