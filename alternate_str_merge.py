from timeit import timeit
from itertools import zip_longest


class Solution:
    """
    https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
    """
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(self._gen(word1, word2))


    def _gen(self, word1: str, word2: str) -> str:
        for a, b in zip_longest(word1, word2, fillvalue=""):
            yield a
            yield b


s1 = Solution()
print(timeit(lambda: s1.mergeAlternately("abcdef", "pqrs")))  # 2.358640058999299
