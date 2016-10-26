from . import _tools


# =====
def valid_object_name(arg):
    return _tools.check_re_match(arg, "Python object name", r"^[a-zA-Z_][a-zA-Z0-9_]*$")
