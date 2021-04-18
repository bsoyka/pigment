from pytest import mark

from pigment import Color  # pylint: disable=import-error


@mark.parametrize(
    'color,expected',
    [
        (Color(0, 0, 0), '<pigment.Color r=0 g=0 b=0>'),
        (Color(255, 255, 255), '<pigment.Color r=255 g=255 b=255>'),
    ],
)
def test_repr(color, expected):
    assert repr(color) == expected
