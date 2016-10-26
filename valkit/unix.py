from . import _tools


# =====
def valid_username(arg):
    return _tools.check_re_match(arg, "UNIX username", r"^[a-z_][a-z0-9_-]*$")


def valid_groupname(arg):
    return _tools.check_re_match(arg, "UNIX groupname", r"^[a-z_][a-z0-9_-]*$")
