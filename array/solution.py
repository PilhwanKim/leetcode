from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        temp = None
        while True:
            if len(nums) <= i:
                break

            if temp == nums[i]:
                del nums[i]
            else:
                temp = nums[i]
                i = i + 1

        return len(nums)

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(1, len(prices)):
            margin = prices[index] - prices[index - 1]
            if margin > 0:
                profit += margin

        return profit if profit >= 0 else 0

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums) == len(nums_set):
            return False
        return True

    def singleNumber(self, nums: List[int]) -> int:
        single_one_set = set()
        for num in nums:
            if num in single_one_set:
                single_one_set.remove(num)
            else:
                single_one_set.add(num)

        if single_one_set:
            return single_one_set.pop()

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        ret_list = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ret_list.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return ret_list

    def plusOne(self, digits: List[int]) -> List[int]:
        target_num = 0
        for digit in digits:
            target_num *= 10
            target_num += digit
        target_num += 1

        ret_list = []
        while target_num:
            digit = target_num % 10
            target_num = target_num // 10
            ret_list.insert(0, digit)

        return ret_list

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        column_sets = [set() for _ in range(9)]
        subbox_sets = [set() for _ in range(9)]

        for y_index, rows in enumerate(board):
            for x_index, cell in enumerate(rows):
                if cell == '.':
                    continue

                cell_int = int(cell)

                row_set = row_sets[y_index]
                if cell_int in row_set:
                    return False
                row_set.add(cell_int)

                column_set = column_sets[x_index]
                if cell_int in column_set:
                    return False
                column_set.add(cell_int)

                subbox_set = subbox_sets[(y_index // 3) * 3 + (x_index // 3)]
                if cell_int in subbox_set:
                    return False
                subbox_set.add(cell_int)

        return True
