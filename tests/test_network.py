import socket

import pytest

from valkit import ValidatorError
from valkit.network import valid_ip_or_host
from valkit.network import valid_ip
from valkit.network import valid_rfc_host
from valkit.network import valid_port


# =====
def test_ok__valid_ip_or_host():
    for (arg, retval) in [
        ("yandex.ru",      ("yandex.ru",      None)),
        ("foobar",         ("foobar",         None)),
        ("foo-bar.ru",     ("foo-bar.ru",     None)),
        ("127.0.0.1",      ("127.0.0.1",      socket.AF_INET)),
        ("8.8.8.8",        ("8.8.8.8",        socket.AF_INET)),
        ("::1",            ("::1",            socket.AF_INET6)),
        ("2001:500:2f::f", ("2001:500:2f::f", socket.AF_INET6)),
    ]:
        assert valid_ip_or_host(arg) == retval


def test_fail__valid_ip_or_host():
    for arg in ["foo_bar.ru", "1.1.1.", ":", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_ip_or_host(arg)


# =====
def test_ok__valid_ip():
    for (arg, retval) in [
        ("127.0.0.1",      ("127.0.0.1",      socket.AF_INET)),
        ("8.8.8.8",        ("8.8.8.8",        socket.AF_INET)),
        ("::1",            ("::1",            socket.AF_INET6)),
        ("2001:500:2f::f", ("2001:500:2f::f", socket.AF_INET6)),
    ]:
        assert valid_ip(arg) == retval


def test__fail_valid_ip():
    for arg in ["ya.ru", "1", "1.1.1.", ":", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_ip(arg)


# =====
def test_ok__valid_rfc_host():
    for arg in [
        "yandex.ru",
        "foobar",
        "foo-bar.ru",
        "z0r.de",
        "11.ru",
        "127.0.0.1",
    ]:
        assert valid_rfc_host(arg) == arg


def test_fail__valid_rfc_host():
    for arg in ["foo_bar.ru", "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_rfc_host(arg)


# =====
def test_ok__valid_port():
    for (arg, retval) in [
        ("0",   0),
        (0,     0),
        ("22",  22),
        (443,   443),
        (65535, 65535),
    ]:
        assert valid_port(arg) == retval


def test_fail__valid_port():
    for arg in ["x", 65536, "", None]:
        print(arg)
        with pytest.raises(ValidatorError):
            valid_port(arg)
