from pigment import Color  # pylint: disable=import-error


def test_updating_1():
    c = Color(255, 0, 0)
    assert c.rgb == (255, 0, 0)

    c.hex_code = "00ff00"
    assert c.rgb == (0, 255, 0)

    c.cmyk = (0, 0, 0, 100)
    assert c.rgb == (0, 0, 0)

    c.hsv = (0, 100, 100)
    assert c.rgb == (255, 0, 0)

    c.hue = 60
    assert c.rgb == (255, 255, 0)
