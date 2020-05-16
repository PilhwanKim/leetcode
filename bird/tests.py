import unittest
from solution import Solution


class TestStringMethods(unittest.TestCase):
    def test_match_by_hobby(self):
        res = Solution().match_by_hobby([
            'E H R A D W Q C T P',
            'E G U D A M C P V B',
            'E H R D A Q W C T M',
        ])
        self.assertDictEqual(res, {
            ('A', 'C', 'D', 'E', 'H', 'Q', 'R', 'T', 'W'): [0, 2]
        })


if __name__ == '__main__':
    unittest.main()
