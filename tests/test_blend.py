from pytest import mark

from pigment import Color, blend


@mark.parametrize(
    "color1,color2,expected",
    [
        (Color(255, 0, 0), Color(0, 255, 0), Color(128, 128, 0)),
        (Color(255, 0, 0), Color(0, 0, 255), Color(128, 0, 128)),
        (Color(0, 255, 0), Color(0, 0, 255), Color(0, 128, 128)),
    ],
)
def test_blend(color1, color2, expected):
    assert blend(color1, color2).rgb == expected.rgb
