
class Memo:
    """
    결국 답지 봤다.

    패착:
    - right 와 left 를 따로 생각을 못함...
    - target 에 도달하지 못했다면 right 를 증가 & 도달했다면 left 를 줄여서 길이를 줄이기
        이걸 하면 loop 한 번에 끝나는건데... dp 쓰면서 루프를 한참을 돌고 앉았네...


    """
    def __init__(self, nums: list[int], memo: dict[int, dict[str, int]]):
        self.nums = nums
        self._memo = memo

    @staticmethod
    def get_key(start: int, end: int) -> str:
        return f"{start}_{end}"

    def calc(self, start: int, end: int, length: int) -> int:
        key = self.get_key(start, end - 1)
        if (memo := self._memo[length-1].get(key)):
            result = memo + self.nums[end]
            self._memo[length][self.get_key(start, end)] = result
            # print(f"dp 됨: start: {start} end: {end} result: {result}")
            return result
        else:
            result = sum(self.nums[start:end])
            self._memo[length][self.get_key(start, end)] = result
            # print(f"dp 실패!: start: {start} end: {end} result: {result}")
            return result

    def clear(self, length: int):
        del self._memo[length]

class Solution:
    """
    https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
    """

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """
        어떻게 하면 최적화 할 수 있는가...

        - 택도 안되는 숫자는 건너 뛴다?
        - length 가 1일때 가장 큰 sub array 부터 탐색을 시작한다?
            - 직전 탐색 과정중 sum 값이 가장 큰 array 부터 탐색을 시작한다!
        - 매 번 sum 을 하는게 아니라 sliding window 를 써야 되네 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

        - 아니 DP 를 해도 시간 리밋을 못 넘긴다고....????
        """
        length = 2

        initial_memo = {i: {} for i in range(1, len(nums) + 1)}
        for i, num in enumerate(nums):
            initial_memo[1][Memo.get_key(i, i)] = num
            if num >= target:
                return 1

        if len(nums) < 2:
            return 0

        memo = Memo(nums, initial_memo)
        while length < len(nums):
            for i in range(0, len(nums) - (length - 1)):
                result = memo.calc(i, i + (length - 1), length)
                if result >= target:
                    return length
            memo.clear(length - 1)
            length += 1

        if memo.calc(0, len(nums), len(nums)) >= target:
            return len(nums)
        return 0


assert Solution().minSubArrayLen(15, [1,2,3,4,5]) == 5
assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert Solution().minSubArrayLen(7, [5]) == 0