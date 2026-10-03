class Solution:
    def compress(self, chars: list[str]) -> int:
        if not chars:
            return 0
            
        ans = []
        current_char = chars[0]
        count = 0
        
        # 1. Loop through characters to build the pairs (Your exact logic structure)
        for i in chars:
            if i == current_char:
                count += 1
            else:
                # Group finished: append the character
                ans.append(current_char)
                # Append the count only if it's greater than 1
                if count > 1:
                    ans.extend(list(str(count)))
                # Reset for the new character group
                current_char = i
                count = 1
                
        # Append the very last group
        ans.append(current_char)
        if count > 1:
            ans.extend(list(str(count)))
            
        # 2. Modify chars in-place to satisfy LeetCode constraints
        chars[:] = ans
        
        return len(chars)
