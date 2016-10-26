import json

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_hex_string(arg, strip=False):
    return _tools.check_re_match(arg, "hex string", r"^[0-9a-fA-F]+$", strip)


@_tools.add_lambda_maker
def valid_uuid_string(arg, strip=False):
    pattern = r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    return _tools.check_re_match(arg, "UUID string", pattern, strip)


@_tools.add_lambda_maker
def valid_json_string(arg, strip=False):
    arg = _tools.not_none_string(arg, "JSON string", strip)
    try:
        json.dumps(json.loads(arg))
        return arg
    except Exception as err:
        raise _tools.raise_error(arg, "JSON string", str(err))
