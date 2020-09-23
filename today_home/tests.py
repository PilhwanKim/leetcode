from .solution import Solution


def test_reverse_string():
    a = [1, 4, 2]
    b = [4, 5, 3]
    assert Solution().minimize_two_arrays_pair_multiply_sum(a, b) == 25

    a = [6, 1, 9, 5, 4]
    b = [3, 4, 8, 2, 4]
    assert Solution().minimize_two_arrays_pair_multiply_sum(a, b) == 80


def test_winning_team_tag_match():
    front_team = [10, 8, 2, 14]
    backend_team = [4, 4, 12, 16]
    assert Solution().maximum_winning_team_tag_match(front_team, backend_team) == 3

    front_team = [10, 8, 2, 20, 14]
    backend_team = [4, 4, 12, 14, 16]
    assert Solution().maximum_winning_team_tag_match(front_team, backend_team) == 4
