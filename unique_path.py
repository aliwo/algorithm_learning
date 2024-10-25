from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75
        """
        queue = deque([(0, 0)])

        while queue[0] != (m - 1, n - 1):
            cur = queue.popleft()
            if cur[0] + 1 < m:
                queue.append((cur[0] + 1, cur[1]))
            if cur[1] + 1 < n:
                queue.append((cur[0], cur[1] + 1))

        return len(queue)


# 와 m = 23, n = 12 에서 Memory Limit Exceeded 터진다... 이거 queue 를 안 쓰고 해야되는거여???

# print(Solution().uniquePaths(2, 3))  # 3
# print(Solution().uniquePaths(3, 3))  # 6
print(Solution().uniquePaths(23, 12))  # 6
