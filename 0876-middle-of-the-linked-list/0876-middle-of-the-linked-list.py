# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head 
        # length = 0 
        # while curr != None :
        #     curr = curr.next 
        #     length += 1 
        
        # curr = head 
        # for i in range (length//2):
        #     curr = curr.next 
        # return curr
        
        slow = head 
        fast = head 
        while fast!=None and fast.next != None :
            slow = slow.next 
            fast = fast.next.next 
        return slow 


        