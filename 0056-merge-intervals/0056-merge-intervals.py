class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Edge case: If the input list is empty, return an empty list immediately
        if not intervals:
            return []
        # Sort intervals by their start value (index 0)
        # Sorting allows us to find overlapping pairs linearly
        intervals.sort(key=lambda x: x[0]) 
        # Initialize output array with the first interval to avoid handling an empty list later
        merged = [intervals[0]]
        # Iterate through remaining intervals starting from the second one
        for start, end in intervals[1:]:
            # Get the end value of the most recently added interval in our output
            lastEnd = merged[-1][1]
            
            # If the current interval's start is less than or equal to the last interval's end, 
            # they are overlapping. Equal counts as overlapping per problem guidelines.
            if start <= lastEnd:
                # Merge them by adjusting the last interval's end to the maximum end value
                # Using max covers edge cases like a fully encapsulated interval (e.g., [1, 5] and)
                merged[-1][1] = max(lastEnd, end)
            else:
                # If they do not overlap, simply append the current interval as a new entry
                merged.append([start, end])
                
        # Return the final array of merged, non-overlapping intervals
        return merged
