class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
        """
        i = 0
        s_i = 0
        while i < len(t):
            if s_i == len(s):
                return True
            if s[s_i] == t[i]:
                s_i += 1
            i += 1
        return s_i == len(s)

print(Solution().isSubsequence("abc", "ahbgdc"))
