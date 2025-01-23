# 으렵네..! 답지 슬쩍 봤는데 DP 나 DFS 로 푸는 문제라고 한다.

import dataclasses
import heapq
from collections import Counter


@dataclasses.dataclass(order=True)
class Edge:
    total: int = dataclasses.field(default=0)
    elems: list[int] = dataclasses.field(compare=False, default_factory=list)

    def heappush(self, elem: int) -> None:
        heapq.heappush(self.elems, elem)
        self.total += elem

    def heappop(self) -> int:
        elem = heapq.heappop(self.elems)
        self.total -= elem
        return elem


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        """
        https://leetcode.com/problems/matchsticks-to-square/
        모든 성냥을 다 써야 한다... 균등하게 분배하고 시작하는게 맞지 않나?

        배열 4개를 만든 후에 항상 "가장 길이가 작은 배열" 에 채워 넣는다면?

        """
        edge1, edge2, edge3, edge4 = Edge(), Edge(), Edge(), Edge()
        edges = [edge1, edge2, edge3, edge4]
        for i in range(len(matchsticks)):
            min(edges).heappush(matchsticks[i])

        total = sum([edge.total for edge in edges])
        target, remainder = divmod(total, 4)
        if remainder:
            return False


        residue = Counter()

        # target 보다 큰 변의 수와 같은 수의 target 보다 작은 변이 반드시 있다. 1세트가 있든 2세트가 있든
        for edge in edges:
            while edge.total > target:
                elem = edge.heappop()
                residue[elem] += 1

        for edge in edges:
            if edge.total < target:
                to_add = target - edge.total
                if residue[to_add] <= 0:
                    return False
                residue[to_add] -= 1
                edge.heappush(to_add)

        return True

print(Solution().makesquare([10,6,5,5,5,3,3,3,2,2,2,2]))
