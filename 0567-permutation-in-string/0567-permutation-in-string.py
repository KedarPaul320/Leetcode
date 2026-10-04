class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1 , len2 = len(s1) , len(s2)
        # Sort s1 once so we can easily compare it later
        sorted_s1 = sorted(s1)
        # Slide a window of length len1 across s2
        for i in range (len2-len1+1):
            # Take a chunk of s2 of the same size as s1
            sub_str = s2[i:i+len1]
            # If the sorted chunk matches the sorted s1, we found a permutation!
            if sorted(sub_str) == sorted_s1:
                return True 
        return False 