import json

from . import _tools


# =====
def valid_hex_string(arg):
    return _tools.check_re_match(arg, "hex string", r"^[0-9a-fA-F]+$")


def valid_uuid_string(arg):
    pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    return _tools.check_re_match(arg, "UUID string", pattern)


def valid_json_string(arg):
    arg = _tools.not_none_strip(arg, "JSON string")
    try:
        json.dumps(json.loads(arg))
        return arg
    except Exception as err:
        raise _tools.raise_error(arg, "JSON string", str(err))
