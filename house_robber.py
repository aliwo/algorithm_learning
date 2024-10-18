class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=leetcode-75
        현재 index 가 0일때 0을 터느냐 1을 터느냐.
        이 선택을 매 번 인덱스를 증가시키면서 쌓아나가면 된다.
        쌓아나간 모든 경우의 수 중에서 max 를 리턴하면 끝.
        """

        if len(nums) <= 2:
            return max(nums)
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])

        memo = [0] * len(nums)
        memo[0], memo[1], memo[2] = nums[0], nums[1], nums[0] + nums[2]

        for i, house in enumerate(nums[3:], start=3):
            memo[i] = (max(memo[i - 2], memo[i - 3]) + house)

        return max(memo[-3:])
