from pytest import mark

from pigment import Color, blend  # pylint: disable=import-error


@mark.parametrize(
    'color1,color2,expected',
    [
        (Color(255, 0, 0), Color(0, 255, 0), Color(180, 180, 0)),
        (Color(255, 0, 0), Color(0, 0, 255), Color(180, 0, 180)),
        (Color(0, 255, 0), Color(0, 0, 255), Color(0, 180, 180)),
    ],
)
def test_blend(color1, color2, expected):
    assert blend(color1, color2).rgb == expected.rgb
