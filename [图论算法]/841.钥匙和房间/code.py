#BFS:
#DFS：
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, queue = {0}, [0]
        while queue:
            room_index = queue.pop()
            for key in rooms[room_index]:
                if key not in visited:
                    visited.add(key)
                    queue.insert(0,key)
        return len(visited) == len(rooms)
