
from base.intro import hello_world, max_two


def test_hello_world():
    assert hello_world() == 'hello world'


def test_max_two():
    assert max_two() == {
        'english': 'hello world',
        'chinese': '你好世界'
    }
    assert max_two() != {
        'english': 'hello world',
        'japanese': 'ハロー・ワールド'
    }

