import pytest

from pyis import validations


class CustomCallable:
    def __call__(self):
        pass


def test_type_validations():
    assert validations.type.is_int(10)
    assert not validations.type.is_int(True)

    assert validations.type.is_string("Hello")
    assert validations.type.is_float(10.5)

    assert validations.type.is_list([])
    assert validations.type.is_bool(True)
    assert validations.type.is_dict({})
    assert validations.type.is_tuple(())


def test_function_validation():
    def sample():
        pass

    assert validations.type.is_function(sample)
    assert validations.type.is_function(CustomCallable())
    assert not validations.type.is_function(10)


def test_amount_validations():
    assert validations.amount.is_set(0)
    assert validations.amount.is_set(False)
    assert validations.amount.is_set("")

    assert validations.amount.is_empty(None)
    assert not validations.amount.is_empty(0)


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (10, True),
        (1, True),
        (0, False),
        (-1, False),
    ],
)
def test_is_positive(value, expected):
    assert validations.numbers.is_positive(value) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (-10, True),
        (-1, True),
        (0, False),
        (1, False),
    ],
)
def test_is_negative(value, expected):
    assert validations.numbers.is_negative(value) is expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, True),
        (0.0, True),
        (1, False),
        (-1, False),
    ],
)
def test_is_zero(value, expected):
    assert validations.numbers.is_zero(value) is expected
