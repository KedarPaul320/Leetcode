from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        # Count target character frequencies we need to match
        need = Counter(s1)
        # Initialize the window with the first 'k' characters of s2
        window = Counter(s2[:k])

        # If the very first window is a perfect match, return True immediately
        if need == window:
            return True

        # Slide the window rightward across s2 one character at a time
        for r in range(k, len(s2)):
            # Add the new character entering the right side of the window
            window[s2[r]] += 1
            
            # Remove one instance of the character leaving the left side of the window
            left_char = s2[r - k]
            window[left_char] -= 1
            
            # Python's Counter treats {'a': 0} and {} as unequal during direct == comparison.
            if window[left_char] == 0:
                del window[left_char]
            
            # Check if the current window matches the required character frequencies
            if window == need:
                return True
        
        # If the loop finishes without finding a match, return False
        return False
