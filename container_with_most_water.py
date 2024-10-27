import heapq


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

        와... 자력으로 풀긴 했는데 beats 5% 다.. 흑흑
        """
        heap = []
        far_left = (len(height))
        far_right = 0
        max_result = 0
        for i, h in enumerate(height):
            heapq.heappush(heap, (-h, i))

        while heap:
            elem, i = heapq.heappop(heap)
            if i < far_left:
                far_left = i
            if i > far_right:
                far_right = i
            max_result = max(max_result, -elem * max(i - far_left, far_right - i))

        return max_result





        # i = 0
        # j = len(height) - 1
        # result = 0
        #
        # for i in range(0, len(height)):
        #     max_right_height = 0
        #     for j in reversed(range(i + 1, len(height))):
        #         if height[j] > max_right_height:
        #             cur_water = (j - i) * min(height[j], height[i])
        #             if cur_water > result:
        #                 result = cur_water
        #                 max_right_height = height[j]
        #
        # return result

print(Solution().maxArea([2,3,10,5,7,8,9]))
