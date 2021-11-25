from pytest import mark

from pigment import Color  # pylint: disable=import-error


@mark.parametrize("i", range(5))
def test_random_color(i):
    c = Color.random()

    assert 0 <= c.rgb[0] <= 255
    assert 0 <= c.rgb[1] <= 255
    assert 0 <= c.rgb[2] <= 255


@mark.parametrize("i", range(5))
def test_random_color_black(i):
    c = Color.random((0, 0), (0, 0), (0, 0))

    assert c.rgb == (0, 0, 0)


@mark.parametrize("i", range(5))
def test_random_color_white(i):
    c = Color.random((255, 255), (255, 255), (255, 255))

    assert c.rgb == (255, 255, 255)
