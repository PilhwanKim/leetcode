from typing import List


class Solution:
    def minimize_two_arrays_pair_multiply_sum(self, a: List[int], b: List[int]):
        sum_value = 0

        # 두 배열 오름 차순 정렬
        sorted_a = sorted(a)
        sorted_b = sorted(b)

        # 한쪽은 정방향으로 한쪽은 역방향으로 쌍을 만들어 곱하고 합계에 더함
        for i in range(len(a)):
            sum_value += sorted_a[i] * sorted_b[-(i + 1)]

        return sum_value

    def maximum_winning_team_tag_match(self, frontend_team: List[int], backend_team: List[int]):
        sorted_frontend_team = sorted(frontend_team)
        sorted_backend_team = sorted(backend_team)

        winning_count = 0
        frontend_cursor = 0

        for backend_member in sorted_backend_team:
            if backend_member > sorted_frontend_team[frontend_cursor]:
                frontend_cursor = frontend_cursor + 1
                winning_count = winning_count + 1

        return winning_count
