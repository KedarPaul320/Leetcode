class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Create shorter references for the two input arrays
        A , B = nums1 , nums2 
        # Calculate the total combined number of elements across both arrays
        total = len(nums1) + len(nums2)
        # Find the size required for the combined left partition half
        half = total // 2 
        # Ensure array A is always the smaller array to optimize binary search bounds
        if len(B) < len(A):
            A , B = B , A 
        
        # Initialize binary search pointers for the smaller array A
        l , r = 0 , len(A)-1
        # Loop indefinitely until the correct partition point is found
        while True :
            i = (l+r)//2 # A # Midpoint index for partition in array A
            j = half -i -2 #B # Corresponding calculated index for partition in array B

            # Determine boundary values for left and right halves, using infinity for out-of-bounds cases
            Aleft = A[i] if i >=0 else float("-inf")
            Aright = A[i+1] if (i+1) < len(A) else float("inf")
            Bleft = B[j] if j >=0 else float("-inf")
            Bright = B[j+1] if (j+1) < len(B) else float("inf")

            # Check if we found the correct partition where left partition elements <= right partition elements
            if Aleft <= Bright and Bleft <= Aright :
                #odd 
                # If the total number of combined elements is odd, return the minimum of the right values
                if total %2  :
                    return min(Aright,Bright)
                #even 
                # If the total elements are even, return the average of the max left and min right values
                return (max(Aleft, Bleft) + min(Aright,Bright))/2
            # If elements from A's left partition are too big, move the search window left
            elif Aleft > Bright:
                r = i -1 
            # If elements from B's left partition are too big, move the search window right
            else:
                l = i+1
