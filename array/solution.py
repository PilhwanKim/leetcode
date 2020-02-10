from typing import List


class Solution:
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



if __name__ == "__main__":
    # ret = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    ret = Solution().containsDuplicate([7, 1, 5, 3, 6, 4])
    print(ret)