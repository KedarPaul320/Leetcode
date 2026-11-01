class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(city: int):
            # Traverse all potential neighbor cities
            for neighbor in range(n):
                # If they are connected and neighbor hasn't been visited yet
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        # Loop through each city to find unvisited components
        for i in range(n):
            if not visited[i]:
                # Found a new province
                provinces += 1
                visited[i] = True
                dfs(i)

        return provinces
