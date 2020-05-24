from typing import List
import time


class Solution:
    def find_subarray_target_sum(self, input_list: List[int], target: int):
        # 중복 합계 계산을 막기위해
        # 이미 계산된 부분배열 합을 저장하기 위한 hash(dict).
        # key를 해당 부분 배열의 시작,끝 인덱스로 함, value 는 합계
        sum_hash = {}
        count = len(input_list)

        for start_index in range(count):
            for end_index in range(1, count):
                hash_sum = sum_hash.get((start_index, end_index))
                # 이미 합을 구한 구간은 합 구하기를 skip 한다.
                if hash_sum is not None:
                    continue

                # hash 에 없는 값은 부분배열 합을 구함
                sub_sum = sum(input_list[start_index: end_index])
                if sub_sum == target:
                    return input_list[start_index: end_index]
                sum_hash[(start_index, end_index)] = sub_sum

        return None


if __name__ == "__main__":
    with open('input.txt', 'r') as fd:
        count = int(fd.readline())
        inputs = fd.readline().rstrip('\n')
        inputs = inputs.split(' ')
        input_list = [int(item) for item in inputs]
        target = int(fd.readline())

    start = time.time()
    matched_result = Solution().find_subarray_target_sum(input_list, target)
    print(f"matched_result :{matched_result}")
    print(f"time :{time.time() - start}")
