import re

from typing import List
from typing import Type
from typing import Callable
from typing import Optional
from typing import Union
from typing import Any

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_bool(
    arg: Any,
    strip: bool=False,
) -> bool:

    true_args = ["1", "true", "yes"]
    false_args = ["0", "false", "no"]
    name = "bool (%r or %r)" % (true_args, false_args)
    arg = _tools.not_none_string(arg, name, strip).lower()
    arg = _tools.check_in_list(arg, name, true_args + false_args)
    return (arg in true_args)


@_tools.add_lambda_maker
def valid_number(
    arg: Any,
    min: Union[int, float, None]=None,  # pylint: disable=redefined-builtin
    max: Union[int, float, None]=None,  # pylint: disable=redefined-builtin
    type: Union[Type[int], Type[float]]=int,  # pylint: disable=redefined-builtin
    strip: bool=False,
) -> Union[int, float]:

    arg = _tools.not_none_string(arg, type.__name__, strip)
    try:
        arg = type(arg)
    except Exception:
        _tools.raise_error(arg, type.__name__)

    if min is not None and arg < min:
        raise _tools.ValidatorError("The argument '%s' must be greater or equial than %s" % (arg, min))
    if max is not None and arg > max:
        raise _tools.ValidatorError("The argument '%s' must be lesser or equal then %s" % (arg, max))
    return arg


@_tools.add_lambda_maker
def valid_in_list(
    arg: Any,
    variants: List,
    subval: Optional[Callable[[Any], Any]]=None,
) -> List:

    variants = list(variants)
    if subval is not None:
        arg = subval(arg)
    return _tools.check_in_list(arg, "item of list %r" % (variants), variants)


@_tools.add_lambda_maker
def valid_string_list(
    arg: Any,
    delim: str=r"[,\t ]+",
    subval: Optional[Callable[[Any], Any]]=None,
    strip: bool=False,
) -> List[str]:

    if not isinstance(arg, (list, tuple)):
        arg = _tools.not_none_string(arg, "string list", strip)
        arg = list(filter(None, re.split(delim, arg)))
        if subval is not None:
            arg = list(map(subval, arg))
    return arg


@_tools.add_lambda_maker
def valid_empty(
    arg: Any,
    subval: Optional[Callable[[Any], Any]]=None,
    strip: bool=False
) -> Any:

    if arg is None or (isinstance(arg, str) and len(arg.strip() if strip else arg) == 0):  # pylint: disable=no-else-return
        return None
    elif subval is None:
        return arg
    else:
        return subval(arg)
