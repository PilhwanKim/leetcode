from typing import List
import time
import itertools


class Solution:
    def match_by_hobby(self, hobbies: List[str]) -> bool:
        # 데이터의 전처리를 한다.
        sorted_hobbies = []
        for user in hobbies:
            hobby = user.split(" ")
            hobby = sorted(hobby)
            sorted_hobbies.append(hobby)

        # 일치하는 취미 갯수가 일치 갯수가 10개 부터 9,8,7 ... 순으로 찾아본다(전부 찾아보지 않기 위함).
        for matching_count in range(10, 0, -1):
            hobby_subset_dict = {}
            # 한 사람의 10개 취미 중에 n개를 뽑는 조합(subset)을 뽑는다.
            # 뽑은 조합을 하나의 hash 에 key로 저장하고, value로 해당되는 user 의 index 를 array 에 넣는다.
            for user_index, user in enumerate(sorted_hobbies):
                hobby_subset_list = itertools.combinations(user, matching_count)
                for hobby_subset in hobby_subset_list:
                    if hobby_subset not in hobby_subset_dict:
                        hobby_subset_dict[hobby_subset] = []
                    hobby_subset_dict[hobby_subset].append(user_index)

            # 일치하는 사람이 2명 이상일 경우가 커플이므로 필터링 한다.
            matched_result = {}
            for (key, value) in hobby_subset_dict.items():
                if len(value) > 1:
                    matched_result[key] = value

            # 결과를 콘솔로 찍고, 결과가 나왔으므로 종료한다.
            if matched_result:
                return matched_result

    @staticmethod
    def print_result(matched_result):
        if not matched_result:
            print(f'취미가 일치하는 커플이 없습니다.')

        for hobby, user_indexes in matched_result.items():
            print(f'일치하는 취미 : {hobby}, 커플 : {user_indexes}')


if __name__ == "__main__":
    with open('500000.txt', 'r') as fd:
        count = int(fd.readline())
        hobbies = fd.read().splitlines()

    start = time.time()
    matched_result = Solution().match_by_hobby(hobbies, count)
    Solution().print_result(matched_result)
    print(f"time :{time.time() - start}")
