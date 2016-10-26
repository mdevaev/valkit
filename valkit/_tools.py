import re


# =====
class ValidatorError(ValueError):
    pass


# =====
def raise_error(arg, name, err_extra=None):
    err_extra = (": %s" % (err_extra) if err_extra else "")
    raise ValidatorError("The argument '%s' is not a valid %s%s" % (arg, name, err_extra))


def not_none(arg, name):
    if arg is None:
        raise ValidatorError("Empty argument is not a valid %s" % (name))
    return arg


def not_none_strip(arg, name):
    return str(not_none(arg, name)).strip()


def check_chain(arg, name, validators):
    for validator in validators:
        try:
            return validator(arg)
        except Exception:
            pass
    raise_error(arg, name)


def check_re_match(arg, name, pattern, limit=None):
    arg = not_none_strip(arg, name)
    if limit is not None:
        arg = arg[:limit]
    if re.match(pattern, arg) is None:
        raise_error(arg, name)
    return arg


def check_in_list(arg, name, variants):
    if arg not in variants:
        raise_error(arg, name)
    return arg


def check_iterable(arg, item_validator, iterable_validator, pass_none=False):
    if arg is None:
        return (None if pass_none else item_validator(arg))
    return list(map(item_validator, iterable_validator(arg)))


def add_lambda_maker(validator):
    def make(*args, **kwargs):
        return (lambda arg: validator(arg, *args, **kwargs))
    validator.mk = make
    return validator
