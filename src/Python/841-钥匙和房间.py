class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.rooms = rooms
        self.visited = [0 for i in range(len(rooms))]
        self.dfs(0)
        return 0 not in self.visited

    def dfs(self, door: int):
        if self.visited[door] == 1:
            return
        self.visited[door] = 1
        keys = self.rooms[door]
        for key in keys:
            if key != door:
                self.dfs(key)
        return
