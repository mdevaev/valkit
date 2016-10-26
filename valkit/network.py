import socket

from . import _tools


# =====
@_tools.add_lambda_maker
def valid_ip_or_host(arg, strip=False):
    name = "IPv4/IPv6 address or RFC-1123 hostname",
    return _tools.check_chain(
        arg=_tools.not_none_string(arg, name, strip),
        name=name,
        validators=[
            valid_ip,
            lambda arg: (valid_rfc_host(arg), None),
        ],
    )


@_tools.add_lambda_maker
def valid_ip(arg, strip=False):
    name = "IPv4/6 address",
    return _tools.check_chain(
        arg=_tools.not_none_string(arg, name, strip),
        name=name,
        validators=[
            lambda arg: ((arg, socket.inet_pton(socket.AF_INET, arg))[0], socket.AF_INET),
            lambda arg: ((arg, socket.inet_pton(socket.AF_INET6, arg))[0], socket.AF_INET6),
        ],
    )


@_tools.add_lambda_maker
def valid_rfc_host(arg, strip=False):
    # http://stackoverflow.com/questions/106179/regular-expression-to-match-hostname-or-ip-address
    pattern = r"^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*" \
              r"([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
    return _tools.check_re_match(arg, "RFC-1123 hostname", pattern, strip)


@_tools.add_lambda_maker
def valid_port(arg, strip=False):
    name = "TCP/UDP portnumber"
    arg = _tools.not_none_string(arg, name, strip)
    try:
        if not (0 <= int(arg) < 65536):
            raise Exception()
        return int(arg)
    except Exception:
        _tools.raise_error(arg, name)
