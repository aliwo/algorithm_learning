
class Solution:

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        dfs_count = 0
        stack = []
        visited = set()
        for i, nodes in enumerate(isConnected):
            if i not in visited:
                visited.add(i)
                if len(visited) == len(isConnected):
                    return dfs_count + 1
                else:
                    self._do_dfs(i, visited, isConnected, stack)
                    dfs_count += 1

        return dfs_count

    def _do_dfs(self, node_idx: int, visited: set[int], isConnected: list[list[int]], stack: list[int]) -> None:
        for i, node in enumerate(isConnected[node_idx]):
            if node_idx != i and node == 1 and i not in visited:
                stack.append(i)
        while stack:
            nod = stack.pop()
            visited.add(nod)
            for i, node in enumerate(isConnected[nod]):
                if node_idx != i and node == 1 and i not in visited:
                    stack.append(i)

print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
