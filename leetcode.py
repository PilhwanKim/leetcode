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

        print(nums)
        return len(nums)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for index in range(1, len(prices)):
            margin = prices[index] - prices[index - 1]
            if margin > 0:
                profit += margin

        return profit if profit >= 0 else 0




if __name__ == "__main__":
    # ret = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    ret = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(ret)