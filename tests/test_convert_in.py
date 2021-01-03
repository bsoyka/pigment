from pigment import Color
from pytest import mark

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)


@mark.parametrize(
    "expected,hex_code",
    [
        (BLACK, "000000"),
        (WHITE, "ffffff"),
        (RED, "ff0000"),
        (GREEN, "00ff00"),
        (BLUE, "0000ff"),
    ],
)
def test_hex_to_rgb(expected, hex_code):
    c = Color(0, 0, 0)
    c.hex_code = hex_code
    assert c.rgb == expected.rgb


@mark.parametrize(
    "expected,cmyk",
    [
        (BLACK, (0, 0, 0, 100)),
        (WHITE, (0, 0, 0, 0)),
        (RED, (0, 100, 100, 0)),
        (GREEN, (100, 0, 100, 0)),
        (BLUE, (100, 100, 0, 0)),
    ],
)
def test_cmyk_to_rgb(expected, cmyk):
    c = Color(0, 0, 0)
    c.cmyk = cmyk
    assert c.rgb == expected.rgb


@mark.parametrize(
    "expected,hsv",
    [
        (BLACK, (0, 0, 0)),
        (WHITE, (0, 0, 100)),
        (RED, (0, 100, 100)),
        (GREEN, (120, 100, 100)),
        (BLUE, (240, 100, 100)),
    ],
)
def test_hsv_to_rgb(expected, hsv):
    c = Color(0, 0, 0)
    c.hsv = hsv
    assert c.rgb == expected.rgb


@mark.parametrize(
    "expected,hls",
    [
        (BLACK, (0, 0, 0)),
        (WHITE, (0, 100, 0)),
        (RED, (0, 50, 100)),
        (GREEN, (120, 50, 100)),
        (BLUE, (240, 50, 100)),
    ],
)
def test_hls_to_rgb(expected, hls):
    c = Color(0, 0, 0)
    c.hls = hls
    assert c.rgb == expected.rgb
