class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Initialize the output array with 1s.
        # Per problem constraints, the returned result array does not count as extra memory.
        res = [1] * (len(nums))

        # First pass (Prefix Pass):
        # Calculate the product of all elements to the left of index i .
        prefix = 1 
        for i in range(len(nums)):
            # Place the accumulated prefix product (everything before index i) into res[i] .
            res[i] = prefix 
            # Multiply the current element to update the prefix for subsequent elements .
            prefix *= nums[i]

        # Second pass (Postfix Pass):
        # Calculate the product of all elements to the right of index i .
        # We iterate backwards from the last element to the first .
        postfix = 1 
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the postfix product by the existing prefix product already stored in res[i] .
            res[i] *= postfix 
            # Update the postfix product by including the current number for elements to the left.
            postfix *= nums[i]

        # res now contains: (product of elements to the left) * (product of elements to the right)
        return res