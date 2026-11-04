from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, edges: list[list[int]], n: int, s: int) -> int:
        # Initialize an adjacency list using 1-based indexing for n nodes
        adjList = [[] for _ in range(n + 1)]
        # Loop through the edges array to populate connections
        for edge in edges:
            # Extract source node, destination node, and signal travel time weight
            x, y, w = edge[0], edge[1], edge[2]
            # Append directed neighbor connection along with its edge weight
            adjList[x].append([y, w])
            
        # Initialize the priority queue and set all initial node delay times to infinity
        heap, dist = [], [float("inf")] * (n + 1)
        # The time it takes for the signal to reach the starting source node itself is 0
        dist[s] = 0
        # Enqueue the starting node pairing its 0 distance time value into the min-heap
        heappush(heap, (dist[s], s))
        
        # Process the heap iteratively as long as there are pending signal updates
        while len(heap) > 0:
            # Extract the node 'u' with the minimum accumulated signal delay time 'd'
            d, u = heappop(heap)
            
            # Skip processing if this entry is outdated compared to a faster signal path
            if d > dist[u]:
                continue
                
            # Scan all directed neighbor nodes 'v' and their travel costs 'w' from node 'u'
            for v, w in adjList[u]:
                # If path through 'u' allows the signal to reach 'v' faster, relax the edge
                if dist[u] + w < dist[v]:
                    # Update neighbor node 'v' with the shorter total arrival time
                    dist[v] = dist[u] + w
                    # Push the neighbor node and its optimized delay back onto the min-heap
                    heappush(heap, (dist[v], v))
                    
        # Slice from index 1 to ignore the unused 0-th index
        # Find the maximum time it took for the signal to reach the furthest reachable node
        ans = max(dist[1:]) 
        
        # Return integer -1 instead of string "-1"
        # Return -1 if any node remains unvisited (infinity); otherwise return max delay time
        return -1 if ans == float("inf") else ans
