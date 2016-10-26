import os

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_path(arg, expanduser=False, abspath=False, f_ok=False):
    name = ("accessible path" if f_ok else "path")
    if len(str(arg).strip()) == 0:
        arg = None
    arg = _tools.not_none(arg, name)
    if expanduser:
        arg = os.path.expanduser(arg)
    if abspath:
        arg = os.path.abspath(arg)
    if f_ok and not os.access(arg, os.F_OK):
        _tools.raise_error(arg, name)
    return arg


def valid_filename(arg):
    # http://en.wikipedia.org/wiki/Filename#Comparison_of_filename_limitations
    assert os.name == "posix", "This validator is not implemented for %s" % (os.name)
    name = "filename"
    arg = os.path.normpath(_tools.not_none(arg, name))
    if arg == "." or arg == "..":
        _tools.raise_error(arg, name)
    return _tools.check_re_match(arg, name, r"^[^/\0]+$")
