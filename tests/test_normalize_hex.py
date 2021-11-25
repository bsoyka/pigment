from pytest import approx, mark, raises

from pigment import normalize_hex  # pylint: disable=import-error

# pylint: disable=import-error
from pigment.exceptions import PigmentError, WrongLengthError


def test_error_inheritance():
    assert issubclass(WrongLengthError, PigmentError)


@mark.parametrize(
    "test_input,expected",
    [("#abcdef", "abcdef"), ("#123456", "123456"), ("#a7b2c8", "a7b2c8")],
)
def test_pound_sign(test_input, expected):
    assert normalize_hex(test_input) == expected


@mark.parametrize(
    "test_input,expected",
    [
        ("ABCDEF", "abcdef"),
        ("FFFFFF", "ffffff"),
        ("000000", "000000"),
        ("aBcDeF", "abcdef"),
        ("a7B4D3", "a7b4d3"),
    ],
)
def test_lowercase(test_input, expected):
    assert normalize_hex(test_input) == expected


@mark.parametrize("test_input", ["a", "AB", "0000", "#49372", "38bcdaef"])
def test_wrong_length(test_input):
    with raises(WrongLengthError):
        normalize_hex(test_input)
