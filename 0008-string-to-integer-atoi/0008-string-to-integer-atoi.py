class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Read in and ignore any leading white spaces
        s = s.strip()

        # Edge case check: If the string is empty after stripping, return 0
        if not s:
            return 0 

        # Step 2: Initialize sign variable (1 for positive, -1 for negative)
        sign = 1
        result = 0
         
        # FIX: Check the first character s[0], not the entire string s
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                sign = -1 # Update sign variable to negative
            s = s[1:]     # Remove the sign character from the string
        
        # Step 3: Loop through the string character by character
        for char in s:
            # Stop the loop as soon as a non-digit character is reached
            if not char.isdigit():
                break 
            # Shift existing digits to the left and add the new digit value
            result = result * 10 + int(char)

        # Combine the accumulated number with the parsed sign factor
        result = result * sign 

        # Step 4: 32-bit signed integer range clamping logic
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
