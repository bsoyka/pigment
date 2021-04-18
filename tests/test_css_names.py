from pytest import mark, raises

from pigment import Color  # pylint: disable=import-error


@mark.parametrize(
    'css_name,hex_code',
    [
        ('white', 'ffffff'),
        ('black', '000000'),
        ('red', 'ff0000'),
        ('lime', '00ff00'),
        ('blue', '0000ff'),
    ],
)
def test_css_names(css_name, hex_code):
    assert Color.from_css_name(css_name).hex_code == hex_code


@mark.parametrize('css_name', ['foo', 'bar', 'foobar'])
def test_unknown_css_names(css_name):
    with raises(KeyError):
        Color.from_css_name(css_name)
