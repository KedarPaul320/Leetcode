from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Initialize an empty queue for processing nodes with 0 incoming dependencies
        q = deque()
        # Initialize a list to record the valid order of processed courses
        ans = []
        # Create a list to count incoming dependencies (prerequisites) for each course
        indegree = [0] * numCourses
        # Build an adjacency list representation of the directed graph
        adjList = [[] for _ in range(numCourses)]
         
        # Populate the dependency structures from the prerequisite pairs
        for a,b in prerequisites :
            # b -> a
            # Course a depends on course b, so increment the incoming count for a
            indegree[a] += 1
            # Add course a as a dependent neighbor directed outward from course b
            adjList[b].append(a)

        # Enqueue all courses that have no initial prerequisite obligations
        for i in range(numCourses):
            if indegree[i] == 0:
                ans.append(i)
                q.append(i)
            
        # Process the available courses sequentially using Breadth-First Search (BFS)
        while len(q) > 0 :
            # Extract the front course from the queue whose prerequisites are fully cleared
            front = q.popleft() 
            # Traverse each dependent course that relies on the current course
            for x in adjList[front]:
                # Decrement the dependency tracker for the adjacent course
                indegree[x] -= 1
                # If all prerequisites are successfully resolved for the course, enqueue it
                if indegree[x] == 0:
                    ans.append(x)
                    q.append(x)

        # Return the collected topological ordering of courses (Note: returns partial list if a cycle exists)
        return ans if len(ans) == numCourses else []