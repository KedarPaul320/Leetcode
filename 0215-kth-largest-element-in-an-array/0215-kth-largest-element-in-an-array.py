import heapq as hq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums :
            hq.heappush(min_heap , num)
            if len(min_heap) > k :
                hq.heappop(min_heap)

        return hq.nlargest(k,min_heap)[-1]