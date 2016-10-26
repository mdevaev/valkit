from . import _tools


# =====
@_tools.add_lambda_maker
def valid_object_name(arg, strip=False):
    return _tools.check_re_match(arg, "Python object name", r"^[a-zA-Z_][a-zA-Z0-9_]*$", strip)
