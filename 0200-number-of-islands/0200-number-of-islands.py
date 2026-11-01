
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the dimensions of the grid: m is the number of rows, n is the number of columns
        m, n = len(grid), len(grid[0])

        # Define a helper function for Depth-First Search (DFS) traversal
        def dfs(i, j):
            # Check for out-of-bounds cases or if the current tile is not land ("1")
            # i < 0: out of bounds top | i >= m: out of bounds bottom
            # j < 0: out of bounds left | j >= n: out of bounds right
            # grid[i][j] != "1": tile is water ("0") or has already been visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return # Base case: stop searching this branch and return
            else:
                # Sink the land: mark the current tile as visited by changing it to "0" (water)
                # This eliminates the need for an extra hash set tracking visited positions
                grid[i][j] = "0"
                
                # Recursively explore all 4 adjacent directions to destroy the connected land component
                dfs(i, j + 1) # Explore right neighbor
                dfs(i + 1, j) # Explore down neighbor
                dfs(i, j - 1) # Explore left neighbor
                dfs(i - 1, j) # Explore up neighbor

        # Initialize tracking variable for the total count of isolated islands
        num_island = 0
        
        # Linearly iterate through every single position in the 2D matrix
        for i in range(m):
            for j in range(n):
                # When unvisited land ("1") is encountered, a new island component is discovered
                if grid[i][j] == "1":
                    num_island += 1 # Increment the island counter
                    
                    # Launch DFS to completely eliminate the rest of this island from the grid
                    # This ensures the remaining parts of this specific island won't be double-counted
                    dfs(i, j)
                    
        # Return the final calculated number of connected graph components (islands)
        return num_island
