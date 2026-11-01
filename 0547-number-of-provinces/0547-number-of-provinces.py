class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # Determine total number of cities
        n = len(isConnected)
        # Track visit status for each city
        visited = [False] * n
        # Initialize component counter
        provinces = 0

        def dfs(city: int):
            # Traverse all potential neighbor cities
            for neighbor in range(n):
                # If they are connected and neighbor hasn't been visited yet
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    # Mark neighbor as visited to prevent duplicate checks
                    visited[neighbor] = True
                    # Recursively traverse the neighbor's connections
                    dfs(neighbor)

        # Loop through each city to find unvisited components
        for i in range(n):
            if not visited[i]:
                # Found a new province
                provinces += 1
                # Mark current starting city as visited
                visited[i] = True
                # Run DFS to sweep the entire connected province component
                dfs(i)

        # Return the total count of provinces found
        return provinces
