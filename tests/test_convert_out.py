from pigment import Color
from pytest import mark

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)


@mark.parametrize(
    "color,expected",
    [
        (BLACK, "000000"),
        (WHITE, "ffffff"),
        (RED, "ff0000"),
        (GREEN, "00ff00"),
        (BLUE, "0000ff"),
    ],
)
def test_rgb_to_hex(color, expected):
    assert color.hex_code == expected


@mark.parametrize(
    "color,expected",
    [
        (BLACK, (0, 0, 0, 100)),
        (WHITE, (0, 0, 0, 0)),
        (RED, (0, 100, 100, 0)),
        (GREEN, (100, 0, 100, 0)),
        (BLUE, (100, 100, 0, 0)),
    ],
)
def test_rgb_to_cmyk(color, expected):
    assert color.cmyk == expected


@mark.parametrize(
    "color,expected",
    [
        (BLACK, (0, 0, 0)),
        (WHITE, (0, 0, 100)),
        (RED, (0, 100, 100)),
        (GREEN, (120, 100, 100)),
        (BLUE, (240, 100, 100)),
    ],
)
def test_rgb_to_hsv(color, expected):
    assert color.hsv == expected


@mark.parametrize(
    "color,expected",
    [
        (BLACK, (0, 0, 0)),
        (WHITE, (0, 100, 0)),
        (RED, (0, 50, 100)),
        (GREEN, (120, 50, 100)),
        (BLUE, (240, 50, 100)),
    ],
)
def test_rgb_to_hls(color, expected):
    assert color.hls == expected
