import pytest
from ..actions_test.app import wrap_string


class TestWrapString():
    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '#########\n# hello #\n#########'],
        ['hello again', '###############\n# hello again #\n###############'],
        ['hello\nover\nlines', '#########\n# hello #\n# over  #\n# lines #\n#########'],
        ['\nskip\nfirst\nline', '#########\n#       #\n# skip  #\n# first #\n# line  #\n#########'],
    ])
    def test_wrap_string_full(self, word, expected):
        result = wrap_string(word, full=True)
        assert result == expected

    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '\nhello\n#####'],
        ['hello again', '\nhello again\n###########'],
        ['hello\nover\nlines', '\nhello\nover\nlines\n#####'],
        ['\nskip\nfirst\nline', '\n\nskip\nfirst\nline\n#####'],
    ])
    def test_wrap_string_default(self, word, expected):
        result = wrap_string(word)
        assert result == expected

    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '\n# hello #\n'],
        ['hello again', '\n# hello again #\n'],
        ['hello\nover\nlines', '\n# hello #\n# over  #\n# lines #\n'],
        ['\nskip\nfirst\nline', '\n#       #\n# skip  #\n# first #\n# line  #\n'],
    ])
    def test_wrap_string_sides(self, word, expected):
        result = wrap_string(word, bottom=False, sides=True)
        assert result == expected

    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '#####\nhello\n'],
        ['hello again', '###########\nhello again\n'],
        ['hello\nover\nlines', '#####\nhello\nover\nlines\n'],
        ['\nskip\nfirst\nline', '#####\n\nskip\nfirst\nline\n'],
    ])
    def test_wrap_string_top(self, word, expected):
        result = wrap_string(word, bottom=False, top=True)
        assert result == expected

    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '\nhello\n[][][]'],
        ['hello again', '\nhello again\n[][][][][][]'],
        ['hello\nover\nlines', '\nhello\nover\nlines\n[][][]'],
        ['\nskip\nfirst\nline', '\n\nskip\nfirst\nline\n[][][]'],
    ])
    def test_wrap_string_default_long_border(self, word, expected):
        result = wrap_string(word, border='[]')
        assert result == expected

    @pytest.mark.parametrize("word, expected", [
        ['', ''],
        ['hello', '[][][][][][][]\n[]  hello   []\n[][][][][][][]'],
        ['hello again', '[][][][][][][][][][]\n[]  hello again   []\n[][][][][][][][][][]'],
        ['hello\nover\nlines', '[][][][][][][]\n[]  hello   []\n[]  over    []\n[]  lines   []\n[][][][][][][]'],
        ['\nskip\nfirst\nline', '[][][][][][][]\n[]          []\n[]  skip    []\n[]  first   []\n[]  line    []\n[][][][][][][]'],
    ])
    def test_wrap_string_full_long_border(self, word, expected):
        result = wrap_string(word, border='[]', full=True)
        assert result == expected
