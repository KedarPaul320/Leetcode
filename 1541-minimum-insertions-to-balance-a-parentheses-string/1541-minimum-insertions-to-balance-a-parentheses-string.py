class Solution:
    def minInsertions(self, s: str) -> int:
        # Determine the total length of the input string
        length = len(s)
        # Initialize counters for required insertions, unmatched open brackets, and the string index pointer
        insertions = left_count = index = 0

        # Traverse the string sequentially from left to right
        while index < length:
            # If the current character is an opening parenthesis, increment the open tracker
            if s[index] == "(":
                left_count += 1
                index += 1
            # If the current character is a closing parenthesis, process the balance requirements
            else:
                # If we have an existing open parenthesis to pair with, match it
                if left_count > 0:
                    left_count -= 1
                # Otherwise, we need to insert an opening parenthesis to match this closing sequence
                else:
                    insertions += 1
                # Look-ahead optimization: check if there is an adjacent second closing parenthesis
                if index < length - 1 and s[index + 1] == ")":
                    # Successfully found a paired double closing parenthesis '))', advance by 2 spaces
                    index += 2
                # If there is no consecutive closing parenthesis, we must insert one right here
                else:
                    insertions += 1
                    index += 1

        # Every remaining unmatched '(' needs two ')' inserted to achieve a balanced state
        insertions += left_count * 2
        # Return the absolute total number of required insertion operations calculated
        return insertions
