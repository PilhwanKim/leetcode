import unittest
from .solution import Solution


class TestStringMethods(unittest.TestCase):
    def test_match_by_hobby(self):
        Solution().match_by_hobby([
            'E H R A D W Q C T P',
            'E G U D A M C P V B',
            'E H R D A Q W C T M',
        ])


if __name__ == '__main__':
    unittest.main()
