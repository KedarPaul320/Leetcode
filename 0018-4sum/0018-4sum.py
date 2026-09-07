class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array
        n = len(nums)
        result = []


        # Loop for the first number
        for first in range(n - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue  # Skip duplicates


            # Loop for the second number
            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue  # Skip duplicates


                remainingTarget = target - nums[first] - nums[second]
                left, right = second + 1, n - 1


                # Two-pointer approach for remaining two numbers
                while left < right:
                    sum_ = nums[left] + nums[right]


                    if sum_ < remainingTarget:
                        left += 1
                    elif sum_ > remainingTarget:
                        right -= 1
                    else:
                        result.append([nums[first], nums[second], nums[left], nums[right]])


                        # Skip duplicates
                        prevLeft, prevRight = nums[left], nums[right]
                        while left < right and nums[left] == prevLeft:
                            left += 1
                        while left < right and nums[right] == prevRight:
                            right -= 1


        return result