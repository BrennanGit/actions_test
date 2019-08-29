import pytest
from app import wrap_string


class TestWrapString():
    @pytest.mark.parametrize("word, expected", [
        ['hello', '#########\n# hello #\n#########'],
        ['hello again', '###############\n# hello again #\n###############'],
        ['hello\nover\nlines', '#########\n# hello #\n# over  #\n# lines #\n#########'],
    ])
    def test_wrap_string_full(self, word, expected):
        result = wrap_string(word, full=True)
        assert result == expected
