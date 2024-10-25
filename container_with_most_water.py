class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

        아직 못 풀었다... 계속 시간 초과 남 ^^ 이거 풀었던 문제 같은데
        """
        i = 0
        j = len(height) - 1
        result = 0

        for i in range(0, len(height)):
            max_right_height = 0
            for j in reversed(range(i + 1, len(height))):
                if height[j] > max_right_height:
                    cur_water = (j - i) * min(height[j], height[i])
                    if cur_water > result:
                        result = cur_water
                        max_right_height = height[j]

        return result
