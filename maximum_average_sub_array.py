from itertools import accumulate, chain


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        """
        https://leetcode.com/problems/maximum-average-subarray-i/solutions/3532127/py3-beginner-friendly-with-details-and-explanation/?envType=study-plan-v2&envId=leetcode-75
        """
        if len(nums) == 1:
            return nums[0]

        prefix_sum = list(chain([0], accumulate(nums)))
        
        max_subarray_sum = float('-inf')
        for i in range(len(prefix_sum) - k):
            max_subarray_sum = max(prefix_sum[i + k] - prefix_sum[i], max_subarray_sum)
        
        return max_subarray_sum / k
    

print(Solution().findMaxAverage([9,7,3,5,6,2,0,8,1,9], 6))

