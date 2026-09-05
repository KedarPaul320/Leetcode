class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dict1 = {arr: 0 for arr in range(1, (n * n) + 1)}
        for i in grid:
            for j in i:
                dict1[j] += 1 

        repeated = -1
        missing = -1
        for key, value in dict1.items():
            if value == 2:
                repeated = key
            elif value == 0:
                missing = key
            if repeated != -1 and missing != -1:
                break

        return [repeated, missing]
