from .solution import Solution


def test_reverseString():
    assert Solution().reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]
    assert Solution().reverseString(["H", "a", "n", "n", "a", "h"]) == ["h", "a", "n", "n", "a", "H"]
    assert Solution().reverseString(["h", "e", "l", "l", "o"]) == ["o", "l", "l", "e", "h"]


def test_reverse():
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
