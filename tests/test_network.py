import socket

from typing import Tuple
from typing import Optional
from typing import Any

import pytest

from valkit import ValidatorError
from valkit.network import valid_ip_or_host
from valkit.network import valid_ip
from valkit.network import valid_rfc_host
from valkit.network import valid_port


# =====
@pytest.mark.parametrize("arg, retval", [
    ("yandex.ru",      ("yandex.ru",      None)),
    ("foobar",         ("foobar",         None)),
    ("foo-bar.ru",     ("foo-bar.ru",     None)),
    ("127.0.0.1",      ("127.0.0.1",      socket.AF_INET)),
    ("8.8.8.8",        ("8.8.8.8",        socket.AF_INET)),
    ("::",             ("::",             socket.AF_INET6)),
    ("::1",            ("::1",            socket.AF_INET6)),
    ("2001:500:2f::f", ("2001:500:2f::f", socket.AF_INET6)),
])
def test_ok__valid_ip_or_host(arg: Any, retval: Tuple[str, Optional[socket.AddressFamily]]) -> None:  # pylint: disable=no-member
    assert valid_ip_or_host(arg) == retval


@pytest.mark.parametrize("arg", [
    "foo_bar.ru",
    "1.1.1.",
    ":",
])
def test_fail__valid_ip_or_host(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_ip_or_host(arg)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("127.0.0.1",      ("127.0.0.1",      socket.AF_INET)),
    ("8.8.8.8",        ("8.8.8.8",        socket.AF_INET)),
    ("::",             ("::",             socket.AF_INET6)),
    ("::1",            ("::1",            socket.AF_INET6)),
    ("2001:500:2f::f", ("2001:500:2f::f", socket.AF_INET6)),
])
def test_ok__valid_ip(arg: Any, retval: Tuple[str, socket.AddressFamily]) -> None:  # pylint: disable=no-member
    assert valid_ip(arg) == retval


@pytest.mark.parametrize("arg", [
    "ya.ru",
    "1",
    "1.1.1",
    "1.1.1.",
    ":",
    "",
    None,
])
def test__fail_valid_ip(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_ip(arg)


# =====
@pytest.mark.parametrize("arg", [
    "yandex.ru",
    "foobar",
    "foo-bar.ru",
    "z0r.de",
    "11.ru",
    "127.0.0.1",
])
def test_ok__valid_rfc_host(arg: Any) -> None:
    assert valid_rfc_host(arg) == arg


@pytest.mark.parametrize("arg", [
    "foo_bar.ru",
    "",
    None,
])
def test_fail__valid_rfc_host(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_rfc_host(arg)


# =====
@pytest.mark.parametrize("arg, retval", [
    ("0",   0),
    (0,     0),
    ("22",  22),
    (443,   443),
    (65535, 65535),
])
def test_ok__valid_port(arg: Any, retval: int) -> None:
    assert valid_port(arg) == retval


@pytest.mark.parametrize("arg", [
    "x",
    65536,
    "",
    None,
])
def test_fail__valid_port(arg: Any) -> None:
    with pytest.raises(ValidatorError):
        valid_port(arg)
