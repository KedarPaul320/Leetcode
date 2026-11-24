class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        l1, l2 = 0, 0
        r1, r2 = len(word1), len(word2)
        
        while l1 < r1 and l2 < r2:
            merged.append(word1[l1])
            merged.append(word2[l2])
            l1 += 1
            l2 += 1
            
        # Append any remaining characters from whichever word is longer
        merged.append(word1[l1:])
        merged.append(word2[l2:])
        
        return "".join(merged)
