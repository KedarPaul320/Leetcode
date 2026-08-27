class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not arr :
            return arr 
        max_val = max(arr)
        count = [0]*(max_val+1)
        for num in arr :
            count[num] += 1 
        arr[:] = []
        for num,freq in enumerate(count):
            arr.extend([num]*freq)

        return arr 
         