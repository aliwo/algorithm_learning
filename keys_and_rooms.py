from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0,}
        queue = deque(rooms[0])
        while len(queue):
            key = queue.popleft()
            if key not in visited:
                visited.add(key)
                for new_key in rooms[key]:
                    queue.append(new_key)
            if len(visited) == len(rooms):
                return True
        return False





print(Solution().canVisitAllRooms([[1],[2],[3],[]]))
