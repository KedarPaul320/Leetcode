class Solution :
    def scoreOfParentheses(self,s: str) -> int:
        stack = [0]  # Total score at the current level
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                v = stack.pop()
                # If v == 0, it means it was "()", so score is 1.
                # Otherwise, it was "(A)", so score is 2 * v.
                stack[-1] += max(2 * v, 1)
        return stack.pop()
