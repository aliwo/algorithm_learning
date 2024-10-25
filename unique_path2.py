class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        https://leetcode.com/problems/unique-paths/description/?envType=study-plan-v2&envId=leetcode-75

        세로 m
        가로 n

        가로가 늘어날때 마다 기존 경우의 수에서 (세로)m - 1 만큼의 경우의 수가 더 생긴다?
        세로가 늘어날때 마다 기존 경우의 수에서 (가로)n - 1 만큼의 경우의 수가 더 생긴다?

        m, n 이 각각 2일때 경우의 수 = 2
        3, 2 = 3
        4, 2 = 4

        3, 3 = 6

        """
        field = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]

        for i in range(1, m):
            for j in range(1, n):
                field[i][j] = field[i-1][j] + field[i][j-1]

        return field[-1][-1]


print(Solution().uniquePaths(3, 7))