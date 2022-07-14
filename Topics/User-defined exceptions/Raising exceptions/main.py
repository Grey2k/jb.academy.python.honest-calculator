class NegativeSumError(Exception):
    pass


def sum_with_exceptions(a, b):
    result = a + b
    if result < 0:
        raise NegativeSumError("Is negative")

    return result
