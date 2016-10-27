import logging

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_object_name(arg, strip=False):
    return _tools.check_re_match(arg, "Python object name", r"^[a-zA-Z_][a-zA-Z0-9_]*$", strip)


@_tools.add_lambda_maker
def valid_object_path(arg, strip=False):
    pattern = r"^([a-zA-Z_][a-zA-Z0-9_]*\.)*[a-zA-Z_][a-zA-Z0-9_]*$"
    return _tools.check_re_match(arg, "Python object path", pattern, strip)


@_tools.add_lambda_maker
def valid_logging_level(arg, up=True, strip=False):
    name = "logging level"
    try:
        arg = int(arg)
        if arg not in logging._levelToName:  # pylint: disable=protected-access
            _tools.raise_error(arg, name)
        return arg
    except ValueError:
        arg = _tools.not_none_string(arg, name, strip)
        try:
            return logging._nameToLevel[arg.upper() if up else arg]  # pylint: disable=protected-access
        except KeyError:
            _tools.raise_error(arg, name)
