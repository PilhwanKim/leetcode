import pytest
from .solution import Solution


def test_containsDuplicate():
    assert Solution().containsDuplicate([1, 2, 3, 1])
    assert Solution().containsDuplicate([1, 2, 3, 4]) == False
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])


def test_single_number():
    assert Solution().singleNumber([2, 2, 1]) == 1
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4


def test_intersect():
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert Solution().intersect([2, 1], [1, 2]) == [1, 2]
    assert Solution().intersect([-2147483648, 1, 2, 3], [1, -2147483648, -2147483648]) == [1, -2147483648]


def test_plusOne():
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_isValidSudoku():
    assert Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]) is True
    assert Solution().isValidSudoku([
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]) is False
