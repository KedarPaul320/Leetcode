class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []  # Total score at the current level
        for char in s:
            if char == '(':
                stack.append(char)
            else:
                # If we see ')' and there is a matching '(' on top, pop it
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    # Otherwise, this ')' is unmatched; save it
                    stack.append(char)

        return len(stack)