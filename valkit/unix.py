from typing import Any

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_username(
    arg: Any,
    strip: bool=False,
) -> str:

    return _tools.check_re_match(arg, "UNIX username", r"^[a-z_][a-z0-9_-]*$", strip)


@_tools.add_lambda_maker
def valid_groupname(
    arg: Any,
    strip: bool=False,
) -> str:

    return _tools.check_re_match(arg, "UNIX groupname", r"^[a-z_][a-z0-9_-]*$", strip)
