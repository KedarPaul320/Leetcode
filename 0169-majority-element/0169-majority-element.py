class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        target_value = max(dict1.values())
        if target_value > n / 2:
            return next(k for k, v in dict1.items() if v == target_value)

            
            
        