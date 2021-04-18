from itertools import permutations

from pytest import mark

from pigment import Color  # pylint: disable=import-error

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


@mark.parametrize('color', [BLACK, WHITE, RED, GREEN, BLUE])
def test_equal(color):
    assert Color(*color) == Color(*color)
    assert Color(*color) == color
    assert color == Color(*color)


@mark.parametrize(
    'color1,color2', permutations([BLACK, WHITE, RED, GREEN, BLUE], 2)
)
def test_not_equal(color1, color2):
    assert Color(*color1) != Color(*color2)
    assert Color(*color1) != color2
    assert color1 != Color(*color2)

    assert Color(*color2) != Color(*color1)
    assert Color(*color2) != color1
    assert color2 != Color(*color1)
